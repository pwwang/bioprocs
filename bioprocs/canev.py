# A set of processes for Cancer Evolution analysis
from pyppl import Box, Proc
from . import rimport, params
from .utils import fs2name

"""
@name:
	pSciClone
@description:
	Run sciClone for subclonal analysis.
@input:
	`vfvcfs:files`: The VCF files of mutations of each sample
	`cnvcfs:files`: The VCF files of copy number variations of each sample
@output:
	`outdir:dir`: The output directory.
@args:
	`params`  : Other parameters for original `sciClone` function. Default: `Box()`
	`exfile`  : The regions to be excluded. In BED3 format
	`vfsamcol`: The index of the target sample in mutation VCF file, 1-based. Default: `1`
	`cnsamcol`: The index of the target sample in copy number VCF file, 1-based. Default: `1`
	`varcount`: An R function string to define how to get the variant allele count. Default: `function(fmt) fmt$AD`
		- If this function returns `NULL`, record will be skipped.
		- It can use the sample calls (`fmt`) and also the record info (`info`)
		- Both `function(fmt) ...` and `function(fmt, info) ...` can be used.
		- Don't include `info` if not necessary. This saves time.
		- This function can return the variant count directly, or 
		- an R `list` like: `list(count = <var count>, depth = <depth>)`.
		- By default, the `depth` will be read from `fmt$DP`
	`cncount` : An R function string to define how to get the copy number. Default: `function(fmt) fmt$CN`
		- Similar as `varcount`
		- Returns copy number directly, or
		- an R `list` like: `list(cn = <copy number>, end = <end>, probes = <probes>)`
		- `end` defines where the copy number variation stops
		- `probes` defines how many probes cover this copy number variantion.
"""
pSciClone               = Proc(desc = "Run sciClone")
pSciClone.input         = "vfvcfs:files, cnvcfs:files"
pSciClone.output        = "outdir:dir:{{i.vfvcfs | fs2name}}.sciclone"
pSciClone.envs.fs2name  = fs2name
pSciClone.envs.rimport  = rimport
pSciClone.args.params   = Box()
pSciClone.args.exfile   = ""
pSciClone.args.vfsamcol = 1 # the first sample is the target sample in variant vcf
pSciClone.args.cnsamcol = 1 # the first sample is the target sample in copy number vcf
pSciClone.args.varcount = 'function(fmt) fmt$AD' # how to get the var count
pSciClone.args.cncount  = 'function(fmt) fmt$CN' # how to get the copy number 
pSciClone.lang          = params.Rscript.value
pSciClone.script        = "file:scripts/canev/pSciClone.r"

"""
@name:
	pPyClone
@description:
	Run PyClone for subclonal analysis
@input:
	`vfvcfs:files`: The VCF files of mutations of each sample
	`cnvcfs:files`: The VCF files of copy number variations of each sample
@output:
	`outdir:dir`: The output directory.
@args:
	`params`  : Other parameters for original `PyClone run_analysis_pipeline` function. Default: `Box()`
	`vfsamcol`: The index of the target sample in mutation VCF file, 1-based. Default: `1`
	`cnsamcol`: The index of the target sample in copy number VCF file, 1-based. Default: `1`
	`varcount`: A python lambda string to define how to get the variant allele count. Default: `lambda fmt: fmt.get("AD")`
		- If this function returns `None`, record will be skipped.
		- It can use the sample calls (`fmt`) and also the record info (`info`)
		- Both `function(fmt) ...` and `function(fmt, info) ...` can be used.
		- This function can return the variant count directly, or 
		- a `dict` like: `dict(count = <var count>, depth = <depth>)`.
		- By default, the `depth` will be read from `fmt.DP`
	`cncount` : An python lambda string to define how to get the copy number. Default: `lambda fmt: fmt.get("CN")`
		- Similar as `varcount`
		- Returns copy number directly, or
		- a `dict` like: `dict(cn = <copy number>, end = <end>)`
		- `end` defines where the copy number variation stops
"""
pPyClone               = Proc(desc = "Run pyclone.")
pPyClone.input         = "vfvcfs:files, cnvcfs:files"
pPyClone.output        = "outdir:dir:{{i.vfvcfs | fs2name}}.pyclone"
pPyClone.envs.fs2name  = fs2name
pPyClone.args.params   = Box()
pPyClone.args.vfsamcol = 1 # 1-based
pPyClone.args.cnsamcol = 1
pPyClone.args.varcount = 'lambda fmt: fmt.get("AD")'
pPyClone.args.cncount  = 'lambda fmt: fmt.get("CN")'
pPyClone.args.pyclone  = params.pyclone.value
pPyClone.lang          = params.python.value
pPyClone.script        = "file:scripts/canev/pPyClone.py"