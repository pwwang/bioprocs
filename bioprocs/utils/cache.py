from pyppl import Box
from medoo import Medoo, Function, Field
from . import alwaysList

class Cache(object):

	ARRAY_DELIMIT = ' // '

	DUMMY = dict(
		plain = dict(
			# compose the where conditions from the database column and query data
			# e.g. ('id', [1,2,3,4]) ==medoo==> 'id' IN (1,2,3,4)
			query  = lambda col, data: (col, Cache._uniqueData(data)),
			# tell whether a query item is found from the query results
			find   = lambda col, qitem, results: Cache._plainFinder(col, qitem, results),
			# how to save the data at the column
			insert = lambda col, data: (col, Cache._uniqueData(data)),
			update = lambda col, data, orig: (col, Cache._uniqueData(data)),
		),
		iplain = dict(
			# UPPER(name) in ('ABC', 'DEF', 'GHI')
			query  = lambda col, data: (Function.upper(col + '[ IN ]'), [d.upper() for d in Cache._uniqueData(data)]),
			# name.upper() in
			find   = lambda col, qitem, results: Cache._plainFinder(col, qitem, results, case = True),
			insert = lambda col, data: (col, Cache._uniqueData(data)),
			update = lambda col, data, orig: (col, Cache._uniqueData(data)),
		),
		array = dict(
			query  = lambda col, data: (col + '[~]', Cache._expandLike(data)),
			find   = lambda col, qitem, results: Cache._arrayFinder(col, qitem, results),
			insert = lambda col, data: (col, Cache._arrayJoiner(Cache._uniqueData(data, True))),
			update = lambda col, data, orig: (col, Function.concat(
				Field(col),
				value = Cache._arrayJoiner(
					set(Cache._uniqueData(data, True)) - set(orig)
				))),
			result = lambda data: data if isinstance(data, list) or data is None else list(filter(None, data.split(Cache.ARRAY_DELIMIT)))
		),
		iarray = dict(
			query = lambda col, data: (col + '[~~]', Cache._expandLike(data)),
			find  = lambda col, qitem, results: Cache._arrayFinder(col, qitem, results, case = True),
			insert = lambda col, data: (col, Cache._arrayJoiner(Cache._uniqueData(data, True))),
			update = lambda col, data, orig: (col, Function.concat(
				Field(col),
				value = Cache._arrayJoiner(
					set(Cache._uniqueData(data, True)) - set(orig)
				))),
			result = lambda data: data if isinstance(data, list) or data is None else list(filter(None, data.split(Cache.ARRAY_DELIMIT)))
		)
	)

	def __init__(self, dbfile, table, schema, pkey):
		# if dbfile exists, check table exists, check cols
		# else create the table

		self.medoo = Medoo(
			database_type = 'sqlite',
			database_file = dbfile,
			check_same_thread = True,
			logging = True
		)
		self.table = table
		self.pkey  = pkey
		self.medoo.create(table, schema)

	@staticmethod
	def _arrayJoiner(array, delimit = None):
		delimit = delimit or Cache.ARRAY_DELIMIT
		if array:
			return delimit + delimit.join(array)
		else:
			return ''

	@staticmethod
	def _plainFinder(col, qitem, results, case = False):
		ret = []
		if case: qitem = qitem.upper()
		for result in results:
			target = result[col] if not case else result[col].upper()
			if qitem == target:
				ret.append(result)
		return ret

	@staticmethod
	def _arrayFinder(col, qitem, results, case = False):
		ret = []
		if case: qitem = qitem.upper()
		for result in results:
			target = [r.upper() if case else r for r in result[col]]
			if qitem in target:
				ret.append(result)
		return ret

	@staticmethod
	def _uniqueData(data, forceList = False):
		if isinstance(data, list):
			return list(set(data))
		elif forceList:
			return [data]
		else:
			return data

	@staticmethod
	def _expandLike(data):
		def expand(d):
			return [
				# // abc
				'%{delimit}{data}'.format(data = d, delimit = Cache.ARRAY_DELIMIT),
				# // abc // def
				'%{delimit}{data}{delimit}%'.format(data = d, delimit = Cache.ARRAY_DELIMIT),
			]
		ret = []
		for d in Cache._uniqueData(data, True):
			ret += expand(d)
		return ret

	@staticmethod
	def _queryWhere(cols, data, dummies):
		conditions = []

		if len(cols) == 1:
			conditions.append(Cache._getDummy(cols[0], dummies)['query'](cols[0], data))
		else:
			condkey = 'OR#' + ':'.join(cols)
			conds   = [Cache._getDummy(key, dummies)['query'](key, data) for key in cols]
			conditions.append((condkey, dict(Box(conds))))
		return dict(Box(conditions))

	@staticmethod
	def _find(qitems, results, dummies):
		found = results
		for keys, qitem in qitems.items():
			keys = alwaysList(keys)
			found2 = []
			for key in keys:
				dummy   = Cache._getDummy(key, dummies)
				found2 += dummy['find'](key, qitem, found)
			found = found2
		if found: return found[0]
		#return None

	@staticmethod
	def _checkData(data):
		maxlen = max([len(val) if isinstance(val, list) else 1 for val in data.values()])
		for key, val in data.items():
			if isinstance(val, list) and len(val) > 1 and len(val) != maxlen:
				raise ValueError('Inconsistence of data length.')
			if isinstance(val, list) and len(val) == 1:
				data[key] = val * maxlen
			elif not isinstance(val, list):
				data[key] = [val] * maxlen
		return maxlen

	@staticmethod
	def _getDummy(column, dummies):
		if not dummies or not column in dummies:
			return Cache.DUMMY['plain']
		dummy = dummies[column]
		return dummy if isinstance(dummy, dict) else Cache.DUMMY[dummy]

	@staticmethod
	def _result(data, dummies):
		for key, val in data.items():
			dummy = Cache._getDummy(key, dummies)
			if 'result' in dummy:
				data[key] = dummy['result'](val)
		return data

	def _queryN(self, columns, data, dummies = None):
		"""
		Query the cached database with N records of data
		@params:
			columns: The columns to select, could be list or comma-concatenated string.
			data:    The data used to query, if query on multiple columns, key could be comma-concatenated string.
			dummies: The dummy functions (query, find) of the columns. If not give, will use self.DUMMY.plain
		@returns:
			results: The records with selected columns
			rest:    The data that records not found
		@examples:
			_queryN('name, symbol', {
				'symbol, alias': ['ABC', 'DEF', 'HIG'],
				'speicies': 'human'
			})
		"""
		columns = alwaysList(columns) + [self.pkey]

		conditions = []
		#datalen = Cache._checkData(data)
		datalen = None
		for keys, dt in data.items():
			datalen  = datalen or len(dt)
			keys     = alwaysList(keys)
			columns += keys
			conditions.append(self._queryWhere(keys, dt, dummies))

		if len(conditions) == 1:
			where = conditions[0]
		else:
			where = {'AND': {}}
			for c in conditions:
				where['AND'].update(c)

		rs = self.medoo.select(self.table, list(set(columns)), where)

		results2 = rs.fetchall() if rs else []
		results3  = [Cache._result(result, dummies) for result in results2 if not any([val is None for val in result.values()])]
		del results2[:]

		results = {}
		for i in range(datalen):
			qitems     = {keys:dt[i] for keys, dt in data.items()}
			results[i] = Cache._find(qitems, results3, dummies)

		rest = {}
		for keys, dt in data.items():
			rest[keys] = [d for i, d in enumerate(dt) if not results[i]]

		return {k:r for k,r in results.items() if r}, rest

	def query(self, columns, data, dummies = None, chunk = 1000):
		retall, retrest = {}, {}
		datalen = Cache._checkData(data)
		for i in xrange(0, datalen, chunk):
			datai = {key:val[i:i+chunk] for key, val in data.items()}
			results, rest = self._queryN(columns, datai, dummies)
			retall.update({k+i:v for k,v in results.items()})
			retrest = {key: (val + (retrest[key] if key in retrest else [])) for key, val in rest.items()}
		return retall, retrest

	"""
	data: {
			'id': [4, 5, 6],
			'c2': ['ANAME4', 'ANAME5', 'A6']
	}
	factory: {
		#         update                               insert
		'c2': ((lambda v: Raw('"c2" || \'|%s\'' % v)), lambda v:v)
	}
	"""
	def save(self, data, dummies = None):

		Cache._checkData(data)
		# see whether we should update or insert
		pkdata     = data[self.pkey]
		rs         = self.medoo.select(self.table, '*', {self.pkey: pkdata})
		rsall      = rs.fetchall() if rs else []
		# existing pkeys
		pks        = [r[self.pkey] for r in rsall]
		idxinserts = [i for i, pk in enumerate(pkdata) if pk not in pks]
		idxupdates = [(i, Cache._result(rsall[pks.index(pk)], dummies)) for i, pk in enumerate(pkdata) if pk in pks]
		dataInsert = [
			Box([Cache._getDummy(key, dummies)['insert'](key, val[i]) for key, val in data.items()]) \
			for i in idxinserts
		]
		dataUpdate = [
			(data[self.pkey][i], Box([
				Cache._getDummy(key, dummies)['update'](key, val[i], r[key]) for key, val in data.items() \
				if key != self.pkey
			]))	for i, r in idxupdates
		]

		if dataInsert:
			self.medoo.insert(self.table, *dataInsert, commit = False)
		for pkdataup in dataUpdate:
			pk, dataup = pkdataup
			self.medoo.update(self.table, dataup, {self.pkey: pk}, commit = False)
		self.medoo.commit()
