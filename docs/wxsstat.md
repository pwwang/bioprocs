
## pVcf2List

### description
	Convert vcf to stat files for pCallRate

### input
#### `vcffile:file`:
 The vcf file  

### output
#### `outfile:file`:
 The stat file  

### args
#### `chroms`:
 SNPs on chromosomes to consider, default: "" (all chroms)  
	- use "chr1-22, chrX, chrY" for chr1 to chr22, chrX and chrY

## pCallRate

### description
	Calculate sample/snp call rate from a matrix of snp-sample
	- rows are snps, columns are samples

### input
#### `infile:file`:
    The snp-sample matrix file  

## pCoverageByBamstats

### description
	Use `bamstats` to calculate coverage for bam file

### input
#### `infile:file`:
  The bam file  

### output
#### `outfile:file`:
    The report of coverage for the bam file  

### args
#### `bin`:
 The `bamstats` executable, default: "bamstats"  
#### `params`:
 Other parameters for `bamstats`, default: ""  

## pPlotBamstats

### description
	Plot coverage use output files generated by `bamstats` or `wxs.pCoverageByBamstats`

### input
#### `indir:file`:
 The directory containing bamstats output files  

### args
#### `chroms`:
 Chromosomes to plot. Default: "" (all chroms)  
	- Note: Whether to have "chr" prefix or not depends on your reference when mapping.
	- You can do a scope assignment: "chr1-chr22, chrX, chrY"

## pSnpEff2Stat

### description
	Convert csvstat file from snpEff to R-readable matrix for plotting

### input
#### `indir:file`:
 The directory containing the csv stat files from `snpEff ann`  

### output
#### `outdir:dir`:
 The output directory  

## pPlotSnpEff

### description
	Plot snpEff annotation statistics

### input
#### `indir:file`:
 The snpEff result directory containing matrix files generated by pSnpEff2Stat  

### output
#### `outdir:dir`:
 The output directory  