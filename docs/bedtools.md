
## pBedGetfasta

### description
	`bedtools getfasta` extracts sequences from a FASTA file for each of the intervals defined in a BED file.

### input
#### `infile:file`:
 The input bed file  

### output
#### `outfile:file`:
 The generated fasta file  

### args
#### `ref`     :
 The fasta file  
#### `bedtools`:
 The bedtools executable,                  default: "bedtools"  
#### `params`  :
 Other parameters for `bedtools getfasta`, default: ""  

## pBedClosest

### description
	Similar to intersect, closest searches for overlapping features in A and B. In the event that no feature in B overlaps the current feature in A, closest will report the nearest (that is, least genomic distance from the start or end of A) feature in B. For example, one might want to find which is the closest gene to a significant GWAS polymorphism. Note that closest will report an overlapping feature as the closest that is, it does not restrict to closest non-overlapping feature. The following iconic cheatsheet summarizes the funcitonality available through the various optyions provided by the closest tool.

### input
#### `afile:file`:
   The -a file  
#### `bfiles:files`:
 The -b files  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `params`:
  Other parameters for `bedtools closest`, default: ""  

## pBedFlank

### description
	`bedtools flank` will create two new flanking intervals for each interval in a BED file. Note that flank will restrict the created flanking intervals to the size of the chromosome (i.e. no start < 0 and no end > chromosome size).

### input
#### `infile:file`:
  The input file  
#### `gfile:file`:
   The genome size file  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `params`:
  Other parameters for `bedtools flank`, default: ""  

## pBedIntersect

### description
	By far, the most common question asked of two sets of genomic features is whether or not any of the features in the two sets overlap with one another. This is known as feature intersection. bedtools intersect allows one to screen for overlaps between two sets of genomic features. Moreover, it allows one to have fine control as to how the intersections are reported. bedtools intersect works with both BED/GFF/VCF and BAM files as input.

### input
#### `afile:file`:
   The a file  
#### `bfiles:files`:
 The b files  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `params`:
  Other parameters for `bedtools intersect`, default: ""  

## pBedMakewindows

### description
	Makes adjacent or sliding windows across a genome or BED file.

### input
#### `infile:file`:
 The input file  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `informat`:
The format of input file, whether is a "bed" file or "genome" size file. Default: "bed"  
#### `params`:
  Other parameters for `bedtools makewindows`, default: ""  

## pBedMerge

### description
	`bedtools merge` combines overlapping or book-ended features in an interval file into a single feature which spans all of the combined features.

### input
#### `infile:file`:
 The input file  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `params`:
  Other parameters for `bedtools merge`, default: ""  

## pBedMultiinter

### description
	Identifies common intervals among multiple BED/GFF/VCF files.

### input
#### `infiles:files`:
 The input files  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `params`:
  Other parameters for `bedtools multiinter`, default: ""  

## pBedRandom

### description
	`bedtools random` will generate a random set of intervals in BED6 format. One can specify both the number (-n) and the size (-l) of the intervals that should be generated.

### input
#### `gfile:file`:
 The genome size file  

### output
#### `outfile:file`:
 The result file  

### args
#### `bedtools`:
 The bedtools executable,    default: "bedtools"  
#### `seed`    :
 The seed for randomization, default: None  
#### `gsize`   :
 The chromsize file.  

## pBedShift

### description
	`bedtools shift` will move each feature in a feature file by a user-defined number of bases. While something like this could be done with an awk '{OFS="\t" print $1,$2+<shift>,$3+<shift>}', bedtools shift will restrict the resizing to the size of the chromosome (i.e. no features before 0 or past the chromosome end).

### input
#### `infile:file`:
 The input file  
#### `gfile:file`:
  The genome size file  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `params`:
  Other parameters for `bedtools shift`, default: ""  

## pBedShuffle

### description
	`bedtools shuffle` will randomly permute the genomic locations of a feature file among a genome defined in a genome file. One can also provide an exclusions BED/GFF/VCF file that lists regions where you do not want the permuted features to be placed. For example, one might want to prevent features from being placed in known genome gaps. shuffle is useful as a null basis against which to test the significance of associations of one feature with another.

### input
#### `infile:file`:
 The input file  
#### `gfile:file`:
  The genome size file  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `params`:
  Other parameters for `bedtools shuffle`, default: ""  

## pBedSubtract

### description
	`bedtools subtract` searches for features in B that overlap A. If an overlapping feature is found in B, the overlapping portion is removed from A and the remaining portion of A is reported. If a feature in B overlaps all of a feature in A, the A feature will not be reported.

### input
#### `afile:file`:
 The a file  
#### `bfile:file`:
 The b file  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `params`:
  Other parameters for `bedtools subtract`, default: ""  

## pBedWindow

### description
	Similar to `bedtools intersect`, `window` searches for overlapping features in A and B. However, window adds a specified number (1000, by default) of base pairs upstream and downstream of each feature in A. In effect, this allows features in B that are near features in A to be detected.

### input
#### `afile:file`:
 The a file  
#### `bfile:file`:
 The b file  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `params`:
  Other parameters for `bedtools window`, default: ""  

## pBedGenomecov

### description
	`bedtools genomecov` computes histograms (default), per-base reports (-d) and BEDGRAPH (-bg) summaries of feature coverage (e.g., aligned sequences) for a given genome.
	
	NOTE: only bam file input implemented here.

### input
#### `infile:file`:
 The bam file  

### output
#### `outfile:file`:
 The result file  

### args
#### `bin`:
     The bedtools executable, default: "bedtools"  
#### `params`:
  Other parameters for `bedtools genomecov`, default: "-bg"  