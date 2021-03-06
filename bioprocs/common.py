"""Some commonly-used processes"""
from diot import Diot
from pyppl import Proc
from . import params, proc_factory
from .utils import fs2name

pSort = proc_factory(
	desc   = 'Sort file using linux command `sort`',
	config = Diot(long = """
		@input:
			`infile:file`: The input file
		@output:
			`outfile:file`: The output file
		@args:
			`inopts`: The input options for infile:
				- `skip`   : First N lines to skip. Default: `0`
				- `delimit`: The delimit. Default          : `\t`
			`case`:   Case-sensitivity. Default: True
				- If True, will set $LANG as C
				- Otherwise, $LANG will be set as en_US.UTF-8
			`mem`    : The buffer size. Default: 4G
			`tmpdir` : The tmpdir.
			`unique` : Just keep the unique lines. Default: False
			`delimit`: The delimit to separate the fields. Default: '\t'
			`params` : The arguments used by `sort`
		"""),
	input  = "infile:file",
	output = "outfile:file:{{i.infile | bn}}",
	lang   = params.python.value,
	args   = Diot(
		params = Diot(),
		inopts = Diot(skip = 0, delimit = '\t'),
		case   = True,
		mem    = params.mem4G.value,
		tmpdir = params.tmpdir.value,
		unique = False,
	)
)

pShell = proc_factory(
	desc   = 'Run shell command directly',
	config = Diot(annotate = """
	@input:
		infile: The input file
	@output:
		outfile: The output file
	@args:
		cmd (str): The executable.
	"""),
	lang   = params.python.value,
	input  = 'infile:file',
	output = 'outfile:file:{{i.infile | stem}}.pShell.txt',
	args   = Diot(cmd = None)
)

pFiles2Dir = proc_factory(
	desc   = 'Put files to a directory using symbolic links.',
	lang   = params.python.value,
	config = Diot(annotate = """
	@name:
		pFiles2Dir
	@description:
		A helper process to convert a list of files into a directory, so that some processes can take it as input
	@input:
		`infiles:files`: The input files
	@output:
		`outdir:dir`:    The output directory
	"""),
	input  = "infiles:files",
	output = "outdir:dir:{{i.infiles | lambda x: sorted(x) | [0] | fn}}.dir"
)


pFile2Proc = proc_factory(
	desc="Convert a file to a proc so it can be used as dependent",
	config = Diot(annotate = """
	@name:
		pFile2Proc
	@description:
		Convert a file to a proc so it can be used as dependent
	@input:
		`infile:file`: The input file
	@output:
		`outfile:file`: The output file
	"""))
pFile2Proc.input  = "infile:file"
pFile2Proc.output = "outfile:file:{{i.infile | bn}}"
pFile2Proc.script = 'ln -s "{{i.infile}}" "{{o.outfile}}"'
pFile2Proc.runner = 'local'

pStr2File = proc_factory(
	desc = "Save string to a file.",
	config = Diot(annotate = """
	@name:
		pStr2File
	@description:
		Save string to a file.
	@input:
		`in:var`: The input string.
	@output:
		`outfile:file`: The output file.
	"""))
pStr2File.input           = "instr:var"
pStr2File.output          = "outfile:file:{{i.instr | encode}}.txt"
pStr2File.args.breakOn    = ','
pStr2File.args.trimLine   = True
pStr2File.envs.encode     = lambda x: __import__('re').sub(r'[^\w_]', '', x)[:16]
pStr2File.lang            = params.python.value

pHead = proc_factory(
	desc = "Like linux's head command",
	config = Diot(annotate = """
	@name:
		pHead
	@description:
		Get the top N lines from a file
	@input:
		`infile:file`: The input file
	@output:
		`outfile:file`: The output file
	@args:
		`n`   : Top n lines. You may use '-n' to skip last n lines.
		`pipe`: other piped command to modify the results
	"""))
pHead.input     = "infile:file"
pHead.output    = "outfile:file:{{i.infile | fn}}.head.txt"
pHead.args.n    = 10
pHead.args.pipe = ''
pHead.script    = 'head -n {{args.n}} {{i.infile | squote}} {{"| " + args.pipe if args.pipe else ""}} > {{o.outfile | squote}}'

pTail = proc_factory(
	desc = "Like linux's tail command",
	config = Diot(annotate = """
	@name:
		pTail
	@description:
		Get the bottom N lines from a file
	@input:
		`infile:file`: The input file
	@output:
		`outfile:file`: The output file
	@args:
		`n`: Bottom n lines. You may use '+n' to skip first n lines.
	"""))
pTail.input               = "infile:file"
pTail.output              = "outfile:file:{{i.infile | fn}}.tail.txt"
pTail.args.n              = 10
pTail.script              = 'tail -n {{args.n | lambda x: "+"+str(int(x)+1) if x.startswith("+") else x}} {{i.infile | squote}} > {{out.outfile | squote}}'

pPrepend = proc_factory(
	desc = "Prepend string to a file.",
	config = Diot(annotate = """
	@name:
		pPrepend
	@description:
		Prepend a string to a file
	@input:
		`in:var`: The input string.
		`infile:file`: The input file.
	@output:
		`outfile:file`: The output file.
	"""))
pPrepend.input            = "in:var, infile:file"
pPrepend.output           = "outfile:file:{{i.infile | fn2}}.prepend{{i.infile | ext}}"
pPrepend.script           = '''
printf {{i.in | squote}} > {{out.outfile | squote}}
cat {{i.infile | squote}} >> {{out.outfile | squote}}
'''

pAppend                   = Proc(desc = "Append string to a file")
pAppend.input             = "in:var, infile:file"
pAppend.output            = "outfile:file:{{i.infile | fn2}}.append{{i.infile | ext}}"
pAppend.script            = 'cat {{i.infile | squote}} > {{out.outfile | squote}}; printf {{i.in | squote}} >> {{out.outfile | squote}}'

pUnique = proc_factory(
	desc = "Make the input file unique",
	config = Diot(annotate = """
	@name:
		pUnique
	@description:
		Make the input file with unique rows (at certain column)
	@input:
		`infile:file`: The input file.
	@output:
		`outfile:file`: The output file.
	@args:
		`inopts`: The options for input file
			- `delimit`: delimit for columns
			- `skip`: skip first lines
			- `comment`: signs for treating lines as comments
		`outopts`: The output options
			- `head`: Output head or not. Default: `False`
			- `headPrefix`: The prefix for the head
			- `headDelimit`: The delimit for the head
			- `headTransform`: The transform function for the head
			- `delimit`: The delimit for the data.
		`col`: The column to compare. Default: `*` (all columns)
		`sorted`: Whether the input file is sorted. Default: `False`
	"""))
pUnique.input             = "infile:file"
pUnique.output            = "outfile:file:{{i.infile | fn2}}.unique{{i.infile | ext}}"
pUnique.args.inopts       = Diot(delimit = "\t", skip = 0, comment = "#")
pUnique.args.outopts      = Diot(head = False, headPrefix = '', headDelimit = '\t', headTransform = None, delimit = '\t')
pUnique.args.col          = '*'
pUnique.args.sorted       = False
pUnique.lang              = params.python.value

pAddHeader = proc_factory(
	desc = 'Add the header of 1st file to 2nd file.',
	config = Diot(annotate = """
	@name:
		pAddHeader
	@description:
		Add the header of 1st file to 2nd file.
	@input:
		`infile1:file`: The first file containing the header.
		`infile2:file`: The second file with the body.
	@output:
		`outfile:file`: The output file with the header from 1st input file, body from 2nd file.
	@args:
		`n`: The number of header lines.
	"""))
pAddHeader.input          = "infile1:file, infile2:file"
pAddHeader.output         = "outfile:file:{{i.infile2 | bn}}"
pAddHeader.args.n         = 1
pAddHeader.script         = '''
head -n {{args.n}} {{i.infile1 | squote}} > {{out.outfile | squote}}
cat {{i.infile2 | squote}} >> {{out.outfile | squote}}
'''

pMergeFiles = proc_factory(
	desc   = 'Merge files by rows.',
	lang   = params.python.value,
	config = Diot(annotate = """
	@input:
		infiles: The input files
	@output:
		outfile:file: The output file
	@args:
		header: Whether the input files have header.
			- If `True`, input files must have the same header line.
	"""))
pMergeFiles.input  = 'infiles:files'
pMergeFiles.output = 'outfile:file:{{i.infiles[0] | stem | @append: "_etc.merged"}}{{i.infiles[0] | ext}}'
pMergeFiles.args   = Diot(header = False)

pGrep = proc_factory(
	desc = 'Filter a file using linux grep',
	config = Diot(annotate = """
	@name:
		pGrep
	"""))
pGrep.input        = 'infile:file'
pGrep.output       = 'outfile:file:{{i.infile | bn}}'
pGrep.args.params  = Diot()
pGrep.args.keyword = ''
pGrep.lang         = params.python.value

pSplitRows = proc_factory(
	desc = 'Split a file by rows.',
	config = Diot(annotate = """
	@name:
		pSplitRows
	@description:
		Split a file by rows, specially usefull to split a job into multithreads/multiprocesses.
	@input:
		`infile:file`: The input file
	@output:
		`outdir:dir`: The output directory including the split files
	@args:
		`skip`: The skip first n lines. Default: `0`
		`cnames`: The column names. If True, the column names will be added to each split file. Default: `True`
		`n`: Number of files to split. Default: `8`
	"""))
pSplitRows.input       = 'infile:file'
pSplitRows.output      = 'outdir:dir:{{i.infile | bn}}.rows'
pSplitRows.args.skip   = 0
pSplitRows.args.cnames = True
pSplitRows.args.n      = 8
pSplitRows.lang        = params.python.value
