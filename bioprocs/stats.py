from pyppl import Proc, Box
from . import params, rimport

"""
@name:
	pMetaPval
@description:
	Combine p-values in the files from input directory
@input:
	`indir:dir`: The directory containing the input files
@output:
	`outfile:file`: The output file containing the meta-pvalues
@args:
	`args.pattern`: The pattern used to filter the input files. Default: '*'
	`args.header`: Whether the input files contains a header. Default: True
		- Could be a list to specify it for each file.
		- The order should be concordant with the file names
	`args.pcol`: Which column is the p-value. Default: -1 (last column)
	`args.poutonly`: Only output pvalues. Default: False (output all possible information)
	`args.outheader`: Whether output the header. Default: True
	`args.method`: The method used to calculate the meta-pvalue. Default: sumlog (Fisher's method)
		- Other available methods: logitp, sumz, votep, sump, meanp and wilkinsonp
		- See: https://www.rdocumentation.org/packages/metap/versions/0.8
@requires:
	[`r-matep`](https://www.rdocumentation.org/packages/metap/)
"""
pMetaPval                   = Proc(desc = "Combine p-values.")
pMetaPval.input             = "indir:dir"
pMetaPval.output            = "outfile:file:{{i.indir | fn}}.metapval.txt"
pMetaPval.args.pattern      = "*"
pMetaPval.args.inopts       = Box(
	cnames = True,
	pcol   = -1
)
pMetaPval.args.outopts      = Box(
	ponly  = False,
	head   = True
)
pMetaPval.args.method       = 'sumlog' # fisher's method
pMetaPval.envs.rimport      = rimport
pMetaPval.lang              = params.Rscript.value
pMetaPval.script            = "file:scripts/stats/pMetaPval.r"

"""
@name:
	pMetaPval1
@description:
	Combine p-values in a single file by rows.
@input:
	`infile:file`: The input file
@output:
	`outfile:file`: The output file containing the meta-pvalues
@args:
	`args.header`: Whether the input files contains a header. Default: True
	`args.pcol`: Which column is the p-value. Default: -1 (last column)
	`args.poutonly`: Only output pvalues. Default: False (output all possible information)
	`args.outheader`: Whether output the header. Default: True
	`args.method`: The method used to calculate the meta-pvalue. Default: sumlog (Fisher's method)
		- Other available methods: logitp, sumz, votep, sump, meanp and wilkinsonp
		- See: https://www.rdocumentation.org/packages/metap/versions/0.8
@requires:
	[`r-matep`](https://www.rdocumentation.org/packages/metap/)
"""
pMetaPval1 = Proc(desc = "Combine p-values in a single file by rows.")
pMetaPval1.input             = "infile:file"
pMetaPval1.output            = "outfile:file:{{i.infile | fn}}.metapval.txt"
pMetaPval1.args.inopts       = Box(
	cnames = True,
	pcol   = -1
)
pMetaPval1.args.outopts      = Box(
	ponly  = False,
	head   = True
)
pMetaPval1.args.method       = 'sumlog' # fisher's method
pMetaPval1.lang              = params.Rscript.value
pMetaPval1.script            = "file:scripts/stats/pMetaPval1.r"

"""
@name:
	pSurvival
@description:
	Survival analysis
@input:
	`infile:file`: The input file (header is required).
		- col1: rownames if args.inopts.rnames = True
		- col2: the survival time
		- col3: the status. 0/1 for alive/dead or 1/2 for alive dead
		- col4: var1.
		- ... other variables
@output:
	`outfile:file`: The outfile containing the pvalues
	`outdir:dir`  : The output directory containing the pval files and plots
@args:
	`inunit`    : The time unit in input file. Default: days
	`outunit`   : The output unit for plots. Default: days
	`nthread`   : Number of threads used to perform analysis for groups. Default: 1
	`inopts`    : The options for input file
		- `rnames`: Whether input file has row names. Default: True
	`combine`   : Whether combine groups in the same plot. Default: `Box()`
		- `nrow`: The number of rows. Default: 1
		- `ncol`: The number of cols. Default: 1
	`devpars`   : The device parameters for png. Default: `{res:300, height:2000, width:2000}`
		- The height and width are for each survival plot. If args.combine is True, the width and height will be multiplied by `max(arrange.ncol, arrange.nrow)`
	`covfile`   : The covariant file. Require rownames in both this file and input file.
	`ngroups`   : Number of curves to plot (the continuous number will divided into `ngroups` groups.
	`params`    : The params for `ggsurvplot`. Default: `Box({'risk.table': True, 'conf.int': True, 'font.legend': 13, 'pval': '{method}\np = {pval}'})`
		- You may do `ylim.min` to set the min ylim. Or you can set it as 'auto'. Default: 0. 
	`ggs`       : Extra ggplot2 elements for main plot. `ggs.table` is for the risk table.
	`pval`      : The method to calculate the pvalue shown on the plot. Default: True (logrank)
		- Could also be `waldtest`, `likeratio` (Likelihoold ratio test)
	`method`    : The method to do survival analysis. 
@requires:
	[`r-survival`](https://rdrr.io/cran/survival/)
	[`r-survminer`](https://rdrr.io/cran/survminer/)
"""
pSurvival        = Proc(desc = "Survival analysis.")
pSurvival.input  = 'infile:file'
pSurvival.output = [
	'outfile:file:{{i.infile | fn2}}.dir/{{i.infile | fn2}}.survival.txt', 
	'outdir:dir:{{i.infile | fn2}}.dir'
]
pSurvival.args.inunit    = 'days' # months, weeks, years
pSurvival.args.outunit   = 'days'
pSurvival.args.method    = 'cox' # tm or auto
pSurvival.args.covfile   = None
pSurvival.args.nthread   = 1
pSurvival.args.inopts    = Box(rnames = True)
pSurvival.args.combine   = Box() # params for arrange_ggsurvplots. Typically nrow or ncol is set. If combine.ncol = 3, that means {ncol: 3, nrow: 1}. If ncol is not set, then it defaults to 1. If empty, the figures will not be combined
pSurvival.args.devpars   = Box(res = 300, height = 2000, width = 2000)
pSurvival.args.ngroups   = 2 # how many curves to plot, typically 2. The values will divided into <ngroups> groups for the var
pSurvival.args.autogroup = True # False to use median, else find the best binary split spot, only applicable when args.ngroup = 2
pSurvival.args.params    = Box({'font.legend': 13, 'pval': '{method}\np = {pval}', 'risk.table': True}) # params for ggsurvplot
pSurvival.args.ggs       = Box(table = Box())
pSurvival.args.pval      = True # 'logrank', 'waldtest', 'likeratio' (latter 2 only for cox)
pSurvival.envs.rimport   = rimport
pSurvival.lang           = params.Rscript.value
pSurvival.script         = "file:scripts/stats/pSurvival.r"

"""
@name:
	pPostSurvival
@description:
	Statistic comparison between groups after survival analysis.
@input:
	`infile:file`: The result file from `pSurvival`
	`survfile:file`: The survival data. See format of infile of `pSurvival`
@output:
	`outfile:file`: The output excel file.
@args:
	`covfile`: The covariant file. Require rownames in both this file and input file.
	`methods`: A list of testing methods
		- `wilcox`: Wilcox rank sum test
		- `t`: t-test
		- `chisq`: chisquare-test
	`inopts`: The input options for `i.survfile`.
		- `rnames`: whether the file has row names. This has to be True if `args.covfile` provided.
"""
pPostSurvival              = Proc(desc = "Post survival analysis: statistics on variables in different groups")
pPostSurvival.input        = 'infile:file, survfile:file'
pPostSurvival.output       = 'outfile:file:{{i.infile | fn2}}.stats.xlsx'
pPostSurvival.args.chi2n   = 10
pPostSurvival.args.inopts  = Box(rnames = True)
pPostSurvival.args.covfile = None
pPostSurvival.envs.rimport = rimport
pPostSurvival.lang         = params.Rscript.value
pPostSurvival.script       = "file:scripts/stats/pPostSurvival.r"

"""
@name:
	pBin
@description:
	Bin the data in columns.
@input:
	`infile:file`: The input file
@output:
	`outfile:file`: The output file. Default: `{{i.infile | stem}}.binned{{i.infile | ext}}`
@args:
	`inopts`: The input options.
		- `delimit`: The delimiter. Default: `\t`
		- `rnames`: Whether input file has row names. Default: `False`
		- `cnames`: Whether input file has column names. Default: `True`
		- Other arguments available for `read.table`
	`binopts`: The default bin options:
		- `nbin`: Number of bins.
		- `step`: The step of binning.
		- `nan`:  What to do if the value is not a number. Default: `skip`
			- `skip/keep`: Keep it
			- `as0`: Treat it as 0
		- `out`: The out value. Default: `step`
			- `step`: Use the step breaks
			- `lower/min`: Use the min value of the records in the bin
			- `upper/max`: Use the max value of the records in the bin
			- `mean`: Use the mean value of the records in the bin
			- `median`: Use the median value of the records in the bin
			- `binno`: Use the bin number (empty bins will be skipped).
	`cols`: The detailed bin options for each column. 
		- If not provided (`None`), all columns will use `binopts`. 
		- If column specified, only the specified column will be binned.
		- Column indices can be used. It's 1-based.
"""
pBin              = Proc(desc = "Bin the data")
pBin.input        = 'infile:file'
pBin.output       = 'outfile:file:{{i.infile | stem}}.binned{{i.infile | ext}}'
pBin.args.inopts  = Box(delimit = "\t", rnames = False, cnames = True)
pBin.args.binopts = Box(nbin = None, step = None, nan = 'skip', out = 'step') # lower/min, upper/max, mean, median, binno
pBin.args.cols    = None
pBin.envs.rimport = rimport
pBin.lang         = params.Rscript.value
pBin.script       = "file:scripts/stats/pBin.r"

"""
@name:
	pQuantileNorm
@description:
	Do quantile normalization
@input:
	`infile:file`: The input matrix
@output:
	`outfile:file`: The output matrix. Default: `{{i.infile | bn}}`
"""
pQuantileNorm              = Proc(desc = 'Do quantile normalization')
pQuantileNorm.input        = 'infile:file'
pQuantileNorm.output       = 'outfile:file:{{i.infile | bn}}'
pQuantileNorm.args.inopts  = Box(rnames = True, cnames = True, delimit = "\t", skip = 0)
pQuantileNorm.envs.rimport = rimport
pQuantileNorm.lang         = params.Rscript.value
pQuantileNorm.script       = "file:scripts/stats/pQuantileNorm.r"

"""
@name:
	pChiSquare
@description:
	Do chi-square test.
@input:
	`infile:file`: The input file.
@output:
	`outfile:file` : The output file containing Xsquare, df, pval and method
	`obsvfile:file`: The observation matrix
	`exptfile:file`: The expectation matrix
@args:
	`intype`: The type of the input file:
		- `count` (default): The contingency table
		```
		#         | Disease | Healthy |
		# --------+---------+---------+
		#   mut   |   40    |   12    |
		# non-mut |   23    |   98    |
		# --------+---------+---------+
		```
		- `raw`: The raw values:
		```
		# Contingency table rows: Mut, Non
		# Contingency table cols: Disease, Healthy
		#
		#         | S1 | S2 | ... | Sn |
		# --------+----+----+-----+----+
		# Disease | 1  | 0  | ... | 1  |
		# Healthy | 0  | 1  | ... | 0  |
		# --------+----+----+-----+----+
		# Mut     | 1  | 0  | ... | 1  |
		# Non     | 0  | 1  | ... | 0  |
		```
	`ctcols`: The colnames of contingency table if input file is raw values
		- You may also specify them in the head of the input file
"""
pChiSquare = Proc(desc = "Do chi-square test.")
pChiSquare.input = "infile:file"
pChiSquare.output = "outfile:file:{{i.infile | fn2}}.chi2.txt, obsvfile:file:{{i.infile | fn2}}.obsv.txt, exptfile:file:{{i.infile | fn2}}.expt.txt"
pChiSquare.args.intype = 'cont' # raw
pChiSquare.args.ctcols = ''
pChiSquare.lang = params.Rscript.value
pChiSquare.script = "file:scripts/stats/pChiSquare.r"

"""
@name:
	pFisherExact
@description:
	Do fisher exact test.
@input:
	`infile:file`: The input file.
@output:
	`outfile:file` : The output file containing confInt1, confInt2, oddsRatio, pval, alternative and method.
@args:
	`intype`: The type of the input file:
		- `count` (default): The contingency table
		```
		#         | Disease | Healthy |
		# --------+---------+---------+
		#   mut   |   40    |   12    |
		# non-mut |   23    |   98    |
		# --------+---------+---------+
		```
		- `raw`: The raw values:
		```
		# Contingency table rows: Disease, Healthy
		# Contingency table cols: Mut, Non
		#
		#    | Disease Healthy | Mut  Non  |
		# ---+--------+--------+-----+-----+
		# S1 |    1   |    0   |  0  |  1  |
		# S2 |    0   |    1   |  1  |  0  |
		# .. |   ...  |   ...  | ... | ... |
		# Sn |    0   |    1   |  0  |  1  |
		#
		```
	`ctcols`: The colnames of contingency table if input file is raw values
		- You may also specify them in the head of the input file
"""
pFisherExact             = Proc(desc = "Do fisher exact test.")
pFisherExact.input       = "infile:file"
pFisherExact.output      = "outfile:file:{{i.infile | fn2}}.fexact.txt"
pFisherExact.args.intype = 'cont' # raw
pFisherExact.args.ctcols = []
pFisherExact.lang        = params.Rscript.value
pFisherExact.script      = "file:scripts/stats/pFisherExact.r"

"""
@name:
	pPWFisherExact
@description:
	Do pair-wise fisher exact test.
	Commonly used for co-occurrence/mutual-exclusivity analysis.
	P-value indicates if the pairs are significantly co-occurred or mutually exclusive.
	Co-occurrence: Odds ratio > 1
	Mutual-exclusivity: Odds ratio < 1
@input:
	`infile:file`: The input file.
@output:
	`outfile:file` : The output file containing confInt1, confInt2, oddsRatio, pval, qval, alternative and method.
@args:
	`intype`: The type of the input file:
		- `pairs`: The contingency table
		```
		#
		# A+	B+	4
		# A-	B-	175
		# A+	B-	12
		# A-	B+	1
		#
		```
		- `raw` (default): The raw values:
		```
		#
		#    | A | B | ... | X |
		# ---+---+---+-----+---+
		# S1 | 1 | 0 | ... | 1 |
		# S2 | 0 | 1 | ... | 0 |
		# .. | 0 | 0 | ... | 1 |
		# Sn | 0 | 1 | ... | 1 |
		#
		```
	`padj`: The p-value adjustment method, see `p.adjust.methods` in R. Default: `BH`
	`rnames`: If the input file has rownames for `raw` input type.
"""
pPWFisherExact              = Proc(desc = "Do pair-wise fisher exact test.")
pPWFisherExact.input        = "infile:file"
pPWFisherExact.output       = "outfile:file:{{i.infile | fn2}}.pwfexact.txt"
pPWFisherExact.args.rnames  = True
pPWFisherExact.args.intype  = 'raw' # pairs
pPWFisherExact.args.padj    = 'BH'
pPWFisherExact.envs.rimport = rimport
pPWFisherExact.lang         = params.Rscript.value
pPWFisherExact.script       = "file:scripts/stats/pPWFisherExact.r"

"""
@name:
	pMediation
@description:
	Do mediation analysis
@input:
	`infile:file`: The input file (a matrix or data.frame). Example:
		```
		     V1   V2   V3
		S1   1    2    3
		S2   4    1    8
		... ...
		Sn   3    3    1
		```
	`medfile:file`: The mediation options. Example:
		```
		[Case   ]Mediator	Treat	Outcome	ModelM	ModelY	FmulaM	FmulaY
		[Case1  ]V1         V2      V3      lm      glm     V1 ~ V2 V3 ~ V1 + V2
		[Case2  ]V2         V1      V3      lm      glm     V2 ~ V1 V3 ~ V2 + V1
		```
	`casefile:file`: Defining cases using different rows in infile. If this is specified, then `Case` in `medfile` is required. Example:
		```
		S1   Case1
		S2   Case1
		... ...
		Sm   Case1
		Sm   Case2
		Sm+1 Case2
		... ...
		Sn   Case2
		```
		- Rows can be reused for different cases (`Sm` in the example).
@output:
	`outfile:file`: The result file.
	`outdir:dir`  : The output directory containing output file and plots.
@args:
	`inopts`: The options for input file.
		- `cnames`: Whether the input file has column names
		- `rnames`: Whether the input file has row names
	`medopts`: The options for mediation analysis.
		- `boot`: Use bootstrap?
		- `sims`: How many time simulations?
	`cov`: The covariate file. Default: ``
	`pval`: The pvalue cutoff. Default: `0.05`
	`fdr` : Method to calculate fdr. Use `False` to disable. Default: `True` (`BH`)
	`plot`: Parameters for `plot.mediate`? Use `False` to disable plotting. Default: `Box()`
	`devpars`: device parameters for the plot. Default: `Box(res = 300, width = 2000, height = 2000)`
"""
pMediation = Proc(desc = "Do mediation analysis.")
pMediation.input  = 'infile:file, medfile:file, casefile:file'
pMediation.output = [
	'outfile:file:{{i.infile | fn2}}.mediation/{{i.infile | fn2}}.mediation.txt',
	'outdir:dir:{{i.infile | fn2}}.mediation'
]
pMediation.args.inopts = Box(
	cnames   = True,
	rnames   = True
)
pMediation.args.medopts = Box(
	boot     = True,
	sims     = 500
)
pMediation.args.cov     = ''
pMediation.args.pval    = 0.05
pMediation.args.fdr     = True # BH, or other methods for p.adjust
pMediation.args.plot    = Box()
pMediation.args.devpars = Box(res = 300, width = 2000, height = 2000)
pMediation.envs.rimport = rimport
pMediation.lang         = params.Rscript.value
pMediation.script       = "file:scripts/stats/pMediation.r"

"""
@name:
	pLiquidAssoc
@description:
	Do liquid association analysis
@input:
	`infile:file`: The input file with input data, where LA will be done on rows.
		```
		     S1   S2 ... ... Sn
		G1   1    2  ... ... 9
		G2   3    1  ... ... 1
		... ...
		Gm   9    2  ... ... 3
		```
	`casefile:file`: Defining the groups (X, Y, Z) and the cases. If case (3rd col) is not provided, all will be treated as one case.
		- Group "Z" is required. You can also specify group "X", then the rest will be group "Y"
		```
		G1   X   Case1
		G2   X   Case1
		Gx   Z   Case1
		Gy   Z   Case1
		```
@output:
	`outfile:file`: The results of the analysis
	`outdir:dir`  : The output directory containing the result file and plots.
@args:
	`inopts` : The options for reading input file
	`zcat`   : Whether the group "Z" is categorical. Default: `False`
		- If it is, then `stein lemma` is not suitable, we will calculate LA manually (`E(g'(z)`)
	`pval`   : The pval cutoff. Default: `0.05`
	`fdr`    : The method to calculate FDR. Use `False` to disable. Default: `True` (BH)
	`nthread`: The number of threads to use. Default: `1` (WCGNA requires)
	`plot`   : Whether do plotting or not. Default: `False`
	`devpars`: device parameters for the plot. Default: `Box(res = 300, width = 2000, height = 2000)`
@requires:
	[r-fastLiquidAssociation](https://github.com/pwwang/fastLiquidAssociation)
"""
pLiquidAssoc        = Proc()
pLiquidAssoc.input  = 'infile:file, casefile:file'
pLiquidAssoc.output = [
	'outfile:file:{{i.infile | fn2}}.la/{{i.infile | fn2}}.la.txt',
	'outdir:dir:{{i.infile | fn2}}.la'
]
pLiquidAssoc.args.inopts = Box(
	cnames   = True,
	rnames   = True
)
pLiquidAssoc.args.zcat    = False
pLiquidAssoc.args.pval    = 0.05
pLiquidAssoc.args.fdr     = True # BH, or other methods for p.adjust
pLiquidAssoc.args.fdrfor  = 'case' # all
pLiquidAssoc.args.nthread = 1
pLiquidAssoc.args.plot    = False
pLiquidAssoc.args.ggs     = Box()
pLiquidAssoc.args.devpars = Box(res = 300, width = 2000, height = 2000)
pLiquidAssoc.envs.rimport = rimport
pLiquidAssoc.lang         = params.Rscript.value
pLiquidAssoc.script       = "file:scripts/stats/pLiquidAssoc.r"

"""
@name:
	pHypergeom
@description:
	Do hypergeometric test.
@input:
	`infile:file`: The input file, could be raw data (presence (1) and absence (0) of elements) or number of overlapped elements and elements in each category.
		- Set `args.intype` as `raw` if it is raw data. The population size `args.N` is required
		- Set `args.intype` as `numbers` (or any string except `raw`) if it is numbers. You can specified explicit header: `k` = overlapped elements, `m` = size of set 1, `n` = size of set 2 and `N` = the population size. If `N` not included, then `args.N` is required
@output:
	`outfile:file`: The output file
@args:
	`intype`: the type of input file. Default: `raw`. See `infile:file`
	`inopts`: The options for input file.
		- `cnames`: Whether the input file has column names
		- `rnames`: Whether the input file has row names
	`N`: The population size. Default: `None`
"""
pHypergeom             = Proc(desc = "Do hypergeometric test.")
pHypergeom.input       = 'infile:file'
pHypergeom.output      = 'outfile:file:{{i.infile | fn2}}.hypergeom.txt'
pHypergeom.args.intype = 'raw' # numbers
pHypergeom.args.inopts = Box(
	cnames = True,
	rnames = True
)
pHypergeom.args.N       = None
pHypergeom.envs.rimport = rimport
pHypergeom.lang         = params.Rscript.value
pHypergeom.script       = "file:scripts/stats/pHypergeom.r"

"""
@name:
	pChow
@description:
	Do Chow-Test
@input:
	`infile:file`: The input file for data to do the regressions. Example:
		```
			    X1  X2  X3  X4 ... Y
			G1  1   2   1   4  ... 9
			G2  2   3   1   1  ... 3
			... ...
			Gm  3   9   1   7  ... 8
		```
	`groupfile:file`: Specify the groups to compare. You may also specify the cases. The Chow-Test will be done between the group for each case. Example:
		```
			G1	Group1	Case1
			G2	Group1	Case1
			... ...
			Gs	Group2	Case1
			Gt	Group2	Case1
			Gt	Group1	Case2
			... ...
			Gu	Group1	Case2
			... ...
			Gz	Group2	Case2
		```
		- In such case, the test will be done between Group1 and Group2 for Case1 and Case2, respectively.
		- Instances can be resued (Gt in the example)
		- If cases not provided, all will be treated as one case.
	`casefile:file`: Define the formula (which columns to use for each case). Example:
		```
		Case1	Y ~ X1
		Case2	Y ~ X2
		```
@output:
	`outfile:file`: The result file of chow test. Default: `{{i.infile | fn}}.chow/{{i.infile | fn}}.chow.txt`
	`outdir:dir`: The output directory, containing the output file, results of regressions and plots.
@args:
	`inopts`: The options for input file.
		- `cnames`: Whether the input file has column names. Default: `True`
		- `rnames`: Whether the input file has row names. Default: `True`
	`cov`: The covariate file. `inopts.rnames` required and this file should have row names too. Default: `''`
	`fdr`   : Calculate FDR or not. Use `False` to disable. If `True` will use `BH` method, otherwise, specify the method (see `R`'s `p.adjust`).
	`pval`: The pvalue cutoff. Default: `0.05`
	`plot`: Whether plot the regressions. Default: `False`
	`ggs` : The extra ggs for the plot.
	`devpars`: device parameters for the plot. Default: `Box(res = 300, width = 2000, height = 2000)`
"""
pChow              = Proc(desc = "Do Chow-Test")
pChow.input        = 'infile:file, groupfile:file, casefile:file'
pChow.output       = 'outfile:file:{{i.infile | fn}}.chow/{{i.infile | fn}}.chow.txt, outdir:dir:{{i.infile | fn}}.chow'
pChow.args.inopts  = Box(
	cnames = True,
	rnames = True
)
pChow.args.cov     = '' # co-variates, inopts.rnames required, and must in same order
pChow.args.pval    = 0.05
pChow.args.fdr     = True
pChow.args.plot    = False
pChow.args.devpars = Box(res = 300, width = 2000, height = 2000)
pChow.args.ggs     = Box()
pChow.envs.rimport = rimport
pChow.lang         = params.Rscript.value
pChow.script       = "file:scripts/stats/pChow.r"

"""
@name:
	pCorr
@description:
	Calculate the correlation coefficient for the input matrix
@input:
	`infile:file`: The input file of data to calculate correlations.
@output:
	`outfile:file`: The output file containing the correlation coefficients
	`outdir:dir`  : The output directory containing the outfile and the plot
@args:
	`outfmt`: The output format. Could be `matrix` or `pairs` (default)
	`metohd`: The method used to calculate the correlation coefficient. Default: `pearson`. Could also be `spearman` or `kendall`
	`byrow`:  Calculate the correlation coefficient by row or by col. Default: `True`
	`inopts`: The input options:
		- `cnames`: Whether the input file has header. Default: `True`
		- `rnames`: Whether the input file has row names. Default: `True`
		- `delimit`: The separator of columns. Default: `\t`
	`plot`:   Whether output a correlation plot. Default: `False`
	`params`: The params for `plot.heatmap` in `utils/plot.r`
	`ggs`:    The extra ggplot2 statements.
	`devpars`:The parameters for the plot device. Default: `Box(height = 2000, width = 2000, res = 300)`
@requires:
	R packages: `ggplot2` and `reshape`
"""
pCorr             = Proc(desc = "Calculate the Correlation Coefficient.")
pCorr.input       = 'infile:file'
pCorr.output      = 'outfile:file:{{i.infile | fn}}.{{args.method}}/{{i.infile | fn}}.{{args.method}}.txt, outdir:dir:{{i.infile | fn}}.{{args.method}}'
pCorr.args.outfmt = 'pairs' # matrix
pCorr.args.method = 'pearson' # spearman, kendall
pCorr.args.byrow  = True # else by column
pCorr.args.inopts = Box(
	cnames  = True,
	rnames  = True,
	delimit = "\t"
)
pCorr.args.plot    = False
pCorr.args.params  = Box() # the parameters for plot.heatmap
pCorr.args.ggs     = Box() # extra ggplot statements
pCorr.args.devpars = Box(height = 2000, width = 2000, res = 300)
pCorr.envs.rimport = rimport
pCorr.lang         = params.Rscript.value
pCorr.script       = "file:scripts/stats/pCorr.r"

"""
@name:
	pCorr2
@description:
	Calculate correlation coefficient between instances of two files
	Don't do it between instances within the same file.
@input:
	`infile1:file`: The first file. See input of `pCorr`
	`infile2:file`: The second file.
		- must have same number of columns with `infile1`
@output:
	`outfile:file`: The output file.
	`outdir:dir`  : The output directory containing output file and other files:
		- pvalues/fdr file and plots
@args:
	`pval`  : Whether output pvalue. Default: `False`
	`fdr`   : Whether output qvalue. Default: `False`
	`outfmt`: The output format. `pairs` (default) or `matrix`
	`plot`  : Whether plot a heatmap or not. Default: `False`
	`params`: The params for `plot.heatmap` in `utils/plot.r`
	`ggs`:    The extra ggplot2 statements.
	`devpars`:The parameters for the plot device. Default: `Box(height = 2000, width = 2000, res = 300)`
"""
pCorr2        = Proc(desc = 'Calculate correlation coefficient between instances of two files')
pCorr2.input  = 'infile1:file, infile2:file'
pCorr2.output = [
	'outfile:file:{{i.infile1 | fn2}}-{{i.infile2 | fn2}}.corr/{{i.infile1 | fn2}}-{{i.infile2 | fn2}}.corr.txt', 
	'outdir:dir:{{i.infile1 | fn2}}-{{i.infile2 | fn2}}.corr'
]
pCorr2.args.inopts1 = Box()
pCorr2.args.inopts2 = Box()
pCorr2.args.method  = 'pearson' # spearman, kendall
pCorr2.args.pval    = False
pCorr2.args.fdr     = False # method: 'BH'
pCorr2.args.outfmt  = 'pairs' # matrix
pCorr2.args.plot    = False
pCorr2.args.params  = Box() # the parameters for plot.heatmap
pCorr2.args.ggs     = Box() # extra ggplot statements
pCorr2.args.devpars = Box(height = 2000, width = 2000, res = 300)
pCorr2.envs.rimport = rimport
pCorr2.lang         = params.Rscript.value
pCorr2.script       = "file:scripts/stats/pCorr2.r"

"""
@name:
	pDiffCorr
@description:
	Test correlation differences using Fisher Z method.
@input:
	`infile:file`: The entire dataset used to calculate correlations. Rownames and colnames are required. Example:
		```
			    S1  S2  S3  S4 ... Sn
			G1  1   2   1   4  ... 9
			G2  2   3   1   1  ... 3
			... ...
			Gm  3   9   1   7  ... 8
		```
	`samfile:file`: The sample groups, between which you want to compare the correlations. You can also specify one sample to multiple groups, and assign with different cases. Example:
		```
			S1	Healthy
			S2	Healthy
			S3	Disease
			... ...
			Sn	Disease
		```
	`casefile:file`: Assign the cases to compare. If not provided, it will do for every possible combination. Example:
		```
			Healthy	Disease
		```
	`groupfile:file`: Specify groups for rows, then the correlation will be only done within the pairs, each of which is from different groups (only 2 allowed). If not provided, it will investigate for every possible row pairs. Example:
		```
			G1	Kinase
			G2	Kinase
			... ...
			Gm	TF
		```
@output:
	`outfile:file`: The pairs under different cases that their correlations have been changed significantly
	`outdir:dir`: The output directory containing plots and other output files.
@args:
	`inopts`: The input options for `infile`. `cnames` and `rnames` have to be `True`
	`method`: The method to calculate the correlation. Default: `pearson`
	`pval`  : The pvalue cutoff to define correlation change significance. Default: `0.05`
	`fdr`   : Calculate FDR or not. Use `False` to disable. If `True` will use `BH` method, otherwise, specify the method (see `R`'s `p.adjust`).
	`fdrfor`: Do FDR calculation for each case (`case`) or all instances (`all`). Default: `case`
	`plot`  : Plot the correlation for cases? Default: `False`
	`ggs`   : `ggs` items for the plot.
	`devpars`: The device parameters for the plot.
"""
pDiffCorr = Proc(desc = 'Test correlation differences.')
pDiffCorr.input  = 'infile:file, samfile:file, casefile:file, groupfile:file'
pDiffCorr.output = [
	'outfile:file:{{i.infile | fn2}}.diffcorr/{{i.infile | fn2}}.diffcorr.txt',
	'outdir:dir:{{i.infile | fn2}}.diffcorr'
]
pDiffCorr.args.inopts  = Box(cnames = True, rnames = True)
pDiffCorr.args.method  = 'pearson' # spearman
pDiffCorr.args.pval    = 0.05
pDiffCorr.args.fdr     = True # BH
pDiffCorr.args.fdrfor  = 'case'
pDiffCorr.args.plot    = False
pDiffCorr.args.ggs     = Box() # extra ggplot statements
pDiffCorr.args.devpars = Box(height = 2000, width = 2000, res = 300)
pDiffCorr.envs.rimport = rimport
pDiffCorr.lang         = params.Rscript.value
pDiffCorr.script       = "file:scripts/stats/pDiffCorr.r"
