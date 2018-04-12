infile   = {{in.infile    | quote}}
outfile  = {{out.outfile  | quote}}

{% if args.intype | lambda x: x == 'pair' or x == 'pairs' %}

#
# A+	B+	4
# A-	B-	175 
# A+	B-	12
# A-	B+	1
#
lines       = readLines(infile)
cont.tables = list()
for (line in lines) {
	parts = unlist(strsplit(line, "\t", fixed = T))
	if (length(parts) < 3) {
		stop(paste('Cannot parse line in pair-file:', line))
	}
	name1 = parts[1]
	name2 = parts[2]
	if (!endsWith(name1, '+') && !endsWith(name1, '-')) {
		stop(paste('Name has to end with + or -:', name1))
	}
	if (!endsWith(name2, '+') && !endsWith(name2, '-')) {
		stop(paste('Name has to end with + or -:', name2))
	}
	cname1 = substr(name1, 1, nchar(name1)-1)
	cname2 = substr(name2, 1, nchar(name2)-1)
	name = paste(cname1, cname2, sep = ".vs.")
	if (!name %in% names(cont.tables)) {
		cont.tables[[name]] = matrix(NA, ncol = 2, nrow = 2)
		colnames(cont.tables[[name]]) = c(paste0(cname1, '+'), paste0(cname1, '-'))
		rownames(cont.tables[[name]]) = c(paste0(cname2, '+'), paste0(cname2, '-'))
	}
	cont.tables[[name]][name2, name1] = as.integer(parts[3])
}
# check if we miss any pair values
for (name in names(cont.tables)) {
	if (is.na(cont.tables[[name]]) || F) {
		stop(paste('Missing values in contingency table:', name))
	}
}

{% else %}

#
# 
#         | S1 | S2 | ... | Sn |
# --------+----+----+-----+----+
# A       | 1  | 0  | ... | 1  |
# B       | 0  | 1  | ... | 0  |
# ...     |           ...      |
# X       | 0  | 1  | ... | 0  |
# --------+----+----+-----+----+
#
indata   = read.table(infile, sep = "\t", header = T, row.names = 1, check.names = F)
it.names = rownames(indata)
cont.tables = list()
for (name1 in it.names) {
	for (name2 in it.names) {
		if (name1 >= name2) next
		
		name1plus  = paste0(name1, '+')
		name1minus = paste0(name1, '-')
		name2plus  = paste0(name2, '+')
		name2minus = paste0(name2, '-')
		name1plus.cols  = colnames(indata[, which(indata[name1,]==1), drop = F])
		name1minus.cols = colnames(indata[, which(indata[name1,]==0), drop = F])
		name2plus.cols  = colnames(indata[, which(indata[name2,]==1), drop = F])
		name2minus.cols = colnames(indata[, which(indata[name2,]==0), drop = F])
		cont.table = matrix(0, ncol = 2, nrow = 2)
		rownames(cont.table) = c(name1plus, name1minus)
		colnames(cont.table) = c(name2plus, name2minus)
		
		cont.table[name1plus, name2plus]   = length(intersect(name1plus.cols, name2plus.cols))
		cont.table[name1plus, name2minus]  = length(intersect(name1plus.cols, name2minus.cols))
		cont.table[name1minus, name2plus]  = length(intersect(name1minus.cols, name2plus.cols))
		cont.table[name1minus, name2minus] = length(intersect(name1minus.cols, name2minus.cols))
		
		name = paste(name1, name2, sep = '.vs.')
		cont.tables[[name]] = cont.table
	}
}

{% endif %}

out = matrix(NA, ncol = 7, nrow = 0)
colnames(out) = c('confInt1', 'confInt2', 'oddsRatio', 'pval', 'qval', 'alternative', 'method')

rets  = list()
pvals = c()
ct.names = names(cont.tables)
for (name in ct.names) {
	rets[[name]] = fisher.test(cont.tables[[name]])
	pvals = c(pvals, rets[[name]]$p.value)	
}
qvals = p.adjust(pvals, method = {{args.padj | quote}})
rm (pvals)
for (i in 1:length(ct.names)) {
	name = ct.names[i]
	qval = qvals[i]
	ret  = rets[[name]]
	items = unlist(strsplit(name, '.vs.', fixed = T))
	tmp  = data.frame(
		Name1       = items[1],
		Name2       = items[2],
		confInt1    = round(ret$conf.int[1], 3),
		confInt2    = round(ret$conf.int[2], 3),
		oddsRatio   = round(ret$estimate, 3),
		pval        = round(ret$p.value, 3),
		qval        = round(qval, 3),
		alternative = ret$alternative,
		method      = ret$method
	)
	#rownames(tmp) = name
	out = rbind(out, tmp)
}

write.table(out, outfile, col.names = T, row.names = F, sep = "\t", quote = F)


