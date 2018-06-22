## algorithm

!!! hint "pRWR"

    - **description**  
        Do random walk with restart (RWR)

    - **input**  
        - `Wfile:file`: The adjecent matrix  
        - `Efile:file`: The start vector  

    - **output**  
        - `outfile:file`: The output of final probabilities  

    - **args**  
        - `c`: The restart probability. Default: 0.1  
        - `eps`: The convergent cutoff || R(i+1) - R(i) ||. Default: 1e-5  
        - `niter`: Max iterations to stop. Default: 10000  
        - `normW`: Weather to normalize W or not, default True.   
        	- Laplacian normalization is used (more to add).
        - `normE`: Weather to normalize E or not, default True.   
        	- E will be normalized as: E = E/sum(E)

    - **requires**  
        if normW = True, R package `NetPreProc` is required.

!!! hint "pAR"

    - **description**  
        Affinity Regression.
        Ref: https://www.nature.com/articles/nbt.3343
        ```
                b           c        d          d  
            _________    _______    ____       ____
            |       |    |  W  |    |  |       |  |
          a |   D   |  b |_____|  c |Pt|  =  a |Y |   <=>
            |_______|               |__|       |  |
                                               |__|
        
        kronecker(P, YtD)*vec(W) = vec(YtY)             <=>
        X*vec(W) = vec(YtY)
        WPt:
               c        d              d  
            _______    ____          _____
            |  W  |    |  |          |   |
          b |_____|  c |Pt|  --->  b |___|
                          |__|
        
        YtDW:
        WtDtY:
             b           a        d               d    
          _______    _________   ____           _____  
          |  Wt |    |       |   |  |           |   |  
        c |_____|  b |   Dt  | a |Y |    ---> c |___|  
                     |_______|   |  |                 
                                 |__|                  
        ```

    - **input**  
        - `D:file` : The D matrix  
        - `Pt:file`: The Pt matrix  
        - `Y:file`: The Y matrix  
        	- All input files could be gzipped

    - **output**  
        - `W:file`: The interaction matrix  
        - `outdir:dir`: The output directory  

    - **args**  
        - `seed`: The seed for sampling the training set.  
        - `tfrac`: The fraction of samples used for training.  
        ``
## bed

!!! hint "pBedSort"

    - **description**  
        Sort bed files

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `tool`: The tool used to sort the file. Default: sort (bedtools, bedops)  
        - `bedtools`: The path to bedtools. Default: bedtools  
        - `bedops_sort`: The path to bedops' sort-bed. Default: sort-bed  
        - `mem`: The memory to use. Default: 8G  
        - `tmpdir`: The tmpdir to use. Default: `$TMPDIR`  
        - `unique`: Remove the dupliated records? Default: True  
        - `params`: Other params for `tool`. Default: {}  

    - **requires**  
        [`bedtools`](http://bedtools.readthedocs.io/en/latest/index.html)
        [`bedops`](https://github.com/bedops/bedops)

!!! hint "pBedCluster"

    - **description**  
        Assign cluster id to each record

    - **input**  
        - `infile:file`: The input bed file  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `tool`: The tool used to sort the file. Default: bedtools  
        - `bedtools`: The path to bedtools. Default: bedtools  
        - `params`: Other params for `tool`. Default: ''  

    - **requires**  
        [`bedtools`](http://bedtools.readthedocs.io/en/latest/index.html)
## bedtools

!!! hint "pBedGetfasta"

    - **description**  
        `bedtools getfasta` extracts sequences from a FASTA file for each of the intervals defined in a BED file.

    - **input**  
        - `infile:file`: The input bed file  

    - **output**  
        - `outfile:file`: The generated fasta file  

    - **args**  
        - `ref`     : The fasta file  
        - `bedtools`: The bedtools executable,                  default: "bedtools"  
        - `params`  : Other parameters for `bedtools getfasta`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedClosest"

    - **description**  
        Similar to intersect, closest searches for overlapping features in A and B. In the event that no feature in B overlaps the current feature in A, closest will report the nearest (that is, least genomic distance from the start or end of A) feature in B. For example, one might want to find which is the closest gene to a significant GWAS polymorphism. Note that closest will report an overlapping feature as the closest that is, it does not restrict to closest non-overlapping feature. The following iconic cheatsheet summarizes the funcitonality available through the various optyions provided by the closest tool.

    - **input**  
        - `afile:file`: The -a file  
        - `bfile:file`: The -b file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bedtools`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools closest`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedClosest2"

    - **description**  
        Multiple b-file version of pBedClosest

    - **input**  
        - `afile:file`: The -a file  
        - `bfiles:files`: The -b files  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bedtools`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools closest`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedFlank"

    - **description**  
        `bedtools flank` will create two new flanking intervals for each interval in a BED file. Note that flank will restrict the created flanking intervals to the size of the chromosome (i.e. no start < 0 and no end > chromosome size).

    - **input**  
        - `infile:file`: The input file  
        - `gfile:file`: The genome size file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bin`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools flank`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedIntersect"

    - **description**  
        By far, the most common question asked of two sets of genomic features is whether or not any of the features in the two sets overlap with one another. This is known as feature intersection. bedtools intersect allows one to screen for overlaps between two sets of genomic features. Moreover, it allows one to have fine control as to how the intersections are reported. bedtools intersect works with both BED/GFF/VCF and BAM files as input.

    - **input**  
        - `afile:file` : The a file  
        - `bfile:file`: The b file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bedtools`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools intersect`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedIntersect2"

    - **description**  
        Multiple b-file version of pBedIntersect

    - **input**  
        - `afile:file` : The a file  
        - `bfiles:files`: The b files  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bedtools`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools intersect`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedMakewindows"

    - **description**  
        Makes adjacent or sliding windows across a genome or BED file.

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bin`: The bedtools executable, default: "bedtools"  
        - `informat`: The format of input file, whether is a "bed" file or "genome" size file. Default: "bed"  
        - `params`: Other parameters for `bedtools makewindows`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedMerge"

    - **description**  
        `bedtools merge` combines overlapping or book-ended features in an interval file into a single feature which spans all of the combined features.

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bedtools`: The bedtools executable,               default: "bedtools"  
        - `params`  : Other parameters for `bedtools merge`, default: {}  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedMerge2"

    - **description**  
        A multi-input file model of pBedMerge: Merge multiple input files.

    - **input**  
        - `infiles:files`: The input files  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bedtools`: The bedtools executable,               default: "bedtools"  
        - `params`  : Other parameters for `bedtools merge`, default: {}  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedMultiinter"

    - **description**  
        Identifies common intervals among multiple BED/GFF/VCF files.

    - **input**  
        - `infiles:files`: The input files  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bin`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools multiinter`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedRandom"

    - **description**  
        `bedtools random` will generate a random set of intervals in BED6 format. One can specify both the number (-n) and the size (-l) of the intervals that should be generated.

    - **input**  
        - `gfile:file`: The genome size file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bedtools`: The bedtools executable,    default: "bedtools"  
        - `seed`    : The seed for randomization, default: None  
        - `gsize`   : The chromsize file.  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedShift"

    - **description**  
        `bedtools shift` will move each feature in a feature file by a user-defined number of bases. While something like this could be done with an awk '{OFS="\t" print $1,$2+<shift>,$3+<shift>}', bedtools shift will restrict the resizing to the size of the chromosome (i.e. no features before 0 or past the chromosome end).

    - **input**  
        - `infile:file`: The input file  
        - `gfile:file`: The genome size file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bin`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools shift`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedShuffle"

    - **description**  
        `bedtools shuffle` will randomly permute the genomic locations of a feature file among a genome defined in a genome file. One can also provide an exclusions BED/GFF/VCF file that lists regions where you do not want the permuted features to be placed. For example, one might want to prevent features from being placed in known genome gaps. shuffle is useful as a null basis against which to test the significance of associations of one feature with another.

    - **input**  
        - `infile:file`: The input file  
        - `gfile:file`: The genome size file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bin`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools shuffle`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedSubtract"

    - **description**  
        `bedtools subtract` searches for features in B that overlap A. If an overlapping feature is found in B, the overlapping portion is removed from A and the remaining portion of A is reported. If a feature in B overlaps all of a feature in A, the A feature will not be reported.

    - **input**  
        - `afile:file`: The a file  
        - `bfile:file`: The b file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bin`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools subtract`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedWindow"

    - **description**  
        Similar to `bedtools intersect`, `window` searches for overlapping features in A and B. However, window adds a specified number (1000, by default) of base pairs upstream and downstream of each feature in A. In effect, this allows features in B that are near features in A to be detected.

    - **input**  
        - `afile:file`: The a file  
        - `bfile:file`: The b file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bin`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools window`, default: ""  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)

!!! hint "pBedGenomecov"

    - **description**  
        `bedtools genomecov` computes histograms (default), per-base reports (-d) and BEDGRAPH (-bg) summaries of feature coverage (e.g., aligned sequences) for a given genome.
        
        NOTE: only bam file input implemented here.

    - **input**  
        - `infile:file`: The bam file  

    - **output**  
        - `outfile:file`: The result file  

    - **args**  
        - `bin`: The bedtools executable, default: "bedtools"  
        - `params`: Other parameters for `bedtools genomecov`, default: "-bg"  

    - **requires**  
        [bedtools](http://bedtools.readthedocs.io/en/latest/index.html)
## chipseq

!!! hint "pPeakToRegPotential"

    - **description**  
        Convert peaks to regulatory potential score for each gene
        The formula is:
        ``
        	             -(0.5 + 4*di/d0)
        PC = sum (pi * e                  )
        ``
        Ref: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489297/

    - **input**  
        - `peakfile:file`: The BED/peak file for peaks  
        - `genefile:file`: The BED file for gene coordinates  

    - **output**  
        - `outfile:file`: The regulatory potential file for each gene  

    - **args**  
        - `intensity`: `pi` in the formula. Boolean value, whether use the peak intensity or not, default: `True`,  
        - `geneformat`: The format for `genefile`, default: `ucsc+gz`. It could be:  
        	- ucsc or ucsc+gz: typically, you can download from http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/refGene.txt.gz
        	- bed or bed+gz: [format](https://genome.ucsc.edu/FAQ/FAQformat#format1), 4th column required as gene identity.
        - `peakformat`: The format for `peakfile`, default: `peak`. It could be:  
        	- peak or peak+gz: (either [narrowPeak](https://genome.ucsc.edu/FAQ/FAQformat.html#format12) or [broadPeak](https://genome.ucsc.edu/FAQ/FAQformat.html#format13), the 7th column will be used as intensity
        	- bed or bed+gz: [format](https://genome.ucsc.edu/FAQ/FAQformat#format1), 5th column will be used as intensity.
        - `window`: `2 * d0` in the formula. The window where the peaks fall in will be consided, default: `100000`.   
        ``
        	|--------- window ----------|
        	|---- d0 -----|
        	|--- 50K --- TSS --- 50K ---|
        	     ^ (peak center)
        	     |-- di --|
        ``
## cluster

!!! hint "pDist2Coords"

    - **description**  
        Convert a distance matrix to coordinates, using multidimensional scaling.

    - **input**  
        - `infile:file`: The distance matrix, could be a full distance matrix, a triangle matrix or a pair-wise distance file  
        	- full dist matrix (full):
        	```
        		s1	s2	s3
        	s1	0	1	1
        	s2	1	0	1
        	s3	1	1	0
        	```
        	- triangle matrix (upper/lower), could be also lower triangle
        	```
        		s1	s2	s3
        	s1	0	1	1
        	s2		0	1
        	s3			0
        	```
        	- pair-wise (pair): (assuming auto-pair-wise distance = 0, that is: `s1	s1	0`)
        	```
        	s1	s2	1
        	s1	s3	1
        	s2	s3	1
        	```
        	- Both rownames and header are required.

    - **output**  
        - `outfile:file`: The output coordinate file  

    - **args**  
        - `informat`: The format of the input file: full, triangle or pair. Default: full  
        	- Could also be upper, lower, pair
        - `k`: How many dimensions? Default: 2 (R^2)  

!!! hint "pCluster"

    - **description**  
        Use `optCluster` to select the best number of clusters and cluster method, then perform the clustering

    - **input**  
        - `infile:file`: The input matrix file. Clustering will be performed against rows. If not, set `args.transpose` = True  

    - **output**  
        - `outfile:file`: The output cluster file  
        - `outdir:dir`: The output directory containing the figures  

    - **args**  
        - `transpose`: Transpose the input matrix. Default: False  
        - `cnames`: Whether the input matrix contains header before transposing. Default: False  
        - `rnames`: Which column is the rownames before transposing. Default: 1  
        - `plot`: Whether plot the cluster. Default: True  
        - `minc`: Min number of clusters to test. Default: 2  
        - `maxc`: Min number of clusters to test. Default: 15  
        	- If number of rows (nrows) <= 15, then max = nrows - 1
        - `methods`: The methods to test. Default: "all"  
        	- Could be any of "agnes", "clara", "diana", "fanny", "hierarchical", "kmeans", "model", "pam", "som", "sota", "em.nbinom", "da.nbinom", "sa.nbinom", "em.poisson", "da.poisson", "sa.poisson"
        	- Multiple methods could be separated by comma (,), or put in a list
        	- By default, fanny, model and sota will be excluded because fanny causes error and the latter two are slow. You can manually include them if you want.
        	- Improper methods will be automatically excluded by `args.isCount`
        - `isCount`: Whether the data is count data. Corresponding methods will be tested. Default: False  

    - **requires**  
        [`r-optCluster`](https://rdrr.io/cran/optCluster/man/optCluster.html)
        [`r-factoextra`](https://cran.r-project.org/web/packages/factoextra/index.html)

!!! hint "pMCluster"

    - **description**  
        Use `r-mclust` to do clustering. Current just do simple clustering with the package

    - **input**  
        - `infile:file`: The input a coordinate file  

    - **output**  
        - `outdir:dir`: The output of final results  

    - **args**  
        - `transpose`: Transpose the input matrix? Default: False  
        - `rnames`: The `row.names` for `read.table` to read the input file, default: True.  
        - `cnames`: The `header` argument for `read.table` to read the input file, default: True.  
        - `caption`: The caption for the `fviz_cluster`, default: "CLARA Clustering".  
        - `minc`: The min # clusters to try, default: 2  
        - `maxc`: The max # clusters to try, default: 15  

    - **requires**  
        [`r-mclust`](https://cran.r-project.org/web/packages/mclust/index.html)
        [`r-factoextra`](https://cran.r-project.org/web/packages/factoextra/index.html)

!!! hint "pAPCluster"

    - **description**  
        Use `r-apcluster` to do clustering. 

    - **input**  
        - `infile:file`: The input a coordinate file  

    - **output**  
        - `outdir:dir`: The output of final results  

    - **args**  
        - `transpose`: Transpose the input matrix? Default: False  
        - `rownames`: The `row.names` for `read.table` to read the input file, default: 1.  
        - `header`: The `header` argument for `read.table` to read the input file, default: True.  
        - `caption`: The caption for the `fviz_cluster`, default: "APClustering".  

    - **requires**  
        [`r-apcluster`](https://cran.r-project.org/web/packages/apcluster/index.html)
        [`r-factoextra`](https://cran.r-project.org/web/packages/factoextra/index.html)

!!! hint "pHCluster"

    - **description**  
        Do hierarchical clustering.

    - **input**  
        - `infile:file`: The input files with variants as rows, features as columns.  
        	- NOTE: clustering is performed on rows, rownames are the leaf labels.

    - **output**  
        - `outdir:dir`: The result directory, containing:  
        	- `hclust.merge.txt`: including merge and height information
        	- `hclust.order.txt`: including order and labels information
        	- `hclust.png`:       the dendrogram plot

    - **args**  
        - `fast`: whether to use `fastcluster` package or not, default: False  
        - `gg`: whether to use `ggdendro` or not, default: False  
        - `rownames`: The `row.names` for `read.table` to read the input file, default: 1.  
        - `header`: The `header` argument for `read.table` to read the input file, default: True.  
        - `method`: Which method to use for `hclust`. Default: "complete" (use `?hclust` to check all availables)  
        - `rotate`: Which to rotate the plot or not. Default: False  
        - `transpose`: Whether to transpose the matrix before cluster. Default: False  

    - **requires**  
        [`r-fastcluster`](https://cran.r-project.org/web/packages/fastcluster/index.html) if `args.fast` is True
        [`r-ggdendro`](https://cran.r-project.org/web/packages/ggdendro/index.html) if `args.gg` is True
## cnvkit

!!! hint "pCNVkitAccess"

    - **description**  
        Calculate the sequence-accessible coordinates in chromosomes from the given reference genome, output as a BED file.

    - **input**  
        - `fafile:file`: The fasta file  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `params`: Other parameters for `cnvkit.py access`  
        - `cnvkit`: The executable of cnvkit. Default: 'cnvkit.py'  

    - **requires**  
        [CNVkit](http://cnvkit.readthedocs.io/)

!!! hint "pCNVkitTarget"

    - **description**  
        Generate targets file for CNVkit using access file and annotate file (`cnvkit.py target`)

    - **input**  
        - `acfile:file`: The access file  
        - `anfile:file`: The annotate file  

    - **output**  
        - `outfile:file`: The targets file  

    - **args**  
        - `cnvkit`: The executable of cnvkit. Default: 'cnvkit.py'  
        - `params`: Other parameters for `cnvkit.py target`  

    - **requires**  
        [CNVkit](http://cnvkit.readthedocs.io/)

!!! hint "pCNVkitCov"

    - **description**  
        Calculate coverage in the given regions from BAM read depths.

    - **input**  
        - `infile:file`: The bam file  

    - **output**  
        - `outfile:file`: The output cnn file  

    - **args**  
        - `tgfile`: The target file  
        - `cnvkit`: The executable of cnvkit. Default: 'cnvkit.py'  
        - `nthread`: The number of threads to use. Default: 1  
        - `params`: Other parameters for `cnvkit.py coverage`  

    - **requires**  
        [CNVkit](http://cnvkit.readthedocs.io/)

!!! hint "pCNVkitRef"

    - **description**  
        Compile a copy-number reference from the given files or directory (containing normal samples). If given a reference genome (-f option), also calculate the GC content and repeat-masked proportion of each region.

    - **input**  
        - `indir:file`: The input directory containing the cnn files  

    - **output**  
        - `outfile:file`: The output reference cnn file  

    - **args**  
        - `cnvkit`: The executable of cnvkit. Default: 'cnvkit.py'  
        - `params`: Other parameters for `cnvkit.py reference`, default: " --no-edge "  

    - **requires**  
        [CNVkit](http://cnvkit.readthedocs.io/)

!!! hint "pCNVkitFix"

    - **description**  
        Combine the uncorrected target and antitarget coverage tables (.cnn) and correct for biases in regional coverage and GC content, according to the given reference. Output a table of copy number ratios (.cnr)

    - **input**  
        - `infile:file`: The cnn file to be fixed  
        - `rcfile:file`: The reference cnn file  

    - **output**  
        - `outfile:file`: The cnr file  

    - **args**  
        - `cnvkit`: The executable of cnvkit. Default: 'cnvkit.py'  
        - `params`: Other parameters for `cnvkit.py fix`, default: " --no-edge "  

    - **requires**  
        [CNVkit](http://cnvkit.readthedocs.io/)

!!! hint "pCNVkitSeg"

    - **description**  
        Infer discrete copy number segments from the given coverage table

    - **input**  
        - `infile:file`: The cnr file   

    - **output**  
        - `outfile:file`: The cns file  

    - **args**  
        - `cnvkit`: The executable of cnvkit. Default: 'cnvkit.py'  
        - `nthread`: The number of threads to use. Default: 1  
        - `params`: Other parameters for `cnvkit.py segment`, default: ""  

    - **requires**  
        [CNVkit](http://cnvkit.readthedocs.io/)

!!! hint "pCNVkitCall"

    - **description**  
        Given segmented log2 ratio estimates (.cns), derive each segment's absolute integer copy number 

    - **input**  
        - `infile:file`: The cns file   

    - **output**  
        - `outfile:file`: The callcns file  

    - **args**  
        - `cnvkit`: The executable of cnvkit. Default: 'cnvkit.py'  
        - `params`: Other parameters for `cnvkit.py segment`, default: ""  

    - **requires**  
        [CNVkit](http://cnvkit.readthedocs.io/)

!!! hint "pCNVkitPlot"

    - **description**  
        Plot CNVkit results

    - **input**  
        - `cnrdir:file`: The directory containing copy number ratio files  
        - `cnsdir:file`: The directory containing copy number segment files  

    - **output**  
        - `outdir:dir`: The output directory  

    - **args**  
        - `cnvkit`: The executable of cnvkit. Default: 'cnvkit.py'  
        - `region`: The region for zoom-in plots. Default: '' (don't plot zoom-in view)  
        - `gene`: The genes to be highlighted. Default: ''  
        - `scatter`: Whether to generate the scatter plot. Default: True  
        - `diagram`: Whether to generate the diagram plot. Default: True  
        - `heatmap`: Whether to generate the heatmap plot. Default: True  

    - **requires**  
        [CNVkit](http://cnvkit.readthedocs.io/)

!!! hint "pCNVkitRpt"

    - **description**  
        Report CNVkit results

    - **input**  
        - `cnrfile:file`: The file containing copy number ratio  
        - `cnsfile:file`: The file containing copy number segment  

    - **output**  
        - `outdir:dir`: The output directory  

    - **args**  
        - `cnvkit`: The executable of cnvkit. Default: 'cnvkit.py'  
        - `breaks`: Whether to report breakpoints. Default: True  
        - `gainloss`: Whether to report gainloss. Default: True  
        - `metrics`: Whether to report metrics. Default: True  
        - `segmetrics`: Whether to report segmetrics. Default: True  

    - **requires**  
        [CNVkit](http://cnvkit.readthedocs.io/)

!!! hint "pCNVkit2Vcf"

    - **description**  
        Output vcf file for cnvkit results

    - **input**  
        - `cnsfile:file`: The cns file  

    - **output**  
        - `outfile:file`: The vcf file  

    - **args**  
        - `cnvkit`: The executable of cnvkit. Default: 'cnvkit.py'  
        - `params`: Other params for `cnvkit.py export`  

    - **requires**  
        [CNVkit](http://cnvkit.readthedocs.io/)
## common

!!! hint "pSort"

    - **description**  
        Sort file using linux command `sort`

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `skip`: To skip first N lines. Default: 0  
        - `case`: Case-sensitivity. Default: True  
        	- If True, will set $LANG as C
        	- Otherwise, $LANG will be set as en_US.UTF-8
        - `mem`    : The buffer size. Default: 4G  
        - `tmpdir` : The tmpdir.  
        - `unique` : Just keep the unique lines. Default: False  
        - `delimit`: The delimit to separate the fields. Default: '\t'  
        - `params` : The arguments used by `sort`  

!!! hint "pFiles2Dir"

    - **description**  
        A helper process to convert a list of files into a directory, so that some processes can take it as input

    - **input**  
        - `infiles:files`: The input files  

    - **output**  
        - `outdir:dir`: The output directory  

!!! hint "pFile2Proc"

    - **description**  
        Convert a file to a proc so it can be used as dependent

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output file  

!!! hint "pStr2File"

    - **description**  
        Save string to a file.

    - **input**  
        - `in:var`: The input string.  

    - **output**  
        - `outfile:file`: The output file.  

!!! hint "pHead"

    - **description**  
        Get the top N lines from a file

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `n`: Top n lines. You may use '-n' to skip last n lines.  

!!! hint "pTail"

    - **description**  
        Get the bottom N lines from a file

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `n`: Bottom n lines. You may use '+n' to skip first n lines.  

!!! hint "pPrepend"

    - **description**  
        Prepend a string to a file

    - **input**  
        - `in:var`: The input string.  
        - `infile:file`: The input file.  

    - **output**  
        - `outfile:file`: The output file.  

!!! hint "pAddHeader"

    - **description**  
        Add the header of 1st file to 2nd file.

    - **input**  
        - `infile1:file`: The first file containing the header.  
        - `infile2:file`: The second file with the body.  

    - **output**  
        - `outfile:file`: The output file with the header from 1st input file, body from 2nd file.  

    - **args**  
        - `n`: The number of header lines.  

!!! hint "pMergeFiles"

    - **description**  
        Merge files in the input directory

    - **input**  
        - `indir:file`: The input directory  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `inopts`: The options for input file.  
        	- defaults: skip: 0, comment: #, delimit '\\t'
        - `outopts`: The options for output file. Defaults:  
        	- head: False (not output head line)
        	- headPrefix: `#` (The prefix for head line)
        	- headDelimit: `\\t` (The delimit for head line)
        	- headTransform: `None` (The callback for head line)
        	- delimit: `\\t` (The delimit for output line)

!!! hint "pSplitRows"

    - **description**  
        Split a file by rows, specially usefull to split a job into multithreads/multiprocesses.

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outdir:dir`: The output directory including the split files  

    - **args**  
        - `skip`: The skip first n lines. Default: `0`  
        - `cnames`: The column names. If True, the column names will be added to each split file. Default: `True`  
        - `n`: Number of files to split. Default: `8`  
## eqtl

!!! hint "pMatrixeQTL"

    - **description**  
        Call eQTLs using Matrix eQTL

    - **input**  
        - `snpfile:file`: The genotype file, rows are snps and columns are samples  
        - `expfile:file`: The expression file, rows are genes  
        - `covfile:file`: The covariant file, rows are covariants  

    - **output**  
        - `outfile:file`: The matrix eqtl output file  

    - **args**  
        - `model`: The model to use, either modelLINEAR(default) or modelANOVA  
        - `pval` : The pvalue cutoff (if `cisopts.dist` > 0, will be used as pval for trans-eQTL)  
        - `fdr`  : Calculate FDR or not (default: True)  
        - `cisopts`: Options for calling cis-, trans-eQTL  
        	- `snppos` : The snp position file (columns are: snp, chr, pos)
        	- `genepos`: The gene position file (columns are: gene, chr, start, end)
        	- `dist`   : The distance to define cis-eQTL. (default: 0 (don't do cis-, trans- calling)
        	- `cispv`  : The pvalue cutoff for cis-eQTL (`pval` will not work)

    - **requires**  
        [`Matrix-eQTL (R)`](http://www.bios.unc.edu/research/genomic_software/Matrix_eQTL/)		
## fastx

!!! hint "pFastq2Expr"

    - **description**  
        Use Kallisto to get gene expression from pair-end fastq files.

!!! hint "pFastqSim"

    - **description**  
        Simulate reads

    - **input**  
        - `seed`: The seed to generate simulation file  
        	- None: use current timestamp.

    - **output**  
        - `fq1:file`: The first pair read file  
        - `fq2:file`: The second pair read file  

    - **args**  
        - `tool`: The tool used for simulation. Default: wgsim (dwgsim)  
        - `len1`: The length of first pair read. Default: 100  
        - `len2`: The length of second pair read. Default: 100  
        - `num`: The number of read PAIRs. Default: 1000000  
        - `gz`: Whether generate gzipped read file. Default: True  
        - `wgsim`: The path of wgsim. Default: wgsim  
        - `dwgsim`: The path of wgsim. Default: dwgsim  
        - `ref`: The reference genome. Required  
        - `params`: Other params for `tool`. Default: ""  

    - **requires**  
        [`wgsim`](https://github.com/lh3/wgsim)

!!! hint "pFastQC"

    - **description**  
        QC report for fastq file

    - **input**  
        - `fq:file`: The fastq file (also fine with gzipped)  

    - **output**  
        - `outdir:dir`: The output direcotry  

    - **args**  
        - `tool`: The tool used for simulation. Default: fastqc  
        - `fastqc`: The path of fastqc. Default: fastqc  
        - `nthread`: Number of threads to use. Default: 1  
        - `params`: Other params for `tool`. Default: ""  

    - **requires**  
        [`fastqc`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)

!!! hint "pFastMC"

    - **description**  
        Multi-QC based on pFastQC

    - **input**  
        - `qcdir:file`: The direcotry containing QC files  

    - **output**  
        - `outdir:dir`: The output direcotry  

    - **args**  
        - `tool`: The tool used for simulation. Default: multiqc  
        - `multiqc`: The path of fastqc. Default: multiqc  
        - `params`: Other params for `tool`. Default: ""  

    - **requires**  
        [`multiqc`](http://multiqc.info/)

!!! hint "pFastqTrim"

    - **description**  
        Trim pair-end FASTQ reads

    - **input**  
        - `fq1:file`: The input fastq file  
        - `fq2:file`: The input fastq file  

    - **output**  
        - `outfq1:file`: The trimmed fastq file  
        - `outfq2:file`: The trimmed fastq file  

    - **args**  
        - `tool`        : The tools used for trimming. Default: trimmomatic (cutadapt|skewer)  
        - `cutadapt`    : The path of seqtk. Default: cutadapt  
        - `skewer`      : The path of fastx toolkit trimmer. Default: skewer  
        - `trimmomatic` : The path of trimmomatic. Default: trimmomatic  
        - `params`      : Other params for `tool`. Default: ""  
        - `nthread`     : Number of threads to be used. Default: 1  
        - Not for cutadapt
        - `gz`          : Whether gzip output files. Default: True  
        - `mem`         : The memory to be used. Default: 4G  
        - Only for trimmomatic
        - `minlen`      : Discard trimmed reads that are shorter than `minlen`. Default: 18  
        - For trimmomatic, the number will be `minlen`*2 for MINLEN, as it filters before trimming
        - `minq`        : Minimal mean qulity for 4-base window or leading/tailing reads. Default: 3  
        - `cut5`        : Remove the 5'end reads if they are below qulity. Default: 3  
        - `cut3`        : Remove the 3'end reads if they are below qulity. Default: 3  
        - Not for skewer
        - `adapter1`    : The adapter for sequence. Default: AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC  
        - `adapter2`    : The adapter for pair-end sequence. Default: AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTA  

    - **requires**  
        [`cutadapt`](http://cutadapt.readthedocs.io/en/stable/guide.html)
        [`skewer`](https://github.com/relipmoc/skewer)
        [`trimmomatic`](https://github.com/timflutre/trimmomatic)

!!! hint "pFastqSETrim"

    - **description**  
        Trim single-end FASTQ reads

    - **input**  
        - `fq:file`: The input fastq file  

    - **output**  
        - `outfq:file`: The trimmed fastq file  

    - **args**  
        - `tool`        : The tools used for trimming. Default: trimmomatic (cutadapt|skewer)  
        - `cutadapt`    : The path of seqtk. Default: cutadapt  
        - `skewer`      : The path of fastx toolkit trimmer. Default: skewer  
        - `trimmomatic` : The path of trimmomatic. Default: trimmomatic  
        - `params`      : Other params for `tool`. Default: ""  
        - `nthread`     : Number of threads to be used. Default: 1  
        - Not for cutadapt
        - `gz`          : Whether gzip output files. Default: True  
        - `mem`         : The memory to be used. Default: 4G  
        - Only for trimmomatic
        - `minlen`      : Discard trimmed reads that are shorter than `minlen`. Default: 18  
        - For trimmomatic, the number will be `minlen`*2 for MINLEN, as it filters before trimming
        - `minq`        : Minimal mean qulity for 4-base window or leading/tailing reads. Default: 3  
        - `cut5`        : Remove the 5'end reads if they are below qulity. Default: 3  
        - `cut3`        : Remove the 3'end reads if they are below qulity. Default: 3  
        - Not for skewer
        - `adapter`     : The adapter for sequence. Default: AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC  

    - **requires**  
        [`cutadapt`](http://cutadapt.readthedocs.io/en/stable/guide.html)
        [`skewer`](https://github.com/relipmoc/skewer)
        [`trimmomatic`](https://github.com/timflutre/trimmomatic)

!!! hint "pFastqSE2Sam"

    - **description**  
        Cleaned paired fastq (.fq, .fq.gz, .fastq, .fastq.gz file to mapped sam/bam file

    - **args**  
        - `tool`: The tool used for alignment. Default: bwa (bowtie2|ngm)  
        - `bwa`: Path of bwa, default: bwa  
        - `ngm`: Path of ngm, default: ngm  
        - `bowtie2`: Path of bowtie2, default: bowtie2  
        - `rg`: The read group. Default: {'id': '', 'pl': 'Illumina', 'pu': 'unit1', 'lb': 'lib1', 'sm': ''}  
        - `id` will be parsed from filename with "_LX_" in it if not given
        - `sm` will be parsed from filename
        - `ref`: Path of reference file  
        - `params`: Other params for tool, default: ''  

!!! hint "pFastq2Sam"

    - **description**  
        Cleaned paired fastq (.fq, .fq.gz, .fastq, .fastq.gz file to mapped sam/bam file

    - **args**  
        - `tool`   : The tool used for alignment. Default: bwa (bowtie2, ngm, star)  
        - `bwa`    : Path of bwa, default: bwa  
        - `ngm`    : Path of ngm, default: ngm  
        - `star`   : Path of ngm, default: STAR  
        - `bowtie2`: Path of bowtie2, default: bowtie2  
        - `rg`: The read group. Default: {'id': '', 'pl': 'Illumina', 'pu': 'unit1', 'lb': 'lib1', 'sm': ''}  
        - `id` will be parsed from filename with "_LX_" in it if not given
        - `sm` will be parsed from filename
        - `ref`    : Path of reference file  
        - `refgene`: The GTF file for STAR to build index. It's not neccessary if index is already been built. Default: ''  
        - `params` : Other params for tool, default: ''  
## gatk

!!! hint "pRealignerTargetCreator"

    - **description**  
        The local realignment process is designed to consume one or more BAM files and to locally realign reads such that the number of mismatching bases is minimized across all the reads. In general, a large percent of regions requiring local realignment are due to the presence of an insertion or deletion (indels) in the individual's genome with respect to the reference genome. Such alignment artifacts result in many bases mismatching the reference near the misalignment, which are easily mistaken as SNPs. Moreover, since read mapping algorithms operate on each read independently, it is impossible to place reads on the reference genome such that mismatches are minimized across all reads. Consequently, even when some reads are correctly mapped with indels, reads covering the indel near just the start or end of the read are often incorrectly mapped with respect the true indel, also requiring realignment. Local realignment serves to transform regions with misalignments due to indels into clean reads containing a consensus indel suitable for standard variant discovery approaches.
        Note that indel realignment is no longer necessary for variant discovery if you plan to use a variant caller that performs a haplotype assembly step, such as HaplotypeCaller or MuTect2. However it is still required when using legacy callers such as UnifiedGenotyper or the original MuTect. There are 2 steps to the realignment process:
        - Determining (small) suspicious intervals which are likely in need of realignment (RealignerTargetCreator)
        - Running the realigner over those intervals (see the IndelRealigner tool)
        For more details, see [the indel realignment method documentation](http://www.broadinstitute.org/gatk/guide/article?id=38).

    - **input**  
        - `bamfile:file`: The aligned bam file  
        - `reffile`: The reference file  

    - **brings**  
        - `bamfile`: `{{bamfile | bn}}.bai` The index file of input bam file  
        - `reffile#fai`: `{{reffile | bn}}.fai`  
        - `reffile#dict`: `{{reffile | bn}}.dict`  

    - **output**  
        - `outfile:file`: A list of target intervals to pass to the IndelRealigner.  

    - **args**  
        - `gatk`: The gatk executable, default: "gatk"  
        - `picard`: The picard executable, default: "picard"  
        - `params`: Other parameters for RealignerTargetCreator, default: ""  
        - `samtools`: The samtools executable, default: "samtools"  
        - `tmpdir`: The tmpdir to use. Default: /tmp  
        - `javamem`: The memory for java vm. Default: "-Xms1g -Xmx8g"  

    - **requires**  
        [GATK](https://software.broadinstitute.org/gatk)
        [samtools](http://www.htslib.org/) if `reffile` is not indexed or `bamfile` is not indexed.
        [picard](https://broadinstitute.github.io/picard/) if `reffile` is not dicted.

!!! hint "pIndelRealigner"

    - **description**  
        The local realignment process is designed to consume one or more BAM files and to locally realign reads such that the number of mismatching bases is minimized across all the reads. In general, a large percent of regions requiring local realignment are due to the presence of an insertion or deletion (indels) in the individual's genome with respect to the reference genome. Such alignment artifacts result in many bases mismatching the reference near the misalignment, which are easily mistaken as SNPs. Moreover, since read mapping algorithms operate on each read independently, it is impossible to place reads on the reference genome such at mismatches are minimized across all reads. Consequently, even when some reads are correctly mapped with indels, reads covering the indel near just the start or end of the read are often incorrectly mapped with respect the true indel, also requiring realignment. Local realignment serves to transform regions with misalignments due to indels into clean reads containing a consensus indel suitable for standard variant discovery approaches.
        Note that indel realignment is no longer necessary for variant discovery if you plan to use a variant caller that performs a haplotype assembly step, such as HaplotypeCaller or MuTect2. However it is still required when using legacy callers such as UnifiedGenotyper or the original MuTect.
        There are 2 steps to the realignment process:
        - Determining (small) suspicious intervals which are likely in need of realignment (see the RealignerTargetCreator tool)
        - Running the realigner over those intervals (IndelRealigner)
        For more details, see [the indel realignment method documentation](http://www.broadinstitute.org/gatk/guide/article?id=38).

    - **input**  
        - `bamfile:file`: The aligned bam file  
        - `intfile:file`: Intervals file output from RealignerTargetCreator  
        - `reffile:file`: The reference file  

    - **brings**  
        - `bamfile`: `{{bamfile | bn}}.bai` The index file of input bam file  
        - `reffile#fai`: `{{reffile | bn}}.fai`  
        - `reffile#dict`: `{{reffile | bn}}.dict`  

    - **output**  
        - `outfile:file`: A realigned version of input BAM file.  

    - **args**  
        - `gatk`: The gatk executable, default: "gatk"  
        - `picard`: The picard executable, default: "picard"  
        - `params`: Other parameters for IndelRealigner, default: ""  
        - `samtools`: The samtools executable, default: samtools  
        - `tmpdir`: The tmpdir to use. Default: /tmp  
        - `javamem`: The memory for java vm. Default: "-Xms1g -Xmx8g"  

    - **requires**  
        [GATK](https://software.broadinstitute.org/gatk)
        [samtools](http://www.htslib.org/) if `reffile` is not indexed or `bamfile` is not indexed.
        [picard](https://broadinstitute.github.io/picard/) if `reffile` is not dicted.

!!! hint "pBaseRecalibrator"

    - **description**  
        Variant calling algorithms rely heavily on the quality scores assigned to the individual base calls in each sequence read. These scores are per-base estimates of error emitted by the sequencing machines. Unfortunately the scores produced by the machines are subject to various sources of systematic technical error, leading to over- or under-estimated base quality scores in the data. Base quality score recalibration (BQSR) is a process in which we apply machine learning to model these errors empirically and adjust the quality scores accordingly. This allows us to get more accurate base qualities, which in turn improves the accuracy of our variant calls. The base recalibration process involves two key steps: first the program builds a model of covariation based on the data and a set of known variants (which you can bootstrap if there is none available for your organism), then it adjusts the base quality scores in the data based on the model. There is an optional but highly recommended step that involves building a second model and generating before/after plots to visualize the effects of the recalibration process. This is useful for quality control purposes. This tool performs the first step described above: it builds the model of covariation and produces the recalibration table. It operates only at sites that are not in dbSNP; we assume that all reference mismatches we see are therefore errors and indicative of poor base quality. This tool generates tables based on various user-specified covariates (such as read group, reported quality score, cycle, and context). Assuming we are working with a large amount of data, we can then calculate an empirical probability of error given the particular covariates seen at this site, where p(error) = num mismatches / num observations. The output file is a table (of the several covariate values, number of observations, number of mismatches, empirical quality score).

    - **input**  
        - `bamfile:file`: A BAM file containing data that needs to be recalibrated.  
        - `reffile:file`: The reference file  

    - **brings**  
        - `bamfile`: `{{bamfile | bn}}.bai` The index file of input bam file  
        - `reffile#fai`: `{{reffile | bn}}.fai`  
        - `reffile#dict`: `{{reffile | bn}}.dict`  

    - **output**  
        - `outfile:file`: A GATKReport file with many tables:  
        	- The list of arguments
        	- The quantized qualities table
        	- The recalibration table by read group
        	- The recalibration table by quality score
        	- The recalibration table for all the optional covariates

    - **args**  
        - `gatk`: The gatk executable, default: "gatk"  
        - `params`: Other parameters for BaseRecalibrator, default: ""  
        - `knownSites`: The known polymorphic sites to mask out, required  
        - `samtools`: The samtools executable, default: samtools  
        - `picard`: The picard executable, default: "picard"  
        - `tmpdir`: The tmpdir to use. Default: /tmp  
        - `javamem`: The memory for java vm. Default: "-Xms1g -Xmx8g"  

    - **requires**  
        [GATK](https://software.broadinstitute.org/gatk)
        [samtools](http://www.htslib.org/) if `reffile` is not indexed or `bamfile` is not indexed.
        [picard](https://broadinstitute.github.io/picard/) if `reffile` is not dicted.

!!! hint "pPrintReads"

    - **description**  
        PrintReads is a generic utility tool for manipulating sequencing data in SAM/BAM format. It can dynamically merge the contents of multiple input BAM files, resulting in merged output sorted in coordinate order. It can also optionally filter reads based on various read properties such as read group tags using the `--read_filter/-rf` command line argument (see documentation on read filters for more information).
        Note that when PrintReads is used as part of the Base Quality Score Recalibration workflow, it takes the `--BQSR` engine argument, which is listed under Inherited Arguments > CommandLineGATK below.

    - **input**  
        - `bamfile:file`: A BAM file.  
        - `recaltable:file`: The GATKReport file  
        - `reffile:file`: The reference file  

    - **brings**  
        - `bamfile`: `{{bamfile | bn}}.bai` The index file of input bam file  
        - `reffile#fai`: `{{reffile | bn}}.fai`  
        - `reffile#dict`: `{{reffile | bn}}.dict`  

    - **output**  
        - `outfile:file`: A single processed bam file.  

    - **args**  
        - `gatk`: The gatk executable, default: "gatk"  
        - `params`: Other parameters for PrintReads, default: ""  
        - `samtools`: The samtools executable, default: samtools  
        - `picard`: The picard executable, default: "picard"  
        - `tmpdir`: The tmpdir to use. Default: /tmp  
        - `javamem`: The memory for java vm. Default: "-Xms1g -Xmx8g"  

    - **requires**  
        [GATK](https://software.broadinstitute.org/gatk)
        [samtools](http://www.htslib.org/) if `reffile` is not indexed or `infile` is not indexed.
        [picard](https://broadinstitute.github.io/picard/) if `reffile` is not dicted.

!!! hint "pHaplotypeCaller"

    - **description**  
        PrintReads is a generic utility tool for manipulating sequencing data in SAM/BAM format. It can dynamically merge the contents of multiple input BAM files, resulting in merged output sorted in coordinate order. It can also optionally filter reads based on various read properties such as read group tags using the `--read_filter/-rf` command line argument (see documentation on read filters for more information).
        Note that when PrintReads is used as part of the Base Quality Score Recalibration workflow, it takes the `--BQSR` engine argument, which is listed under Inherited Arguments > CommandLineGATK below.

    - **input**  
        - `bamfile:file`: A BAM file.  
        - `reffile:file`: The reference file  

    - **brings**  
        - `bamfile`: `{{bamfile | bn}}.bai` The index file of input bam file  
        - `reffile#fai`: `{{reffile | bn}}.fai`  
        - `reffile#dict`: `{{reffile | bn}}.dict`  

    - **output**  
        - `outfile:file`: Either a VCF or gVCF file with raw, unfiltered SNP and indel calls.  

    - **args**  
        - `gatk`    : The gatk executable, default: "gatk"  
        - `params`  : Other parameters for HaplotypeCaller, default: ""  
        - `samtools`: The samtools executable, default: samtools  
        - `picard`: The picard executable, default: "picard"  
        - `tmpdir`: The tmpdir to use. Default: /tmp  
        - `javamem`: The memory for java vm. Default: "-Xms1g -Xmx8g"  
        - `nthread`: Corresponding to -nct option  

    - **requires**  
        [GATK](https://software.broadinstitute.org/gatk)
        [samtools](http://www.htslib.org/) if `reffile` is not indexed or `infile` is not indexed.
        [picard](https://broadinstitute.github.io/picard/) if `reffile` is not dicted.

!!! hint "pSelectVariants"

    - **description**  
        Often, a VCF containing many samples and/or variants will need to be subset in order to facilitate certain analyses (e.g. comparing and contrasting cases vs. controls; extracting variant or non-variant loci that meet certain requirements, displaying just a few samples in a browser like IGV, etc.). SelectVariants can be used for this purpose.
        There are many different options for selecting subsets of variants from a larger callset:
        - Extract one or more samples from a callset based on either a complete sample name or a pattern match.
        - Specify criteria for inclusion that place thresholds on annotation values, e.g. "DP > 1000" (depth of coverage greater than 1000x), "AF < 0.25" (sites with allele frequency less than 0.25). These - criteria are written as "JEXL expressions", which are documented in the article about using JEXL expressions.
        - Provide concordance or discordance tracks in order to include or exclude variants that are also present in other given callsets.
        - Select variants based on criteria like their type (e.g. INDELs only), evidence of mendelian violation, filtering status, allelicity, and so on.
        There are also several options for recording the original values of certain annotations that are recalculated when a subsetting the new callset, trimming alleles, and so on.

    - **input**  
        - `vcffile:file`: A variant call set from which to select a subset.  
        - `reffile:file`: The reference file  

    - **brings**  
        - `reffile#fai`: `{{reffile | bn}}.fai`  
        - `reffile#dict`: `{{reffile | bn}}.dict`  

    - **output**  
        - `outfile:file`: A new VCF file containing the selected subset of variants.  

    - **args**  
        - `gatk`: The gatk executable, default: "gatk"  
        - `params`: Other parameters for SelectVariants, default: ""  
        - `samtools`: The samtools executable, default: samtools  
        - `picard`: The picard executable, default: "picard"  
        - `tmpdir`: The tmpdir to use. Default: /tmp  
        - `javamem`: The memory for java vm. Default: "-Xms1g -Xmx8g"  

    - **requires**  
        [GATK](https://software.broadinstitute.org/gatk)
        [samtools](http://www.htslib.org/) if `reffile` is not indexed or `infile` is not indexed.
        [picard](https://broadinstitute.github.io/picard/) if `reffile` is not dicted.

!!! hint "pVariantFiltration"

    - **description**  
        This tool is designed for hard-filtering variant calls based on certain criteria. Records are hard-filtered by changing the value in the FILTER field to something other than PASS. Filtered records will be preserved in the output unless their removal is requested in the command line.
        The most common way of specifying filtering criteria is by using JEXL queries. See the article on JEXL expressions in the documentation Guide for detailed information and examples.

    - **input**  
        - `vcffile:file`: A variant call set from which to select a subset.  
        - `reffile:file`: The reference file  

    - **brings**  
        - `reffile#fai`: `{{reffile | bn}}.fai`  
        - `reffile#dict`: `{{reffile | bn}}.dict`  

    - **output**  
        - `outfile:file`: A filtered VCF.  

    - **args**  
        - `gatk`: The gatk executable, default: "gatk -T VariantFiltration"  
        - `params`: Other parameters for VariantFiltration, default: ""  
        - `samtools`: The samtools executable, default: samtools  
        - `picard`: The picard executable, default: "picard"  
        - `tmpdir`: The tmpdir to use. Default: /tmp  
        - `javamem`: The memory for java vm. Default: "-Xms1g -Xmx8g"  

    - **requires**  
        [GATK](https://software.broadinstitute.org/gatk)
        [samtools](http://www.htslib.org/) if `reffile` is not indexed or `infile` is not indexed.
        [picard](https://broadinstitute.github.io/picard/) if `reffile` is not dicted.

!!! hint "pMuTect2"

    - **description**  
        MuTect2 is a somatic SNP and indel caller that combines the DREAM challenge-winning somatic genotyping engine of the original MuTect ([Cibulskis et al., 2013](http://www.nature.com/nbt/journal/v31/n3/full/nbt.2514.html)) with the assembly-based machinery of HaplotypeCaller. The basic operation of MuTect2 proceeds similarly to that of the HaplotypeCaller.
        NOTE: only Tumor/Normal variant calling implemented in bioprocs

    - **input**  
        - `tumor:file`: the tumor bam file  
        - `normal:file`: the normal bam file  
        - `reffile:file`: the reference file  

    - **brings**  
        - `tumor`: `{{tumor | bn}}.bai` the index file of tumor  
        - `normal`: `{{normal | bn}}.bai` the index file of normal  
        - `reffile#fai`: `{{reffile | bn}}.fai`  
        - `reffile#dict`: `{{reffile | bn}}.dict`  

    - **output**  
        - `outfile:file`: The vcf file containing somatic mutations  

    - **args**  
        - `gatk`: The gatk executable, default: "gatk"  
        - `samtools`: The samtools executable, default: samtools  
        - `params`: Other parameters for MuTect2, default: ""  
        - `picard`: The picard executable, default: "picard"  
        - `tmpdir`: The tmpdir to use. Default: /tmp  
        - `javamem`: The memory for java vm. Default: "-Xms1g -Xmx8g"  

    - **requires**  
        [GATK](https://software.broadinstitute.org/gatk)
        [samtools](http://www.htslib.org/) if index files of input files are not found
        [picard](https://broadinstitute.github.io/picard/) if `reffile` is not dicted.

!!! hint "pMuTect2Interval"

    - **description**  
        Use interval file model of MuTect2

    - **input**  
        - `tumor:file`: the tumor bam file  
        - `normal:file`: the normal bam file  
        - `reffile:file`: the reference file  

    - **brings**  
        - `tumor`: `{{tumor | bn}}.bai` the index file of tumor  
        - `normal`: `{{normal | bn}}.bai` the index file of normal  
        - `reffile#fai`: `{{reffile | bn}}.fai`  
        - `reffile#dict`: `{{reffile | bn}}.dict`  

    - **output**  
        - `outfile:file`: The vcf file containing somatic mutations  

    - **args**  
        - `gatk`: The gatk executable, default: "gatk"  
        - `samtools`: The samtools executable, default: samtools  
        - `params`: Other parameters for MuTect2, default: ""  
        - `picard`: The picard executable, default: "picard"  
        - `tmpdir`: The tmpdir to use. Default: /tmp  
        - `javamem`: The memory for java vm. Default: "-Xms1g -Xmx8g"  

    - **requires**  
        [GATK](https://software.broadinstitute.org/gatk)
        [samtools](http://www.htslib.org/) if index files of input files are not found
        [picard](https://broadinstitute.github.io/picard/) if `reffile` is not dicted.
## gene

!!! hint "pGenePromoters"

    - **description**  
        Alias of `seq.pPromoters`.

!!! hint "pGeneNameNorm"

    - **description**  
        Normalize gene names using MyGeneinfo.

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `notfound`: What if a symbol is not found. Default: ignore  
        	- skip  : skip the record(don't write it to output file)
        	- ignore: use the original name;
        	- error : report error
        - `col`: the column index containing the gene names  
        - `from`: the original format. Default: 'symbol, alias'  
        - `to`: the output gene name format. Default: 'symbol'  
        - `genome`: the genome. Default: 'hg19'  

!!! hint "pGeneTss"

    - **description**  
        Get gene TSS in BEd format.

    - **input**  
        - `infile:file`: The input file containing genes  

    - **output**  
        - `outfile:file`: The output BED file  

    - **args**  
        - `notfound`: What if the gene is not found. Default: skip.  
        	- error: report error
        - `header`: Whether the input file contains header. Default: False  
        - `skip`: Skip N lines of input file. Default: 0  
        	- This has highest priority of header and comment
        - `comment`: The comment line start sign. Default: #  
        - `delimit`: The delimit of input file if it has multiple column. Default: `\\t`  
        - `col`: The column index contains the genes. Default: 0  
        - `frm`: The format of the genes. Default: `symbol, alias`  
        - `tmpdir`: The tmpdir used to store mygene cache files.  
        - `genome`: In which genome to fetch the coordinates. Default: hg19  

!!! hint "pGeneBody"

    - **description**  
        Get gene body region in BED format

    - **input**  
        - `infile:file`: The input file containing genes  

    - **output**  
        - `outfile:file`: The gene body region  

    - **args**  
        - `notfound`: What if a gene is not found when transfer the gene names to gene symbols  
        	- error: report error
        	- skip (default): skip it
        - `inmeta`: The metadata for input file, mainly to indicate where the GENE column is.  
        - `inopts`: Input options for reading input file.  
        	- skip: number of lines to skip. Default: 0
        	- comment: the starting string for comment lines. Default: #
        	- delimit: The delimit for the input file. Default: '\\t'
        frm: The gene name format in the input file. Default: 'symbol, alias'
        tmpdir: The tmpdir to cache the gene name conversion.
        genome: The genome used to do the conversion.
## genomeplot

!!! hint "pInteractionTrack"

    - **description**  
        Gererate genomic interaction track for Gviz

    - **input**  
        - `name`: The name of the track  
        - `infile:file`: The input file.   
        	- See the `type` argument for `makeGenomicInteractionsFromFile` from `GenomicInteractions` r-package
        - `region`: the region, just chromosome!  

    - **output**  
        - `outfile:file`: The dumped track data  

    - **args**  
        - `intype`: Input file type. Default: auto  
        	- Identified by extension
        	- One of "chiapet.tool", "bed12", "bedpe", "hiclib", "homer", "bam", "two.bams".
        - `params`: The display params  

!!! hint "pGeneTrack"

    - **description**  
        Generate gene track using ucsc data source

    - **input**  
        - `name`: The name of the track  

    - **output**  
        - `outfile:file`: The file to save the track  

    - **args**  
        - `genome`: The genome  
        - `params`: use `displayPars(UcscTrack(genome="mm9", chromosome="chrM", track="knownGene"))` to see all available args  

    - **requires**  
        [r-Gviz](https://rdrr.io/bioc/Gviz)

!!! hint "pAnnoTrack"

    - **description**  
        The annotation track of Gviz

    - **input**  
        - `name`: the name of the track  
        - `infile:file`: the file for the track. (wig, bigWig or bedGraph, bam, need to be indexed!)  
        - `chrom`: the chrom  

    - **output**  
        - `outfile:file`: the rds file for the track  

    - **args**  
        - `genome`: The genome  
        - `params`: See `displayPars(DataTrack())` for all available display params  

    - **requires**  
        [r-Gviz](https://rdrr.io/bioc/Gviz/man/DataTrack-class.html)

!!! hint "pDataTrack"

    - **description**  
        The data track of Gviz

    - **input**  
        - `name`: the name of the track  
        - `infile:file`: the file for the track. (wig, bigWig or bedGraph, bam, need to be indexed!)  
        - `chrom`: the chrom  

    - **output**  
        - `outfile:file`: the rds file for the track  

    - **args**  
        - `genome`: The genome  
        - `params`: See `displayPars(DataTrack())` for all available display params  

    - **requires**  
        [r-Gviz](https://rdrr.io/bioc/Gviz/man/DataTrack-class.html)

!!! hint "pUcscTrack"

    - **description**  
        Generate track from ucsc

    - **input**  
        - `name`     : the name of the track  
        - `track`    : the UCSC track  
        - `trackType`: the Gviz track  
        - `region`   : the region  

    - **output**  
        - `outfile:file`: the dumped track  

    - **args**  
        - `params`: use `displayPars(UcscTrack(genome="mm9", chromosome="chrM", track="knownGene"))` to see all available args.  

    - **requires**  
        [r-Gviz](https://rdrr.io/bioc/Gviz)

!!! hint "pGenomePlot"

    - **description**  
        plot the genomic features

    - **input**  
        - `trkfiles:files`: the list of track dumped files  
        - `region`: the region, in format of `chr1:1-1000`  
        - `highlight`: the highlight regions, informat of start1-end1; start2-end2; ...  

    - **output**  
        - `outfile:file`: the figure  

    - **args**  
        - `genome`  : The genome  
        - `showIdeo`: Show ideogram track? Default: True  
        - `showAxis`: Show axis? Default: True  
        - `showGenes`: Show geneTrack? Default: True  
        - `params`: The params  
        	- `genneral`:  General params for plotTracks
        	- `geneTrack`: The params for geneTrack

    - **requires**  
        [r-Gviz](https://rdrr.io/bioc/Gviz)
## gsea

!!! hint "pGMT2Mat"

    - **description**  
        Convert a GMT file to a matrix.
        Rownames of GMT file will be the column names of output matrix.

    - **input**  
        - `infile:file`: The input file in GMT format.  

    - **output**  
        - `outfile:file`: output matrix file  

!!! hint "pExpmat2Gct"

    - **description**  
        Convert expression matrix to GCT file.
        Refer to http://software.broadinstitute.org/cancer/software/genepattern/file-formats-guide#GCT for file format

    - **input**  
        - `expfile:file`: the input expression matrix file. Samples as columns, genes as rows.  

    - **output**  
        - `outfile:file`: the gct file  

!!! hint "pSampleinfo2Cls"

    - **description**  
        Convert sample infomation to cls file.
        Refer to http://software.broadinstitute.org/cancer/software/genepattern/file-formats-guide#CLS for file format
        NOTE that the order of samples must be the same as in GMT file in further analysis.

    - **input**  
        - `sifile:file`: the sample information file.  
        	- Headers are: [Sample, ]Patient, Group, Batch
        	- Rows are samples

    - **output**  
        - `outfile:file`: the cls file  

!!! hint "pSSGSEA"

    - **description**  
        Single sample GSEA
        Refer to http://software.broadinstitute.org/cancer/software/genepattern/file-formats-guide#GCT for GCT file format
        Refer to http://software.broadinstitute.org/cancer/software/genepattern/file-formats-guide#GMT for GMT file format

    - **input**  
        - `gctfile:file`: the expression file  
        - `gmtfile:file`: the gmtfile for gene sets  

    - **output**  
        - `outdir:file`: the output directory  
        - `report.txt`: the enrichment report for each Gene set.
        - `RES_<GeneSet>.png`: the running ES plot for <GeneSet>
        - `normP_<GeneSet>.png`: the norminal P value plot for <GeneSet>

    - **args**  
        - `weightexp`: Exponential weight employed in calculation of enrichment scores. Default: 0.75  
        - `nperm`: Number of permutations. Default: 10000  

!!! hint "pGSEA"

    - **description**  
        GSEA
        Refer to http://software.broadinstitute.org/cancer/software/genepattern/file-formats-guide#GCT for GCT file format
        Refer to http://software.broadinstitute.org/cancer/software/genepattern/file-formats-guide#GMT for GMT file format
        Refer to http://software.broadinstitute.org/cancer/software/genepattern/file-formats-guide#CLS for CLS file format

    - **input**  
        - `gctfile:file`: the expression file  
        - `clsfile:file`: the class file  
        - `gmtfile:file`: the gmtfile for gene sets  

    - **output**  
        - `outdir:file`: the output directory  

    - **args**  
        - `weightexp`: Exponential weight employed in calculation of enrichment scores. Default: 0.75  
        - `nperm`: Number of permutations. Default: 10000  

!!! hint "pEnrichr"

    - **description**  
        Use APIs from http://amp.pharm.mssm.edu/Enrichr/help#api&q=1 to analyze a gene list

    - **input**  
        - `infile:file`: The gene list, each per line  

    - **output**  
        - `outdir:dir`: The output directory, containing the tables and figures.  

    - **args**  
        - `topn`: Top N pathways used to plot. Default: 10  
        - `col`: The columns index containing the genes. Default: 0  
        - `delimit`: The delimit of input file. Default: '\\t'  
        - `dbs`: The databases to do enrichment against. Default: KEGG_2016  
          - A full list can be found here: http://amp.pharm.mssm.edu/Enrichr/#stats
          - Multiple dbs separated by comma (,)
        - `norm`: Normalize the gene list use [python-mygene](https://pypi.python.org/pypi/mygene/3.0.0)  
        - `rmtags`: Remove pathway tags in the plot. Default: True  
          - For example: change "Lysine degradation_Homo sapiens_hsa00310" to "Lysine degradation".
        - `plot`: Whether to plot the result. Default: True  
        - `title`: The title for the plot. Default: "Gene enrichment: {db}"  

    - **requires**  
        [python-mygene](https://pypi.python.org/pypi/mygene/3.0.0) if `args.norm` is `True`

!!! hint "pTargetEnrichr"

    - **description**  
        Use APIs from http://amp.pharm.mssm.edu/Enrichr/help#api&q=1 to analyze a gene list

    - **input**  
        - `infile:file`: The target genes with regulators  
        	- Format:
        	- Header is not required, but may specified in first line starting with `#`
        	- If only 3 columns are there, the 3rd column is anyway the relation!
        	- If only 4 columns are there, 3rd is target status, 4th is relation!
        	  ```
        	  #Regulator	Target	Regulator status	Target status	Relation
        	  has-mir-22	Gene	+	+	+
        	  ```

    - **output**  
        - `outdir:dir`: The output directory, containing the tables and figures.  

    - **args**  
        - `dbs`       : The databases to do enrichment against. Default: KEGG_2016  
          - A full list can be found here: http://amp.pharm.mssm.edu/Enrichr/#stats
          - Multiple dbs separated by comma (,)
        - `rmtags`    : Remove pathway tags in the plot. Default: True  
          - For example: change "Lysine degradation_Homo sapiens_hsa00310" to "Lysine degradation".
        - `enrplot`   : Whether to plot the result. Default: True  
        - `enrn`      : Top N pathways used to plot. Default: 10  
        - `netplot`   : Whether to plot the network. Default: True  
        - `netn`      : Top N pathways used to plot the network. Default: 5  
        	- Must <= `enrn`. If `netn` >= `enrn`, `netn` = `enrn`
        - `title`     : The title for the plot. Default: "Gene enrichment: {db}"  

    - **requires**  
        [`python-mygene`](https://pypi.python.org/pypi/mygene/3.0.0)
        [`graphviz`](https://pypi.python.org/pypi/graphviz)
## hic
## marray

!!! hint "pCELdir2Matrix"

    - **description**  
        Convert CEL files to expression matrix
        File names will be used as sample names (colnames)

    - **input**  
        - `indir:file`: the directory containing the CEL files, could be gzipped  
        	- If you have files, then use `pFiles2Dir` first

    - **output**  
        - `outfile:file`: the expression matrix file  
        - `outdir:dir`: the directory containing expr file and plots  

    - **args**  
        - `pattern`  : The pattern to filter files. Default `'*'`  
        - `norm`     : The normalization method. Default: rma (mas5)  
        - `gfile`    : The group file. Default: ''  
        - `cdffile`  : The cdffile. Default: ''  
        - `annofile` : The annotation file. Default: ''  
        - `hmrows`   : How many rows to be used to plot heatmap  
        - `plot`: Whether to plot  
        	- `boxplot`   : Whether to plot a boxplot. Default: False
        	- `heatmap`   : Whether to plot a heatmap. Default: False
        	- `histogram` : Whether to plot a histgram. Default: False
        - `devpars`    : Parameters for png. Default: `{'res': 300, 'width': 2000, 'height': 2000}`  
        - `ggs`: The ggplot parameters  
        	- `boxplot`  : The ggplot parameters for boxplot. Default: `Box(ylab = {0: "Log2 Intensity"})`
        	- `heatmap`  : The ggplot parameters for heatmap. Default: `Box(theme = {'axis.text.y': 'r:element_blank()'})`
        	- `histogram`: The ggplot parameters for histgram. Default: `Box(labs = {'x': "Log2 Intensity", "y": "Density"})`
## misc

!!! hint "pGEP70"

    - **description**  
        Calculate GEP70 scores for multiple mylenoma 70-gene-signatures
## pca

!!! hint "pPCA"

    - **description**  
        Perform PCA analysis

    - **input**  
        - `infile:file`: The matrix to do the analysis  
        - Note that rows are samples, columns are features, if not, use `args.transpose = True`

    - **output**  
        - `outfile:file`: The output coordinate file  
        - Columns are PCs, rows are samples

    - **args**  
        - `transpose`: Whether to transpose the input matrix from infile. Default: False  
        - `rownames`: The `row.names` argument for `read.table`, default: 1  
        - `header`: The `header` argument for `read.table` to read the input file, default: True.  
        - `screeplot`: Whether to generate the screeplot or not. Default: True  
        - `sp_ncp`: Number of components in screeplot. Default: 0 (auto detect)  
        - if total # components (tcp) < 20: use all
        - else if tcp > 20, use 20
        - `varplot`: Whether to generate the variable plot or not. Default: False  
        - `biplot`: Whether to generate the variable plot or not. Default: True  

    - **requires**  
        [`r-factoextra`](https://cran.r-project.org/web/packages/factoextra/index.html) for plots

!!! hint "pSelectPCs"

    - **description**  
        Select a subset of PCs from pPCA results

    - **input**  
        - `indir:file`: The directory generated from pPCA  

    - **output**  
        - `outfile:file`: The file containing selected PCs  

    - **args**  
        - `n`: The number of PCs to select. Default: 0.9  
        - If it is < 1, used as the % variation explained from stdev.txt
## picard

!!! hint "pMarkDuplicates"

    - **description**  
        Identifies duplicate reads.
        
        This tool locates and tags duplicate reads in a BAM or SAM file, where duplicate reads are defined as originating from a single fragment of DNA. Duplicates can arise during sample preparation e.g. library construction using PCR. See also EstimateLibraryComplexity for additional notes on PCR duplication artifacts. Duplicate reads can also result from a single amplification cluster, incorrectly detected as multiple clusters by the optical sensor of the sequencing instrument. These duplication artifacts are referred to as optical duplicates.
        
        The MarkDuplicates tool works by comparing sequences in the 5 prime positions of both reads and read-pairs in a SAM/BAM file. An BARCODE_TAG option is available to facilitate duplicate marking using molecular barcodes. After duplicate reads are collected, the tool differentiates the primary and duplicate reads using an algorithm that ranks reads by the sums of their base-quality scores (default method).
        
        The tool's main output is a new SAM or BAM file, in which duplicates have been identified in the SAM flags field for each read. Duplicates are marked with the hexadecimal value of 0x0400, which corresponds to a decimal value of 1024. If you are not familiar with this type of annotation, please see the following [blog post](https://www.broadinstitute.org/gatk/blog?id=7019) for additional information.
        
        Although the bitwise flag annotation indicates whether a read was marked as a duplicate, it does not identify the type of duplicate. To do this, a new tag called the duplicate type (DT) tag was recently added as an optional output in the 'optional field' section of a SAM/BAM file. Invoking the TAGGING_POLICY option, you can instruct the program to mark all the duplicates (All), only the optical duplicates (OpticalOnly), or no duplicates (DontTag). The records within the output of a SAM/BAM file will have values for the 'DT' tag (depending on the invoked TAGGING_POLICY), as either library/PCR-generated duplicates (LB), or sequencing-platform artifact duplicates (SQ). This tool uses the READ_NAME_REGEX and the OPTICAL_DUPLICATE_PIXEL_DISTANCE options as the primary methods to identify and differentiate duplicate types. Set READ_NAME_REGEX to null to skip optical duplicate detection, e.g. for RNA-seq or other data where duplicate sets are extremely large and estimating library complexity is not an aim. Note that without optical duplicate counts, library size estimation will be inaccurate.
        
        MarkDuplicates also produces a metrics file indicating the numbers of duplicates for both single- and paired-end reads.
        
        The program can take either coordinate-sorted or query-sorted inputs, however the behavior is slightly different. When the input is coordinate-sorted, unmapped mates of mapped records and supplementary/secondary alignments are not marked as duplicates. However, when the input is query-sorted (actually query-grouped), then unmapped mates and secondary/supplementary reads are not excluded from the duplication test and can be marked as duplicate reads.
        
        If desired, duplicates can be removed using the REMOVE_DUPLICATE and REMOVE_SEQUENCING_DUPLICATES options.

    - **input**  
        - `infile:file`: The bam file   

    - **output**  
        - `outfile:file`: The marked bam file  

    - **args**  
        - `picard`: The picard executable, default: "picard"  
        - `params`: Other parameters for picard MarkDuplicates, default: ""  
        - `tmpdir`: The tmpdir to use. Default: /tmp  

    - **requires**  
        [picard](https://broadinstitute.github.io/picard/)

!!! hint "pAddOrReplaceReadGroups"

    - **description**  
        Replace read groups in a BAM file.This tool enables the user to replace all read groups in the INPUT file with a single new read group and assign all reads to this read group in the OUTPUT BAM file.
        
        For more information about read groups, see the [GATK Dictionary entry](https://www.broadinstitute.org/gatk/guide/article?id=6472). 
        
        This tool accepts INPUT BAM and SAM files or URLs from the Global Alliance for Genomics and Health (GA4GH) (see http://ga4gh.org/#/documentation).

    - **input**  
        - `infile:file`: The bam file  
        - `rg`: The read group information. For example:  
        	- "RGID=4 RGLB=lib1 RGPL=illumina RGPU=unit1 RGSM=20"

    - **output**  
        - `outfile:file`: The bam file with read group added  

    - **args**  
        - `picard`: The picard executable, default: "picard "  
        - `params`: Other parameters for picard AddOrReplaceReadGroups, default: ""  

    - **requires**  
        [picard](https://broadinstitute.github.io/picard/)

!!! hint "pCreateSequenceDictionary"

    - **description**  
        Creates a sequence dictionary for a reference sequence. This tool creates a sequence dictionary file (with ".dict" extension) from a reference sequence provided in FASTA format, which is required by many processing and analysis tools. The output file contains a header but no SAMRecords, and the header contains only sequence records.
        
        The reference sequence can be gzipped (both .fasta and .fasta.gz are supported).

    - **input**  
        - `infile:file`: The fasta file   

    - **output**  
        - `outfile:file`: The same fasta file, but with dict file created  

    - **args**  
        - `picard`: The picard executable, default: "picard"  
        - `params`: Other parameters for picard CreateSequenceDictionary, default: ""  

    - **requires**  
        [picard](https://broadinstitute.github.io/picard/)

!!! hint "pCollectWgsMetrics"

    - **description**  
        Collect metrics about coverage and performance of whole genome sequencing (WGS) experiments.
        
        This tool collects metrics about the fractions of reads that pass base- and mapping-quality filters as well as coverage (read-depth) levels for WGS analyses. Both minimum base- and mapping-quality values as well as the maximum read depths (coverage cap) are user defined.
        
        Note: Metrics labeled as percentages are actually expressed as fractions!

    - **input**  
        - `infile:file`: The bam file   

    - **output**  
        - `outfile:file`: The metrics file  

    - **args**  
        - `picard`: The picard executable, default: "picard"  
        - `params`: Other parameters for `picard CollectWgsMetrics`, default: ""  
        - `reffile`: The reference file, default: ""  

    - **requires**  
        [picard](https://broadinstitute.github.io/picard/)

!!! hint "pSortSam"

    - **description**  
        Use `picard SortSam` to sort sam or bam file

    - **input**  
        - `infile:file`: The sam or bam file to be sorted  

    - **output**  
        - `outfile:file`: The sorted sam or bam file  

    - **args**  
        - `picard`: The picard executable, default: "picard"  
        - `order`: The sort order, default: coordinate. Possible: unsorted, queryname, coordinate, duplicate  
        - `outtype`: The type of output file, sam or bam. Default: bam  
        - `params`: Other parameters for `picard SortSam`, default: ""  
        - `tmpdir`: The tmpdir to use. Default: /tmp  
        - `javamem`: The memory for java vm. Default: "-Xms1g -Xmx8g"  

    - **requires**  
        [picard](http://broadinstitute.github.io/picard/command-line-overview.html)

!!! hint "pIndexBam"

    - **description**  
        Use `picard BuildBamIndex` to index bam file

    - **input**  
        - `infile:file`: The bam file   

    - **output**  
        - `outfile:file`: The same bam file (link) but with .bai file in `proc.outdir`  

    - **args**  
        - `picard`: The picard executable, default: "picard"  
        - `params`: Other parameters for `picard BuildBamIndex`, default: "-Xms1g -Xmx8g"  

    - **requires**  
        [picard](http://broadinstitute.github.io/picard/command-line-overview.html)
## plot

!!! hint "pPlot"

    - **description**  
        Use ggplot2 to generate plots

    - **input**  
        - `infile:file`: The input data file  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `cnames` : Whether the input file has colnames. Default: True  
        - `rnames` : Whether the input file has rownames. Default: False  
        - `aes`    : The default aes. Default: {'x':1, 'y':2} (corresponding to colnames)  
        - `helper` : Some helper codes to generate `params` and `ggs`  
        - `devpars`: The device parameters. Default: `Box(res = 300, height = 2000, width = 2000)`  
        - `ggs`    : The extra ggplot elements.  

!!! hint "pScatter"

    - **description**  
        Use ggplot2 geom_point to generate plots

    - **infile**  
        - `infile:file`: The input data file  

    - **outfile**  
        - `outfile:file`: The output file  

    - **args**  
        - `cnames` : Whether the input file has colnames. Default: True  
        - `rnames` : Whether the input file has rownames. Default: False  
        - `x`      : The x aes. Default: 1 (corresponding to colnames)  
        - `y`      : The y aes. Default: 2 (corresponding to colnames)  
        - `helper` : Some helper codes to generate `params` and `ggs`  
        - `devpars`: The device parameters. Default: `Box(res = 300, height = 2000, width = 2000)`  
        - `params` : The extra params for `geom_point`  
        - `ggs`    : The extra ggplot elements.  

!!! hint "pPoints"

    - **description**  
        Alias for pScatter

!!! hint "pHisto"

    - **description**  
        Use ggplot2 geom_histogram to generate histograms

    - **infile**  
        - `infile:file`: The input data file  

    - **outfile**  
        - `outfile:file`: The output file  

    - **args**  
        - `cnames` : Whether the input file has colnames. Default: True  
        - `rnames` : Whether the input file has rownames. Default: False  
        - `x`      : The x aes. Default: 1 (corresponding to colnames)  
        - `helper` : Some helper codes to generate `params` and `ggs`  
        - `devpars`: The device parameters. Default: `Box(res = 300, height = 2000, width = 2000)`  
        - `params` : The extra params for `geom_point`  
        - `ggs`    : The extra ggplot elements.  

!!! hint "pFreqpoly"

    - **description**  
        Use ggplot2 geom_freqpoly to generate frequency polygon plot.

    - **infile**  
        - `infile:file`: The input data file  

    - **outfile**  
        - `outfile:file`: The output file  

    - **args**  
        - `cnames` : Whether the input file has colnames. Default: True  
        - `rnames` : Whether the input file has rownames. Default: False  
        - `x`      : The x aes. Default: 1 (corresponding to colnames)  
        - `helper` : Some helper codes to generate `params` and `ggs`  
        - `devpars`: The device parameters. Default: `Box(res = 300, height = 2000, width = 2000)`  
        - `params` : The extra params for `geom_point`  
        - `ggs`    : The extra ggplot elements.  

!!! hint "pBoxplot"

    - **description**  
        Generate box plot

    - **input**  
        - `datafile:file`: The data file  

    - **output**  
        - `outpng:file`: The output figure  

    - **args**  
        - `inopts` : Input options to read the input file  
        	- `cnames` :   Whether the input file has header. Default: `True`
        	- `rnames` :   Whether the input file has row names. Default: `False`
        	- `delimit`:   The seperator. Defualt: `\\t`
        - `x`      : The `ind` (index) column. Only for `args.stacked = True`. Default: `2`  
        - `y`      : The `values` column. Only for `args.stacked = True`. Default: `1`  
        - `helper` : Some raw codes to help to construct the matrix and arguments.  
        - `stacked`: Whether the input file is stacked  
        	- Stacked file looks like:
        	  ```
        	  values	ind
        	  1.1	col1
        	  1.2	col1
        	  ...
        	  .8	col2
        	  .9	col2
        	  ...
        	  3.2	col3
        	  ...
        	  ```
        	- Unstacked file looks like:
        	  ```
        	  col1	col2	col3
        	  1.1	.8	3.2
        	  1.2	.9	2.2
        	  ```
        - `params`: Other parameters for `boxplot`, default: `""`  
        - `ggs`   : Extra ggplot2 statements  

!!! hint "pHeatmap"

    - **description**  
        Plot heatmaps.

    - **input**  
        - `infile:file`: The input matrix file  

    - **output**  
        - `outfile:file`: The heatmap  

    - **args**  
        - `ggs`: The ggplot items for heatmap  
        - `devpars`: The parameters for device. Default: `{'res': 300, 'height': 2000, 'width': 2000}`  
        - `dendro`: The parameters for control of the dendrogram. Default: `{'dendro': True}`  
        	- `dendro`: `True`: plot dendros for both rows and cols; `col`: only plot dendro for cols; `row`: only plot dendro for rows
        	- `rows`: The rownames to subset the rows and control the order of rows. Must a list. Only works when not plotting dendro for rows.
        	- `cols`: The colnames to subset the cols and control the order of cols. Must a list. Only works when not plotting dendro for cols.
        - `header`: The input file has header? Default: True  
        - `rownames`: The input file has rownames? Default: 1  
        - `rows`: Row selector  
        	- `all`: All rows
        	- `top:N`: Top N rows (original data ordered in descending order). N defaults to 100
        	- `bottom:N`: Bottom N rows. N defaults to 100
        	- `both:N`: Top N rows and bottom N rows. N defaults to 50
        	- `random:N`: Random N rows. N defaults to 50
        	- `random-both:N`: Random N rows from top part and N rows from bottom part. N defaults to 50
        - `cols`: Col selector (see `rows`).  

!!! hint "pScatterCompare"

    - **description**  
        Plot scatter plot to compare values of first 2 columns of input data

    - **input**  
        - `infile:file`: The input file containing a matrix with at least 2 columns  
        	- Other columns are groups used to group the scatter points
        	- Data must be normalized to [0, 1]

    - **output**  
        - `outfile:file`: The output plot  

    - **args**  
        - `ggs`: Extra expressions for ggplot. Note if geom_point is included, original geom_point will be ignored.  
        - `devpars`: The parameters for plot device. Default: `{'res': 300, 'height': 2000, 'width': 2000}`  
        - `rownames`: Whether the input file has row names. Default: True  
        - `regr`: Whether draw the regression line. Default: False  
        - `corr`: The method to calculate the correlation. Default: `pearson`  
        	- Could be: `pearson`, `spearman` or `kendall`
        	- If it's neither of the three, no correlations will show.

!!! hint "pROC"

    - **description**  
        Generate ROC curves and output AUC.

    - **input**  
        - `infile:file`: The input matrix file.  
        	- Col1: rownames if args.rnames is True else label (0, 1 class)
        	- Col2: prediction values from model1
        	- ...

!!! hint "pVenn"

    - **description**  
        Venn/UpsetR plots.

    - **input**  
        - `infile:file`: The input matrix  
        	- format:
        	```
        		category1	category2	category3
        	[e1]	0	1	1
        	[e2]	0	0	1
        	...
        	[eN]	1	0	0
        	```
        	rownames are not necessary but colnames are.

    - **output**  
        - `outfile:file`: The plot  

    - **args**  
        - `tool`    : Which tools to use. Default: auto (venn, upsetr, auto(n<=3: venn, otherwise upsetr))  
        - `rnames`  : Whether input file has rownames. Default: False  
        - `params`  : Other params for `venn.diagram` or `upset`. Default: {}  
        - `devpars` : The parameters for plot device. Default: `{'res': 300, 'height': 2000, 'width': 2000}`  

    - **requires**  
        [`r-VennDiagram`](https://www.rdocumentation.org/packages/VennDiagram)
        [`r-UpSetR`](https://www.rdocumentation.org/packages/UpSetR)

!!! hint "pPie"

    - **description**  
        Plot piechart

    - **input**  
        - `infile:file`: The input file. Could be either:  
        	- Direct numbers of each category.
        	```
        	Group1	Group2
        	50	50
        	```
        	- Presence of each items in the category.
        	```
        		Group1	Group2
        	Item1	1	0
        	Item2	0	1
        	...
        	```

    - **output**  
        - `outfile:file`: the output plot  

    - **args**  
        - `rnames` : Whether the input file has row names. Default: `False`  
        - `ggs`    : Extra expressions for ggplot.  
        - `devpars`: The parameters for plot device. Default: `{'res': 300, 'height': 2000, 'width': 2000}`  
## power

!!! hint "pSurvivalPower"

    - **description**  
        Do power analysis for survival analysis.
        See http://www.sample-size.net/sample-size-survival-analysis/

    - **input**  
        - `infile:file`: The input file, could be either:  
         	- detailed suvival data with [`patient`, ]`time`, `status`, `variable1`, `variable2`, ...; or
        	- ratios with `variable`, `survrate1`, `survrate2`, `ssratio`, where `survrate1` and
        		`survrate2` are survival rates in group1 and group2, respectively,
        		and `ssratio` is sample size ratio in group1/group2

    - **output**  
        - `outfile:file`: The output file with columns:  
        	- Variable: the variable (including paired groups)
        	- Alpha: the alpha value
        	- Beta: the beta value (1-power)
        	- SSize1: the sample size for group1
        	- SSize2: the sample size for group2
        	- Total: the total sample size
## rank

!!! hint "pRankProduct"

    - **description**  
        Calculate the rank product of a set of ranks. Refer to [here](https://en.wikipedia.org/wiki/Rank_product)

    - **input**  
        - `infile:file`: The input file  
        - Format:
        ```
        			Case1	Case2	...
        Feature1	8.2  	10.1 	...
        Feature2	2.3  	8.0  	...
        ...
        ```
        - Or instead of values, you can also have ranks in the input file:
        ```
        			Rank1	Rank2	...
        Feature1	2    	1    	...
        Feature2	3    	2    	...
        ...
        ```

    - **output**  
        - `outfile:file`: The output file with original ranks, rank products and p-value if required  

    - **args**  
        - `informat`: The input format of the values. Whether they are real values (value) or ranks (rank). Default: value  
        - `pval`: Whether to calculate the p-value or not. Default: True  
        - `header`: Whether the input file has headers (rownames are required!). Default: True  
        - `plot`: Number of rows to plot. Default: 0 (Don't plot)  
        - `cex`: Font size for plotting. Default: 0.9  
        - `cnheight`: Colname height. Default: 80  
        - `rnwidth`: Rowname width. Default: 50  
        - `width`: Width of the png file. Default: 2000  
        - `height`: height of the png file. Default: 2000  
## resource

!!! hint "pTxt"

    - **description**  
        Download CSV format files.

    - **input**  
        - `in`: The name of the resource  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `cols`: Select the columns to keep. Default: '' (all cols)  
        - `rowfilter`: Filter rows. For example, to filter out rows not start with 'Chr':  
        	- `"lambda x: not x[0].startswith('Chr')"`
        	- Note that rowfilter applied before cols filter.
        - `urls`: Available resources and their urls.  
        - `gz`: Whether to gzip the output file.  

    - **requires**  
        [`curl`](https://en.wikipedia.org/wiki/CURL)
## rnaseq

!!! hint "pEXPRdir2Matrix"

    - **description**  
        Convert expression files to expression matrix
        File names will be used as sample names (colnames)
        Each gene and its expression per line.
        Suppose each expression file has the same rownames and in the same order.

    - **input**  
        - `indir:file`: the directory containing the expression files, could be gzipped  

    - **output**  
        - `outfile:file`: the expression matrix file  
        - `outdir:dir`: the directory containing expr file and plots  

    - **args**  
        - `pattern` : The pattern to filter files. Default `'*'`  
        - `namefunc`: Transform filename (no extension) as column name. Default: "function(fn) fn"  
        - `header`  : Whether each expression file contains header. Default: `False`  
        - `exrows`  : Rows to be excluded, regular expression applied. Default: `["^Sample", "^Composite", "^__"]`  
        - `boxplot` : Whether to plot a boxplot. Default: False  
        - `heatmap` : Whether to plot a heatmap. Default: False  
        - `histplot`: Whether to plot a histgram. Default: False  
        - `devpars` : Parameters for png. Default: `{'res': 300, 'width': 2000, 'height': 2000}`  
        - `boxplotggs`: The ggplot parameters for boxplot. Default: `['r:ylab("Expression")']`  
        	- See ggplot2 documentation.
        - `heatmapggs`: The ggplot parameters for heatmap. Default: `['r:theme(axis.text.y = element_blank())']`  
        - `histplotggs`: The ggplot parameters for histgram. Default: `['r:labs(x = "Expression", y = "# Samples")']`  

!!! hint "pBatchEffect"

    - **description**  
        Remove batch effect with sva-combat.

    - **input**  
        - `expr:file`: The expression file, generated by pEXPRdir2Matrix  
        - `batch:file`: The batch file defines samples and batches.  

    - **output**  
        - `outfile:file`: the expression matrix file  
        - `outdir:dir`: the directory containing expr file and plots  

    - **args**  
        - `tool`    : The tool used to remove batch effect. Default `'combat'`  
        - `hmrows`  : How many rows to be used to plot heatmap  
        - `plot`: Whether to plot  
        	- `boxplot`   : Whether to plot a boxplot. Default: False
        	- `heatmap`   : Whether to plot a heatmap. Default: False
        	- `histogram` : Whether to plot a histgram. Default: False
        - `devpars`    : Parameters for png. Default: `{'res': 300, 'width': 2000, 'height': 2000}`  
        - `ggs`: The ggplot parameters  
        	- `boxplot`  : The ggplot parameters for boxplot. Default: `Box(ylab = {0: "Log2 Intensity"})`
        	- `heatmap`  : The ggplot parameters for heatmap. Default: `Box(theme = {'axis.text.y': 'r:element_blank()'})`
        	- `histogram`: The ggplot parameters for histgram. Default: `Box(labs = {'x': "Log2 Intensity", "y": "Density"})`

!!! hint "pRawCounts2"

    - **description**  
        Convert raw counts to another unit

    - **input**  
        - `infile:file`: the expression matrix  
        	- rows are genes, columns are samples

    - **output**  
        - `outfile:file`: the converted expression matrix  

    - **args**  
        - `transpose`: transpose the input matrix? default: False  
        - `log2`: whether to take log2? default: False  
        - `unit`: convert to which unit? default: cpm (or rpkm, tmm)  
        - `header`: whether input file has header? default: True  
        - `rownames`: the index of the column as rownames. default: 1  
        - `glenfile`: the gene length file, for RPKM  
        	- no head, row names are genes, have to be exact the same order and length as the rownames of infile
        - `boxplot` : Whether to plot a boxplot. Default: False  
        - `heatmap` : Whether to plot a heatmap. Default: False  
        - `histplot`: Whether to plot a histgram. Default: False  
        - `devpars` : Parameters for png. Default: `{'res': 300, 'width': 2000, 'height': 2000}`  
        - `boxplotggs`: The ggplot parameters for boxplot. Default: `['r:ylab("Expression")']`  
        	- See ggplot2 documentation.
        - `heatmapggs`: The ggplot parameters for heatmap. Default: `['r:theme(axis.text.y = element_blank())']`  
        - `histplotggs`: The ggplot parameters for histgram. Default: `['r:labs(x = "Expression", y = "# Samples")']`  

    - **requires**  
        [edgeR](https://bioconductor.org/packages/release/bioc/html/edger.html) if cpm or rpkm is chosen
        [coseq](https://rdrr.io/rforge/coseq/man/transform_RNAseq.html) if tmm is chosen

!!! hint "p2RawCounts"

    - **description**  
        Convert gene expression to raw counts.

    - **input**  
        - `infile:file`: The expression matrix file  

    - **output**  
        - `outfile:file`: The output file  
        - `outdir:dir`: The output directory, may contain the figures.  

    - **args**  
        - `unit`: The unit of input gene expression. Default: fpkm  
        	- Could also be rpkm, tpm
        - `nreads`     : Total reads approximately. Default: 30, 000, 000  
        - `refgene`    : The refgene file for gene length.  
        - `boxplot`    : Whether to plot boxplot after transformation. Default: False  
        - `heatmap`    : Whether to plot heatmap after transformation. Default: False  
        - `heatmapn`   : How many genes used to plot heatmap. Default: 500  
        - `histplot`   : Whether to plot histgram after transformation. Default: False  
        - `devpars`    : The device parameters for plotting. Default: `{'res': 300, 'width': 2000, 'height': 2000}`  
        - `boxplotggs` : The ggplot statement for boxplot.  
        - `heatmapggs` : The ggplot statement for heatmap.  
        - `histplotggs`: The ggplot statement for histgram.  

!!! hint "pRNAseqDEG"

    - **description**  
        Detect DEGs for RNA-seq data

    - **input**  
        - `efile:file`: The expression matrix  
        - `gfile:file`: The group information  
        	- Like:
        	```
        	Sample1	Group1
        	Sample2	Group1
        	Sample3	Group1
        	Sample4	group2
        	Sample5	group2
        	Sample6	group2
        	```

    - **output**  
        - `outfile:file`: The DEG list  
        - `outdir:file`: The output directory containing deg list and plots  

    - **args**  
        - `tool`      : the tool used to detect DEGs. Default: 'edger' (deseq2)  
        - `filter`    : filter out low count records. Default: `"1,2"` (At least 2 samples have at least 2 reads)  
        - `mdsplot`   : whether to plot the MDS plot, default : True  
        - `volplot`   : whether to plot the volcano plot, default : True  
        - `maplot`    : whether to plot MA plots within each group, default : False  
        - `heatmap`   : whether to plot the heatmap using DEGs. Default : False  
        - `heatmapn`  : How many genes to be used for heatmap. If `heatmapn`, the number will be `heatmapn * # DEGs`. Default: 100  
        - `heatmapggs`: The ggplots options for heatmap. Default : []  
        - `maplotggs` : The ggplots options for maplot. Default : []  
        - `volplotggs`: The ggplots options for volplot. Default : []  
        - `devpars`   : Parameters for png. Default: `{'res': 300, 'width': 2000, 'height': 2000}`  

!!! hint "pCoexp"

    - **description**  
        Get co-expression of gene pairs in the expression matrix.
## sambam

!!! hint "pSam2Bam"

    - **description**  
        Deal with mapped sam/bam files, including sort, markdup, and/or index

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output bam file  
        - `idxfile:file`: The index of the output bam file  
        - If args.index == False, it'll a link to outfile and should be never used

    - **args**  
        - `tool`             : The tool used to do the sort. Default: sambamba (picard|sambamba|biobambam|samtools)  
        - `sambamba`         : The path of the sambamba. Default: sambamba  
        - `picard`           : The path of the picard. Default: picard  
        - `biobambam_bamsort`: The path of the biobambam's bamsort. Default: bamsort  
        - `samtools`         : The path of the samtools. Default: samtools  
        - `sort`             : Do sorting? Default: True  
        - If input is sam, tool is biobambam, this should be True
        - `index`            : Do indexing? Default: True  
        - `markdup`          : Do duplicates marking? Default: False  
        - `rmdup` for samtools will be called
        - `rmdup`            : Do duplicates removing? Default: False  
        - `tmpdir`           : The tmp dir used to store tmp files. Default: <system default tmpdir>  
        - `sortby`           : Sort by coordinate or queryname. Default: coordinate  
        - `nthread`          : Default: 1  
        - `informat`         : The format of input file. Default: <detect from extension> (sam|bam)  
        - `params`           : Other parameters for `tool`. Defaut: ""  
        - `mem`              : The max memory to use. Default: "16G"  
        - Unit could be G/g/M/m
        - Will be converted to -Xmx4G, and -Xms will be 1/8 of it

    - **requires**  
        [sambamba](https://lomereiter.github.io/sambamba/docs/sambamba-view.html) if `args.tool` == samtools or reference used but not indexed.
        [picard](https://broadinstitute.github.io/picard/command-line-overview.html)
        [biobambam](https://github.com/gt1/biobambam2)
        [samtools](https://github.com/samtools/samtools)

!!! hint "pBamMarkdup"

    - **description**  
        Mark/remove duplicates for bam files

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output bam file  

    - **args**  
        - `tool`             : The tool used to do the sort. Default: sambamba (picard|sambamba|biobambam|samtools|bamutil)  
        - `sambamba`         : The path of sambamba. Default: sambamba  
        - `picard`           : The path of picard. Default: picard  
        - `biobambam_bamsort`: The path of biobambam's bamsort. Default: bamsort  
        - `samtools`         : The path of samtools. Default: samtools  
        - `bamutil`          : The path of bamutil. Default: bam  
        - `rmdup`            : Do duplicates removing? Default: False  
        - Samtools will anyway remove the duplicates
        - `tmpdir`           : The tmp dir used to store tmp files. Default: <system default tmpdir>  
        - `nthread`          : Default: 1  
        - Not available for samtools and picard
        - `params`           : Other parameters for `tool`. Defaut: ""  
        - `mem`              : The max memory to use. Default: "16G"  
        - Unit could be G/g/M/m
        - Will be converted to -Xmx4G, and -Xms will be 1/8 of it

    - **requires**  
        [sambamba](https://lomereiter.github.io/sambamba/docs/sambamba-view.html)
        [picard](https://broadinstitute.github.io/picard/command-line-overview.html)
        [biobambam](https://github.com/gt1/biobambam2)
        [samtools](https://github.com/samtools/samtools)
        [bamutil](http://genome.sph.umich.edu/wiki/BamUtil#Programs)

!!! hint "pBamRecal"

    - **description**  
        Recalibrate a bam file

    - **input**  
        - `infile:file`: The bam file  

    - **output**  
        - `outfile:file`: The output bam file  

    - **args**  
        - `tool`                         : The tool used to recalibrate the bam file. Default: `gatk` (gatk|bamutil)  
        - `gatk`                         : The path of gatk, including java path. Default: `gatk`  
        - `samtools`                     : The path of samtools. Default: `samtools`  
        - `bamutil`                      : The path of bamutil. Default: `bam`  
        - `picard`                       : The path of picard. Default: `picard`  
        - `paramsRealignerTargetCreator` : Other parameters for `gatk RealignerTargetCreator`. Defaut: ""  
        - `paramsIndelRealigner`         : Other parameters for `gatk IndelRealigner`. Defaut: ""  
        - `paramsBaseRecalibrator`       : Other parameters for `gatk BaseRecalibrator`. Defaut: ""  
        - `paramsPrintReads`             : Other parameters for `gatk PrintReads`. Defaut: ""  
        - `params`                       : Other parameters for `bam recab`. Default: ""  
        - `mem`                          : The max memory to use. Default: "32G"  
        - `knownSites`                   : The known polymorphic sites to mask out. Default: "" (Required for GATK)  
        - `ref`                          : The reference file. Required.  
        - Will be converted to -Xmx4G, and -Xms will be 1/8 of it

    - **requires**  
        [gatk](https://software.broadinstitute.org/gatk)
        [samtools](https://github.com/samtools/samtools) if `args.ref` is not indexed, or bamutil is used for bam index file generation.
        [picard](https://broadinstitute.github.io/picard/command-line-overview.html) if `args.ref is not dicted.`

!!! hint "pBamReadGroup"

    - **description**  
        Add or replace read groups of a bam file

    - **input**  
        - `infile:file`: The bam file  

    - **output**  
        - `outfile:file`: The output bam file  

    - **args**  
        - `tool`                         : The tool used. Default: `picard` (picard|bamutil)  
        - `picard`                       : The path of picard. Default: `picard`  
        - `bamutil`                      : The path of bamutil. Default: `bam`  
        - `rg`                           : The read group. Default: {'id': '', 'pl': 'Illumina', 'pu': 'unit1', 'lb': 'lib1', 'sm': ''}  
        - `id` will be parsed from filename with "_LX_" in it if not given
        - `sm` will be parsed from filename
        - `params`                       : Other parameters for `tool`. Defaut: ""  
        - `mem`                          : The max memory to use. Default: "4G"  
        - Will be converted to -Xmx4G, and -Xms will be 1/8 of it
        - `tmpdir`                       : The temporary directory. Default: <system tmpdir>  

    - **requires**  
        [gatk](https://lomereiter.github.io/sambamba/docs/sambamba-view.html)
        [samtools](https://github.com/samtools/samtools) if `args.ref` is not indexed.
        [picard](https://broadinstitute.github.io/picard/command-line-overview.html) if `args.ref is not dicted.`

!!! hint "pBamReorder"

    - **description**  
        Reorder a sam/bam file by a given reference file using `picard ReorderSam`

    - **input**  
        - `infile:file`: The sam/bam file  

    - **output**  
        - `outfile:file`: The output bam file  

    - **args**  
        - `picard`                       : The path of picard. Default: `picard`  
        - `ref`                          : The reference file. Required  
        - `params`                       : Other parameters for `picard ReorderSam`. Defaut: ""  
        - `mem`                          : The max memory to use. Default: "4G"  
        - Will be converted to -Xmx4G, and -Xms will be 1/8 of it
        - `tmpdir`                       : The temporary directory. Default: <system tmpdir>  

    - **requires**  
        [picard](https://broadinstitute.github.io/picard/command-line-overview.html)

!!! hint "pBamMerge"

    - **description**  
        Merges multiple SAM and/or BAM files (must be sorted by coordinate) into a single file.

    - **input**  
        - `infiles:file`: Input sam/bam files to be merged  

    - **output**  
        - `outfile:file`: The merged bam file  

    - **args**  
        - `tool`     : The tool used to merge. Default: bamutil (picard|samtools|sambamba)  
        - `picard`   : The path of picard. Default: `picard`  
        - `bamutil`  : The path of bamutil. Default: `bam`  
        - `samtools` : The path of samtools. Default: `samtools`  
        - `sambamba` : The path of sambamba. Default: `sambamba`  
        - `params`   : Other parameters for `tool`. Defaut: ""  
        - `mem`      : The max memory to use. Default: "4G"  
        - Will be converted to -Xmx4G, and -Xms will be 1/8 of it, just for picard
        - `tmpdir`   : The temporary directory. Default: <system tmpdir>  
        - `nthread`  : # threads to use. Default: 1  
        - For picard, if nthread>1, USE_THREADING=true, otherwise USE_THREADING=false

    - **requires**  
        [picard](https://broadinstitute.github.io/picard/command-line-overview.html)

!!! hint "pBam2Gmut"

    - **description**  
        Call germline (snps and indels) from a call-ready bam file.

    - **input**  
        - `infile:file`: The input bam file  

    - **output**  
        - `outfile:file`: The vcf file containing the mutations  

    - **args**  
        - `tool`: The tool used to call mutations. Default: gatk (vardict, snvsniffer, platypus, strelka)  
        - `gatk`: The path of gatk. Default: gatk  
        - `vardict`: The path of vardict. Default: vardict  
        - `snvsniffer`: The path of snvsniffer. Default: SNVSniffer  
        - `samtools`: The path of samtools. Default: samtools (used to generate reference index)  
        - `platypus`: The path of platypus. Default: platypus  
        - `strelka`: The path of strelka. Default: configureStrelkaGermlineWorkflow.py  
        - `configParams`: The params for `strelka` configuration. Default: ""  
        - `picard`: The path of picard. Default: picard  
        - `mem`: The memory to be used. Default: 32G  
        - will be converted to -Xms4G -Xmx32G for java programs
        - `ref`: The reference file. Required.  
        - `gz`: Gzip output file? Default: False  
        - `tmpdir`: The temporary directory. Default: <system tmpdir>  
        - `params`: Other params for `tool`. Default: ""  

    - **requires**  
        [gatk](https://lomereiter.github.io/sambamba/docs/sambamba-view.html)
        [samtools](https://github.com/samtools/samtools) if `args.ref` is not indexed.
        [picard](https://broadinstitute.github.io/picard/command-line-overview.html) if `args.ref is not dicted.`
        [vardict](https://github.com/AstraZeneca-NGS/VarDict)
        [snvsniffer](http://snvsniffer.sourceforge.net/homepage.htm#latest)
        [platypus](http://www.well.ox.ac.uk/platypus)
        [strelka@2.7.1+](https://github.com/Illumina/strelka)

!!! hint "pBamPair2Smut"

    - **description**  
        Call somatic mutations from tumor-normal bam pair.

    - **input**  
        - `tumor:file`: The tumor bam file  
        - `normal:file`: The normal bam file  

    - **output**  
        - `outfile:file`: The vcf file  

    - **args**  
        - `tool`: The tool used to call mutations. Default: gatk (somaticsniper, strelka, snvsniffer, virmid, varidct)  
        - `gatk`: The path to gatk. Default: gatk  
        - `somaticsniper`: The path to gatk. Default: bam-somaticsniper  
        - `strelka`: The path to gatk. Default: configureStrelkaSomaticWorkflow.py  
        - `snvsniffer`: The path to gatk. Default: SNVSniffer  
        - `virmid`: The path to gatk. Default: virmid  
        - `vardict`: The path to gatk. Default: vardict  
        - `samtools`: The path to gatk. Default: samtools  
        - `picard`: The path to gatk. Default: picard  
        - `configParams`: The configuration parameters for `configureStrelkaSomaticWorkflow.py`. Default: `{}`  
        - `params`: The parameters for main programs. Default: `{}`  
        - `meme`: The memory. Default: 24G  
        - `ref`: The reference genom. Default: `params.ref.value`  
        - `gz`: Whether gzip the output vcf file. Default: False  
        - `nthread`: The number of threads to use. Default: 1  
        - `tmpdir`: The temporary directory. Default: `params.tmpdir.value`  

    - **requires**  
        [gatk](https://lomereiter.github.io/sambamba/docs/sambamba-view.html)
        [samtools](https://github.com/samtools/samtools) if `args.ref` is not indexed.
        [picard](https://broadinstitute.github.io/picard/command-line-overview.html) if `args.ref is not dicted.`
        [vardict](https://github.com/AstraZeneca-NGS/VarDict)
        [snvsniffer](http://snvsniffer.sourceforge.net/homepage.htm#latest)
        [platypus](http://www.well.ox.ac.uk/platypus)
        [strelka@2.7.1+](https://github.com/Illumina/strelka)

!!! hint "pBam2Cnv"

    - **description**  
        Detect copy number variation from bam files.

    - **input**  
        - `input:file`: The bam file  

    - **output**  
        - `outfile:file`: The output vcf file  
        - `outdir`: The output directory containing other result files  

    - **args**  
        - `gz`                    : Whether to gzip the output vcf file. Default: False  
        - `tool`                  : The tool used to call cnv. Default: 'cnvkit'  
        - `cnvnator`              : The path of cnvnator. Default: 'cnvnator'  
        - `cnvnator2vcf`          : The path of cnvnator2VCF. Default: 'cnvnator2VCF.pl'  
        - `cnvkit`                : The path of cnvkit. Default: 'cnvkit.py'  
        - `wandy`                 : Tha path of Wandy. Default: 'Wandy'. A `tool.info` file should be with the executable file.  
        - `ref`                   : The reference file. Required by cnvkit to generate access file. Default: ''  
        - `cnvkitAccessParams`    : The params for cnvkit access command. Default: '-s 5000'  
        - `cnvkitTargetParams`    : The params for cnvkit target command. Default: '--split --short-names'  
        - `cnvkitCoverageParams`  : The params for cnvkit coverage command. Default: ''  
        - `cnvkitReferenceParams` : The params for cnvkit reference command. Default: '--no-edge'  
        - `cnvkitFixParams`       : The params for cnvkit fix command. Default: '--no-edge'  
        - `cnvkitSegmentParams`   : The params for cnvkit segment command. Default: ''  
        - `cnvkitCallParams`      : The params for cnvkit call command. Default: ''  
        - `cnvkitPlotParams`      : The params for cnvkit plot command. Default: ''  
        - `cnvkitBreaksParams`    : The params for cnvkit breaks command. Default: ''  
        - `cnvkitGainlossParams`  : The params for cnvkit gainloss command. Default: ''  
        - `cnvkitMetricsParams`   : The params for cnvkit metrics command. Default: ''  
        - `cnvkitSegmetricsParams`: The params for cnvkit segmetrics command. Default: '--iqr'  
        - `cnvkitExportParams`    : The params for cnvkit export command. Default: ''  
        - `cnvkitScatterParams`   : The params for cnvkit scatter command. Default: [''] # multiple scatter plots  
        - `cnvkitHeatmapParams`   : The params for cnvkit heatmap command. Default: [''] # multiple heatmap plots  
        - `cnvkitDiagramParams`   : The params for cnvkit diagram command. Default: ''  
        - `cnvkitReport`          : Generate cnvkit reports? Default: True  
        - `cnvkitPlot`            : Generate cnvkit plots? Default: True  
        - `cnvnatorBinsize`       : Bin size for cnvnator. Default: 100  
        - `cnvnatorGenome`        : Genome for cnvnator. Default: 'hg19'. (NCBI36, hg18, GRCh37, hg19)  
        - `params`                : The params for `tool`. Default: '-t 1' # wandy 1:hg19 solid cell/blood, 2:hg19 cell free/plamsa, 3:hg38 solid cell/blood, 4:hg38 cell free/plamsa  
        - `mem`                   : The memory used. Default: '20G' # only for wandy  
        - `nthread`               : The # threads to use. Default: 1	 # only for cnvkit  

    - **requires**  
        [`cnvkit`](http://cnvkit.readthedocs.io/en/stable/index.html)
        [`cnvnator`](https://github.com/abyzovlab/CNVnator)
        - `wandy`: Inside cnv caller  

!!! hint "pBamStats"

    - **description**  
        Get read depth from bam files.

    - **input**  
        - `infile:file`: The input bam file  

    - **output**  
        - `outfile:file`: The output statistic file  
        - `outdir:dir`: The directory containing result files and figures.  

    - **args**  
        - `tool`: The tool used to do the job. Default: bamstats  
        - `bamstats`: The path to bamstats. Default: bamstats  
        - `params`: Other params to main program. Default: `{}`  
        - `mem`: The memory to be used. Default: 16G  
        - `plot`: Whether plot the result. Default: True  

!!! hint "pBam2Fastq"

    - **description**  
        Convert sam/bam files to pair-end fastq files.

    - **input**  
        - `infile:file`: The sam/bam file.  
        	- Sam files only available for biobambam, picard

    - **output**  
        - `fqfile1:file`: The 1st match of paired reads  
        - `fqfile2:file`: The 2nd match of paired reads  

    - **args**  
        - `tool`     : The tool to use. Default: biobambam (bedtools, samtools, picard)  
        - `biobambam`: The path of bamtofastq of biobambam. Default: bamtofastq  
        - `bedtools` : The path of bedtools. Default: bedtools  
        - `samtools` : The path of samtools. Default: samtools  
        - `picard`   : The path of picard. Default: picard  
        - `mem`      : The memory to be used by picard. Default: 8G  
        - `gz`       : Whether gzip the output files. Default: True  
        - `params`: : Other params for `tool`. Default: ''  
        - `tmpdir`   : The tmpdir. Default: `__import__('tempfile').gettempdir()`  

    - **requires**  
        [picard](https://broadinstitute.github.io/picard/command-line-overview.html)
        [biobambam](https://github.com/gt1/biobambam2)
        [samtools](https://github.com/samtools/samtools)
        [bedtools](http://bedtools.readthedocs.io/en/latest/content/bedtools-suite.html)

!!! hint "pBam2FastqSE"

    - **description**  
        Convert sam/bam files to single-end fastq files.

    - **input**  
        - `infile:file`: The sam/bam file.  
        	- Sam files only available for biobambam, picard

    - **output**  
        - `fqfile:file`: The fastq file  

    - **args**  
        - `tool`     : The tool to use. Default: biobambam (bedtools, samtools, picard)  
        - `biobambam`: The path of bamtofastq of biobambam. Default: bamtofastq  
        - `bedtools` : The path of bedtools. Default: bedtools  
        - `samtools` : The path of samtools. Default: samtools  
        - `picard`   : The path of picard. Default: picard  
        - `mem`      : The memory to be used by picard. Default: 8G  
        - `gz`       : Whether gzip the output files. Default: True  
        - `params`: : Other params for `tool`. Default: ''  
        - `tmpdir`   : The tmpdir. Default: `__import__('tempfile').gettempdir()`  

    - **requires**  
        [picard](https://broadinstitute.github.io/picard/command-line-overview.html)
        [biobambam](https://github.com/gt1/biobambam2)
        [samtools](https://github.com/samtools/samtools)
        [bedtools](http://bedtools.readthedocs.io/en/latest/content/bedtools-suite.html)

!!! hint "pBam2Counts"

    - **description**  
        Extract read counts from RNA-seq bam files.

    - **input**  
        - `infile:file`: The input bam files  

    - **outfile**  
        - `outfile:file`: The count file  

    - **args**  
        - `tool`: The tool used to extract counts. Default: ht-seq  
        - `htseq`: The path of htseq-count.  
        - `params`: Other params for main program.  
        - `refgene`: The reference gene in GTF format.  

    - **requires**  
        [`htseq`](https://htseq.readthedocs.io/)
## seq

!!! hint "pConsvPerm"

    - **description**  
        Generate a null distribution of conservation scores.

    - **input**  
        - `seed`: The seed to generate the random regions. Default: None  

    - **output**  
        - `outfile:file`: A file with mean conservation scores sorted descendingly.  

    - **args**  
        - `len`: The length of a random region. Default: 50  
        - `nperm`: Number of permutations. Default: 1000  
        - `gsize`: The chrom size file.  
        - `bedtools`: The path of bedtools.  
        - `bwtool`: The path of bwtool.  
        - `consvdir`: The directory containing bigwig files of conservation scores  
        	- The bigwig file should start with chr name: chrN.*

    - **requires**  
        [bwtool](https://github.com/CRG-Barcelona/bwtool)
        [bedtools](http://bedtools.readthedocs.io/en/latest/content/bedtools-suite.html)

!!! hint "pConsv"

    - **description**  
        Get the conservation scores of regions.
        It uses wigFix to find the conservation scores.
        But first you have to convert those wigFix.gz files to bigWig files using ucsc-wigToBigWig

    - **input**  
        - `bedfile:file`: The bedfile with regions in the same chromosome  
        - `permfile:file`: The permutaiton file generated by `pConsvPerm`, used to calculate p-values  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `consvdir`: The bigwig directory, the bigwig files must be named as "chrN.*.bw"  
        	- For example: `chr1.phyloP30way.bw`
        - `bwtool`: The path of bwtool executable. Default: `bwtool`  
        - `bedtools`: The path of bedtools executable. Default: `bedtools`  
        - `pval`: Whether calculate pvalue of each region. Default: False  
        	- In this case, the `in.permfile` can be ignored.

    - **requires**  
        [bwtool](https://github.com/CRG-Barcelona/bwtool)
        [bedtools](http://bedtools.readthedocs.io/en/latest/content/bedtools-suite.html)

!!! hint "pPromoters"

    - **description**  
        Get the promoter regions in bed format of a gene list give in infile.

    - **input**  
        - `infile:file`: the gene list file  

    - **output**  
        - `outfile:file`: the bed file containing the promoter region  

    - **args**  
        - `up`: the upstream to the tss, default: 2000  
        - `down`: the downstream to the tss, default: 2000  
        - `genome`: the genome, default: hg19  

    - **require**  
        [python-mygene](http://mygene.info/)
## snp

!!! hint "pSnp2Bedx"

    - **description**  
        Find coordinates for SNPs in BEDX format.

    - **input**  
        - `snpfile:file`: the snp file, each snp per line  

    - **output**  
        - `outfile:file`: the result file, columns are:  
        	- chrom, start(0-based), end, name, score, strand, ref, allele

    - **args**  
        - `genome`: default: hg19  
        - `snpver`: default: snp147  
        - `notfound`: What to do if the snp is not found. Default: skip  
        - `inmeta`: The metadata for input file to determine which column is rsID  
        - `xcols`: The extra columns to extract and output to extra columns in output file.  
        - `indem`: The input delimit. Default: '\\t'  
        - `incom`: The input comment. Default: '#'  
        - `skip`: The lines to skip for input file. Default: 0  

    - **requires**  
        [`python-cruzdb`](https://github.com/brentp/cruzdb)

!!! hint "pSnp2Avinput"

    - **description**  
        Convert SNP list to avinput to ANNOVAR.

    - **input**  
        - `snpfile:file`: the snp file, each snp per line  

    - **output**  
        - `outfile:file`: the result avinput file  

    - **args**  
        - `genome`: default: hg19  
        - `snpver`: default: snp147  

    - **requires**  
        [`python-cruzdb`](https://github.com/brentp/cruzdb)
## snparray

!!! hint "pGistic"

    - **description**  
        Runing GISTIC to get CNV results.
        see: ftp://ftp.broadinstitute.org/pub/GISTIC2.0/GISTICDocumentation_standalone.htm

    - **input**  
        - `segfile:file`: Segmentation File  
        - `mkfile:file` : Markers File  
        - `alfile:file` : Array List File  
        - `cnvfile:file`: CNV File  

    - **output**  
        - `outdir:dir`: The output directory  
        	- All Lesions File (all_lesions.conf_XX.txt, where XX is the confidence level)
        	- Amplification Genes File (amp_genes.conf_XX.txt, where XX is the confidence level)
        	- Deletion Genes File (del_genes.conf_XX.txt, where XX is the confidence level)
        	- Gistic Scores File (scores.gistic)
        	- Segmented Copy Number (raw_copy_number.pdf)

    - **args**  
        - `gistic`: The path to gistic.  
        - `genome`: The genome used to select refgene file from refgenefiles.  
        - `mcr`: The mcr path  
        - `params`: Other params for gistic  

!!! hint "pSNP6Genotype"

    - **description**  
        Call genotypes from GenomeWideSNP_6 CEL file

    - **input**  
        - `celfile:file`: the CEL file  

    - **output**  
        - `outfile:file`: the outfile containing probe name and genotypes  
        - format: `<Probe name>\t<genotype>`
        - `<genotype>` = 0: AA, 1: AB, 2: BB

    - **requires**  
        [bioconductor-crlmm](http://bioconductor.org/packages/release/bioc/html/crlmm.html)

!!! hint "pGenoToAvInput"

    - **description**  
        Convert the genotype called by pSNP6Genotype to [ANNOVAR input file](http://annovar.openbioinformatics.org/en/latest/user-guide/input/#annovar-input-file) using dbSNP identifiers.	

    - **input**  
        - `genofile:file`: the genofile generated by pSNP6Genotype, must be sorted by probe names  
        - `annofile:flie`: the annotation file downloaded from http://www.affymetrix.com/support/technical/annotationfilesmain.affx  
        	- Could be in .gz format

    - **output**  
        - `outfile:file`: the avinput file  

    - **requires**  
        [python-read2](https://github.com/pwwang/read2)
## sql

!!! hint "pCreateTable"

    - **description**  
        Create tables in the database

    - **input**  
        - `dsn`: The dsn to connect to the database  
        	- currently support `sqlite:file=...`
        - `schema:file`: The schema file  
        	- could be a pure schema file:
        	```
        	Field	Type	Statement
        	ID	INT	PRIMARY KEY
        	...
        	```
        	- or a data file with header

    - **output**  
        - `dsn`: The dsn  

    - **args**  
        - `intype`: The input file schema file or a data file. Default: `schema`  
        - `drop`: Force creating the table (drop the pre-existing table)  
        - `delimit`: The delimit of input file. Default: `\\t`  

!!! hint "pImportData"

    - **description**  
        Create tables and import the data

    - **input**  
        - `dsn`: The dsn to connect to the database  
        	- currently support `sqlite:file=...`
        - `datafile:file`: The schema file  
        	- must have header

    - **output**  
        - `dsn`: The dsn  

    - **args**  
        - `delimit`: The delimit of input file. Default: `\\t`  

!!! hint "pUpdateTable"

    - **description**  
        Update table using sql.

    - **input**  
        - `dsn`: The dsn to connect to the database  
        	- currently support `sqlite:file=...`

    - **output**  
        - `dsn`: The dsn  

    - **args**  
        - `sql`: The sql to update the table (list)  

!!! hint "pSelectTable"

    - **description**  
        Select data from table and dump it.

    - **input**  
        - `dsn`: The dsn to connect to the database  
        	- currently support `sqlite:file=...`

    - **output**  
        - `outfile:file`: The dumped file  

    - **args**  
        - `sql`: The sql to select data from the table (list)  
## stats

!!! hint "pMetaPval"

    - **description**  
        Combine p-values in the files from input directory

    - **input**  
        - `indir:dir`: The directory containing the input files  

    - **output**  
        - `outfile:file`: The output file containing the meta-pvalues  

    - **args**  
        - `args.pattern`: The pattern used to filter the input files. Default: '*'  
        - `args.header`: Whether the input files contains a header. Default: True  
        	- Could be a list to specify it for each file.
        	- The order should be concordant with the file names
        - `args.pcol`: Which column is the p-value. Default: -1 (last column)  
        - `args.poutonly`: Only output pvalues. Default: False (output all possible information)  
        - `args.outheader`: Whether output the header. Default: True  
        - `args.method`: The method used to calculate the meta-pvalue. Default: sumlog (Fisher's method)  
        	- Other available methods: logitp, sumz, votep, sump, meanp and wilkinsonp
        	- See: https://www.rdocumentation.org/packages/metap/versions/0.8

    - **requires**  
        [`r-matep`](https://www.rdocumentation.org/packages/metap/)

!!! hint "pMetaPval1"

    - **description**  
        Combine p-values in a single file by rows.

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output file containing the meta-pvalues  

    - **args**  
        - `args.header`: Whether the input files contains a header. Default: True  
        - `args.pcol`: Which column is the p-value. Default: -1 (last column)  
        - `args.poutonly`: Only output pvalues. Default: False (output all possible information)  
        - `args.outheader`: Whether output the header. Default: True  
        - `args.method`: The method used to calculate the meta-pvalue. Default: sumlog (Fisher's method)  
        	- Other available methods: logitp, sumz, votep, sump, meanp and wilkinsonp
        	- See: https://www.rdocumentation.org/packages/metap/versions/0.8

    - **requires**  
        [`r-matep`](https://www.rdocumentation.org/packages/metap/)

!!! hint "pSurvival"

    - **description**  
        Survival analysis

    - **input**  
        - `infile:file`: The input file (header is required).  
        	- col1: rownames if args.inopts.rnames = True
        	- col2: the survival time
        	- col3: the status. 0/1 for alive/dead or 1/2 for alive dead
        	- col4: var1.
        	- ... other variables

    - **output**  
        - `outfile:file`: The outfile containing the pvalues  
        - `outdir:dir`  : The output directory containing the pval files and plots  

    - **args**  
        - `inunit`    : The time unit in input file. Default: days  
        - `outunit`   : The output unit for plots. Default: days  
        - `nthread`   : Number of threads used to perform analysis for groups. Default: 1  
        - `inopts`    : The options for input file  
        	- `rnames`: Whether input file has row names. Default: True
        - `combine`   : Whether combine groups in the same plot. Default: True  
        - `devpars`   : The device parameters for png. Default: `{res:300, height:2000, width:2000}`  
        	- The height and width are for each survival plot. If args.combine is True, the width and height will be multiplied by `max(arrange.ncol, arrange.nrow)`
        - `covfile`   : The covariant file. Require rownames in both this file and input file.  
        - `ngroups`   : Number of curves to plot (the continuous number will divided into `ngroups` groups.  
        - `plot`      : The params for plot.  
        	- `params` : The params for `ggsurvplot`. Default: `Box({'risk.table': True, 'conf.int': True, 'font.legend': 13, 'pval': '{method}\np = {pval}'})`
        		- You may do `ylim.min` to set the min ylim. Or you can set it as 'auto'. Default: 0. 
        	- `arrange`: How to arrange multiple survival plots in one if `args.combine = True`.
        		- `nrow`: The number of rows. Default: 1
        		- `ncol`: The number of cols. Default: 1
        - `ggs`       : Extra ggplot2 elements for main plot. `ggs.table` is for the risk table.  
        - `pval`      : The method to calculate the pvalue shown on the plot. Default: True (logrank)  
        	- Could also be `waldtest`, `likeratio` (Likelihoold ratio test)
        - `method`    : The method to do survival analysis.   

    - **requires**  
        [`r-survival`](https://rdrr.io/cran/survival/)
        [`r-survminer`](https://rdrr.io/cran/survminer/)

!!! hint "pChiSquare"

    - **description**  
        Do chi-square test.

    - **input**  
        - `infile:file`: The input file.  

    - **output**  
        - `outfile:file` : The output file containing Xsquare, df, pval and method  
        - `obsvfile:file`: The observation matrix  
        - `exptfile:file`: The expectation matrix  

    - **args**  
        - `intype`: The type of the input file:  
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
        - `ctcols`: The colnames of contingency table if input file is raw values  
        	- You may also specify them in the head of the input file

!!! hint "pFisherExact"

    - **description**  
        Do fisher exact test.

    - **input**  
        - `infile:file`: The input file.  

    - **output**  
        - `outfile:file` : The output file containing confInt1, confInt2, oddsRatio, pval, alternative and method.  

    - **args**  
        - `intype`: The type of the input file:  
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
        - `ctcols`: The colnames of contingency table if input file is raw values  
        	- You may also specify them in the head of the input file

!!! hint "pPWFisherExact"

    - **description**  
        Do pair-wise fisher exact test.
        Commonly used for co-occurrence/mutual-exclusivity analysis.
        P-value indicates if the pairs are significantly co-occurred or mutually exclusive.
        Co-occurrence: Odds ratio > 1
        Mutual-exclusivity: Odds ratio < 1

    - **input**  
        - `infile:file`: The input file.  

    - **output**  
        - `outfile:file` : The output file containing confInt1, confInt2, oddsRatio, pval, qval, alternative and method.  

    - **args**  
        - `intype`: The type of the input file:  
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
        	#         | S1 | S2 | ... | Sn |
        	# --------+----+----+-----+----+
        	# A       | 1  | 0  | ... | 1  |
        	# B       | 0  | 1  | ... | 0  |
        	# ...     |           ...      |
        	# X       | 0  | 1  | ... | 0  |
        	# --------+----+----+-----+----+
        	#
        	```
        - `padj`: The p-value adjustment method, see `p.adjust.methods` in R. Default: `BH`  

!!! hint "pMediation"

    - **description**  
        Do mediation analysis

    - **input**  
        - `infile:file`: The input file (a matrix or data.frame).  

    - **output**  
        - `outfile:file`: The result file.  

    - **args**  
        - `inopts`: The options for input file.  
        	- `cnames`: Whether the input file has column names
        	- `rnames`: Whether the input file has row names
        - `medopts`: The options for mediation analysis.  
        	- `modelm`: The model for M ~ X. Default: `lm(M ~ X)`
        	- `modely`: The model for Y ~ X + M. Default: `lm(Y ~ X + M)`
        	- `mediator`: Tell the model which column is the mediator
        	- `treat`: Tell the model which column is the variable
        	- `boot`: Use bootstrap?
        	- `sims`: How many time simulations?

!!! hint "pHypergeom"

    - **description**  
        Do hypergeometric test.

    - **input**  
        - `infile:file`: The input file, could be raw data (presence (1) and absence (0) of elements) or number of overlapped elements and elements in each category.  
        	- Set `args.intype` as `raw` if it is raw data. The population size `args.N` is required
        	- Set `args.intype` as `numbers` (or any string except `raw`) if it is numbers. You can specified explicit header: `k` = overlapped elements, `m` = size of set 1, `n` = size of set 2 and `N` = the population size. If `N` not included, then `args.N` is required

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `intype`: the type of input file. Default: `raw`. See `infile:file`  
        - `inopts`: The options for input file.  
        	- `cnames`: Whether the input file has column names
        	- `rnames`: Whether the input file has row names
        - `N`: The population size. Default: `None`  
## tabix

!!! hint "pTabix"

    - **description**  
        Use tabix to extract information.

    - **input**  
        - `infile`: a local or remote file  
        - `region`: a region or a file containing regions  

    - **output**  
        - `outfile:file`: The information extracted from the input file  

    - **args**  
        - `tabix`: The path to `tabix`  
        - `params`: Other params for `tabix`  

!!! hint "pTabixIndex"

    - **description**  
        Generate tabix index file.

    - **input**  
        - `infile:file`: the input file  
        	- Could be bgzipped.

    - **output**  
        - `outfile:file`: The bgzipped file  
        - `outidx:file`: The tabix index file  

    - **args**  
        - `tabix`: The path to `tabix`  
        - `params`: Other params for `tabix`  
        - `python`: Will be used to generate command line arguments.  
## tcga

!!! hint "pDownload"

    - **description**  
        Download TCGA use `gdc-client` and a manifest file

    - **input**  
        - `manifile:file`: the manifest file  

    - **output**  
        - `outdir:file`: the directory containing downloaded file  

    - **args**  
        - `params`: other params for `gdc-client`, default: "--no-related-files --no-file-md5sum -n 20"  
        - `bin-gdc`: the executable file of `gdc-client`, default: "gdc-client"  

!!! hint "pSample2SubmitterID"

    - **description**  
        convert TCGA sample names with submitter id with metadata and sample containing folder

    - **input**  
        - `indir:file`: the directory containing the samples  
        - `mdfile:file`: the metadata file  

    - **output**  
        - `outdir:file`: the directory containing submitter-id named files  

!!! hint "pConvertExpFiles2Matrix"

    - **description**  
        convert TCGA expression files to expression matrix, and convert sample name to submitter id

    - **input**  
        - `dir:file`: the directory containing the samples  
        - `mdfile:file`: the metadata file  

    - **output**  
        - `outfile:file`: the output matrix  

    - **requires**  
        [python-mygene](https://pypi.python.org/pypi/mygene/3.0.0)

!!! hint "pConvertMutFiles2Matrix"

    - **description**  
        convert TCGA mutation files (vcf.gz) to mut matrix, and convert sample name to submitter id

    - **input**  
        - `dir:file`: the directory containing the samples  
        - `mdfile:file`: the metadata file  

    - **output**  
        - `outfile:file`: the output matrix  
## tfbs

!!! hint "pMotifScan"

    - **description**  
        Scan motif along the given sequences.

    - **input**  
        - `tffile:file`: The infile containing TF name and motif name.  
        	- If only one column is give, will be used as both TF and motif name
        	- If there are 2 columns, 1st column will be motif name, 2nd column will be TF name
        - `sfile:file`: The sequence file  

    - **output**  
        - `outdir:file`: The output dir  

    - **args**  
        - `tools`   : The tool used to scan the motif. Default: 'meme'  
        - `meme`    : The path of MEME's fimo. Default: 'fimo'  
        `motifs   : The motif database in MEME format.
        - `pval`    : The pvalue cutoff. Default: 1e-4  
        - `cleanmname`: Whether to clean motif name. Default: True  
        - `ucsclink`: The ucsc link template. Default: `https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&position={}`  
        - `nthread` : Number of threads used to scan, only available when you have multiple mids. Default: 1  
        - `params`  : Other parameters for `fimo`  

    - **requires**  
        [`fimo` from MEME Suite](http://meme-suite.org/tools/fimo)
## tsv

!!! hint "pMatrixR"

    - **description**  
        Operate a matrix and save the new matrix to file.

    - **input**  
        - `infile:file`: The input file containing the matrix  

    - **output**  
        - `outfile:file`: The output matrix  

    - **args**  
        - `cnames`: Whether the input file has cnames. Default: True  
        - `rnames  `: Whether the input file has rnames  . Default: 1  
        - `code`: The R code to operating the matrix. (the matrix is read in variable `mat`)  

!!! hint "pCbind"

    - **description**  
        Cbind the rest of files to the first file.

    - **input**  
        - `infiles:files`: The input files  

    - **output**  
        - `outfile:file`: The output matrix  

    - **args**  
        - `cnames`: Whether the input file has cnames. Default: True  
        	- or [True, True, False] corresponding to the file order
        - `rnames  `: Whether the input file has rnames  . Default: 1  
        - `miss`: Replacement for missing values. Default: `NA`  

!!! hint "pRbind"

    - **description**  
        Rbind the rest of files to the first file.

    - **input**  
        - `infiles:files`: The input files  

    - **output**  
        - `outfile:file`: The output matrix  

    - **args**  
        - `cnames`: Whether the input file has cnames. Default: True  
        	- or [True, True, False] corresponding to the file order
        - `rnames  `: Whether the input file has rnames  . Default: 1  
        - `miss`: Replacement for missing values. Default: `NA`  

!!! hint "pCsplit"

    - **description**  
        Split a matrix by columns and save them into files.

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outdir:dir`: The directory containing the output column files  

    - **args**  
        - `cnames`: Whether the input file has cnames. Default: True  
        	- or [True, True, False] corresponding to the file order
        - `rnames  `: Whether the input file has rnames  . Default: 1  

!!! hint "pRsplit"

    - **description**  
        Split a matrix by rows and save them into files.

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outdir:dir`: The directory containing the output row files  

    - **args**  
        - `cnames`: Whether the input file has cnames. Default: True  
        	- or [True, True, False] corresponding to the file order
        - `rnames  `: Whether the input file has rnames  . Default: 1  

!!! hint "pTsv"

    - **description**  
        Read, Transform, filter a TSV file.

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `inopts`: The input options for infile:  
        	- `delimit`: The delimit. Default: `\\t`
        	- `comment`: The comment sign. Default: `#`
        	- `skip`: First N lines to skip. Default: `0`
        	- `ftype`: The file type. Metadata can be assigned direct (list/OrderedDict). If not specified, metadata will be generated automatically.
        - `outopts`: The output options for outfile:  
        	- `delimit`: The delimit for records. Default: `\\t`
        	- `head`: Output header or not. Default: `False`
        	- `headDelimit`: The delimit for header. Default: `\\t`
        	- `headPrefix`: The prefix for header. Default: ``
        	- `headTransform`: The transformer for header. Default: `None`
        	- `ftype`: The file type. Metadata can be assigned direct (list/OrderedDict, '+' as an element or key is allowed to indicate extra meta from the reader). If not specified, metadata will be borrowed from the reader. 
        - `ops`: A ops function to transform the row. Argument is an instance of `readRecord`  
        - `opshelper`: A helper function for `args.ops`  

!!! hint "pSimRead"

    - **description**  
        Read files simultaneously.
        NOTE: only one file allows multiple lines with same value to compare, and that file should be the first one. For example: 
        ```
        File1:
        1	1
        1	2
        1	3
        File2:
        1	1
        2	2
        3	3
        ```
        If you compare the first column, File1 has to put at the begining for input.

    - **input**  
        - `infiles:files`: The input files  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `skip`: argument skip for each file  
        - `delimit`: argument delimit for each file  
        - `usehead`: The header from which input file will be used for output file.  
        	- Default: None (Don't write header)
        - `gzip`: argument gzip for each file  
        - `match`: The match function.   
        - `do`: The do function. Global vaiable `fout` is available to write results to output file.  

    - **requires**  
        [`python-simread`](https://github.com/pwwang/simread)
## utils
## vcf

!!! hint "pVcfFilter"

    - **description**  
        Filter records in vcf file.

    - **input**  
        - `infile:file`: The input file  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `filters`: The filters, should be a string of lambda function:  
        	```
        	"lambda record, samples: <expression>"
        	* ``record.CHROM`` : 'chr20'
        	* ``record.POS``   : 1234567
        	* ``record.ID``    : 'microsat1'
        	* ``record.REF``   : ''GTC''
        	* ``record.ALT``   : [G, GTCT]
        	* ``record.QUAL``  : 50
        	* ``record.FILTER``: ['PASS'] # NO!, PASS should be []
        	* ``record.INFO``  : {'AA': 'G', 'NS': 3, 'DP': 9}
        	* samples = record.samples
        	* len(samples): 3
        	* samples[0].sample: 'NA00001'
        	* samples[0]: Call(sample=NA00001, CallData(GT=0/1, GQ=35, DP=4))
        	* samples[0].data: calldata(GT='0/1', GQ=35, DP=4)
        	* samples[0].data.GT: '0/1'
        	```
        	- see here for record and samples: https://github.com/jamescasbon/PyVCF
        	- Remember if filters() returns True, record remained.
        - `gz`     : Whether to gzip the output file. Default: False  
        - `keep`   : Whether to keep the filtered records. Default: True. (only for gatk, snpsift at filter step)  

    - **requires**  
        [`pyvcf`](https://github.com/jamescasbon/PyVCF)

!!! hint "pVcf"

    - **description**  
        Use pyvcf to manipulate vcf file

    - **input**  
        - `infile:file`: The input vcf file  

    - **output**  
        - `outfile:file`: The output vcf file  

    - **args**  
        - `helper`: The helper code injected to script  
        	- Since lambda function can't do assignment and manipulation so you can write some help function here
        - `readerops`: A lambda function (must be quoted) to manipulate the reader (vcf.Reader instance)  
        - `recordops`: A lambda function (must be quoted) to manipulate the record (vcf.Record instance)  
        - `gz`: Gzip the ouput file  

!!! hint "pVcfAnno"

    - **description**  
        Annotate the variants in vcf file.
        You have to prepare the databases for each tool.

    - **input**  
        - `infile:file`: The input vcf file  

    - **output**  
        - `outfile:file`: The output file (output file of annovar will also be converted to vcf)  
        - `outdir`: The output directory, used to fetch some stat/summary files  

    - **args**  
        - `tool`: The tool used to do annotation. Default: snpeff  
        - `snpeff`: The path of snpeff. Default: snpEff  
        - `vep`: The path to vep. Default: vep  
        - `gz`: Whether to gzip the result file. Default: False  
        - `annovar`: The path of annovar. Default: annotate_variation.pl  
        - `annovar_convert`: The path of convert2annovar.pl, used to convert vcf to annovar input file. Default: convert2annovar.pl  
        - `genome`: The genome for annotation. Default: hg19  
        - `tmpdir`: The tmpdir, mainly used by snpeff. Default: <system tmpdir>  
        - `dbpath`: The path of database for each tool. Required by 'annovar' and 'vep'  
        - `params`: Other params for tool. Default: ''  
        - `snpeffStats`: Whether to generate stats file when use snpeff. Default: False  
        - `mem`: The memory used by snpeff. Default: '4G'  

    - **requires**  
        [`annovar`](http://doc-openbio.readthedocs.io/projects/annovar/en/latest/)
        [`snpeff`](http://snpeff.sourceforge.net/SnpEff_manual.html#intro)
        [`vep`](http://www.ensembl.org/info/docs/tools/vep/script/vep_tutorial.html)

!!! hint "pVcfSplit"

    - **description**  
        Split multi-sample Vcf to single-sample Vcf files.

    - **input**  
        - `infile:file`: The input vcf file  
        - `samples`: The samples, if not provided, will extract all samples  

    - **output**  
        - `outdir:dir`: The output directory containing the extracted vcfs  

    - **args**  
        - `tool`: The tool used to do extraction. Default: vcftools  
        - `vcftools`: The path of vcftools' vcf-subset  
        - `bcftools`: The path of bcftools, used to extract the sample names from input vcf file.  
        - `gatk`: The path of gatk.  

!!! hint "pVcfMerge"

    - **description**  
        Merge single-sample Vcf files to multi-sample Vcf file.

    - **input**  
        - `infiles:files`: The input vcf files  
        - `outfile:dir`: The output multi-sample vcf.  

    - **args**  
        - `tool`: The tool used to do extraction. Default: vcftools  
        - `vcftools`: The path of vcftools' vcf-subset  
        - `bcftools`: The path of bcftools, used to extract the sample names from input vcf file.  
        - `gatk`: The path of gatk.  

!!! hint "pVcf2Maf"

    - **description**  
        Convert Vcf file to Maf file

    - **input**  
        - `infile:file` : The input vcf file  
        	- see `args.somatic`

    - **output**  
        - `outfile:file`: The output maf file  

    - **args**  
        - `tool`     : Which tool to use. Default: vcf2maf  
        - `vcf2maf`  : The path of vcf2maf.pl  
        - `vep`      : The path of vep  
        - `vepDb`    : The path of database for vep  
        - `filtervcf`: The filter vcf. Something like: ExAC_nonTCGA.r0.3.1.sites.vep.vcf.gz  
        - `ref`      : The reference genome  
        - `nthread`  : Number of threads used to extract samples. Default: 1  
        - `tumor1st` : Whether tumor sample comes first. Default: `True`  
        - `bcftools` : Path to bcftools used to extract sample names.  
        - `vcftools` : Path to vcftools used to split vcf.  
        - `samfunc`  : A lambda function used to deduce sample names from file name.  
        - `somatic`  : Whether input vcf file is a somatic mutation file. Default: False  
        	- somatic mutation vcf file can only have one sample TUMOR, or two samples, TUMOR and NORMAL, but will be considered as single sample.
        	- otherwise, multiple samples are supported in the input vcf file. Tumor id will be sample name for each sample, normal id will be NORMAL.

!!! hint "pVcf2GTMat"

    - **description**  
        Convert Vcf file to genotype matrix.
## vcfnext

!!! hint "pVcfStatsPlot"

    - **description**  
        Convert csvstat file from snpEff to R-readable matrix and plot them.

    - **input**  
        - `indir:file`: The directory containing the csv stat files from `snpEff ann`  

    - **output**  
        - `outdir:dir`: The output directory  

    - **args**  
        - `chroms`: The chromsome filter. Default: "" (all chroms)  
        - Note: snpEff csvstat file has no "chr" prefix

!!! hint "pCallRate"

    - **description**  
        Calculate sample/snp call rate from single sample vcfs

    - **input**  
        - `indir:file`: The dir containing the vcfs  

    - **output**  
        - `outsample:file`: The report of call rate for each sample  
        - `figsample:file`: The bar chat of sample call rates  
        - `outsnp:file`: The report of call rate for each snp  
        - `figsnp:file`: The bar chat of snp call rates  

!!! hint "pCepip"

    - **description**  
        Run CEPIP.

    - **input**  
        - `infile:file`: The input file (vcf or avinput)  

    - **output**  
        - `outfile:file`: The cepip result file  

    - **args**  
        - `cepip`: The path of cepip  
        - `cell` : The related cell line  
        - `params`: Other params for cepip  

    - **requires**  
        [`cepip`](http://jjwanglab.org/cepip/)

!!! hint "pMutSig"

    - **description**  
        MutSig stands for "Mutation Significance".  MutSig analyzes lists of mutations discovered in DNA sequencing, to identify genes that were mutated more often than expected by chance given background mutation processes.
        For more information, see Lawrence, M. et al. Mutational heterogeneity in cancer and the search for new cancer-associated genes. Nature 499, 214-218 (2013).
        
        See [dcumentation](http://archive.broadinstitute.org/cancer/cga/mutsig_run)

    - **input**  
        - `infile:file`: mutation table  

    - **output**  
        - `outdir:dir`: The output directory  

    - **args**  
        - `mutsig` : The path to `run_MutSigCV.sh`, default: 'mutsig'  
        - `mcr`    : The Matlab MCR path  
        - `cvrg`   : coverage table  
        - `cvrt`   : covariates table  
        - `mutdict`: mutation_type_dictionary_file  
        - `chrdir` : chr_files_hg18 or chr_files_hg19  

    - **requires**  
        [MutSig](http://archive.broadinstitute.org/cancer/cga/mutsig_download)

!!! hint "pMafMerge"

    - **description**  
        Merge maf files.

    - **input**  
        - `indir:dir`: The directory containing the maf files  

    - **output**  
        - `outfile:file`: The merged maf file  

    - **args**  
        - `excols`: How to deal with extra columns other than 34 standard columns from TCGA.  
        	- merge(default): Merge the columns, if one not exists, fill with an empty string.
        	- discard: Just discard the extra columns, with only 34 columns left. So you can also put just one maf file in the indir with some columns missed to fill it with standard columns.

!!! hint "pMaftools"

    - **description**  
        Use maftools to draw plots.

    - **args**  
        - `ngenes`:   

    - **requires**  
        [``]
## web

!!! hint "pDownloadForm"

    - **description**  
        Download results by submitting a form, supporting pagination.

    - **input**  
        - `url`   : the URL contains the form  
        - `data`  : the data used to fill the form (JSON string or transformed from dict by json.dumps).  
        - `submit`: the submit button to submit the form (use Xpath).  
        - `next`  : the button for next page (use Xpath)  

    - **output**  
        - `outdir:file`: The directory saves the results  

    - **args**  
        - `interval`: seconds to wait between fetching each page. Default: 1  

    - **requires**  
        [`Splinter`](https://splinter.readthedocs.io/en/latest/index.html)
        [`Phantomjs`](http://phantomjs.org/)

!!! hint "pDownloadGet"

    - **description**  
        Download results by urls.

    - **input**  
        - `url`: the URLs to download  

    - **output**  
        - `outfile:file`: The output file  

!!! hint "pDownload"

    - **description**  
        Alias of `pDownloadGet`

!!! hint "pDownloadPost"

    - **description**  
        Download results by POST.

    - **input**  
        - `url` : the URLs to download  
        - `data`: the POST data.  

    - **output**  
        - `outfile:file`: The output file  
## wxs
## wxsanno

!!! hint "pSnpEff"

    - **description**  
        This is the default command. It is used for annotating variant filed (e.g. VCF files).

    - **input**  
        - `infile:file`: The input file   

    - **output**  
        - `outdir:file`: The directory containing output anntated file, snpEff_genes.txt and snpEff_summary.html  

    - **args**  
        - `snpEff`: The snpEff executable, default: "snpEff"  
        - `params`: Other parameters for `snpEff`, default: "-Xms1g -Xmx4g -v"  
        - `genome`: The genome used for annotation, default: "hg19"  
        - `informat`: The format of input file [vcf or bed], default: "vcf"  
        - `outformat`: The format of output file [vcf, gatk, bed, bedAnn], default: "vcf"  
        - `csvStats`: Whether to generate csv stats file, default: True.  
        - `htmlStats`: Whether to generate the html summary file, default: False.  
        - `javamem`: The memory to use. Default: '-Xms1g -Xmx8g'  

    - **requires**  
        [snpEff](http://snpeff.sourceforge.net/SnpEff_manual.html)
## wxscall

!!! hint "pCNVnator"

    - **description**  
        Use `CNVnator` to call CNVs from bam file

    - **input**  
        - `infile:file`: The bam file   

    - **output**  
        - `outfile:file`: The vcf file  

    - **args**  
        - `cnvnator`: The CNVnator executable, default: "cnvnator"  
        - `cnv2vcf`: The converter executable to convert CNVnator results to vcf, default: "cnvnator2VCF.pl"  
        - `binsize`: The bin_size, default: 100  
        - `genome`: The genome: default: hg19  
        - `chrom`: Chromosome names, default: "" (all chromosomes)  
        - `chrdir`: The dir contains reference sequence of chromosomes, default: "" (don't specify)  
        

    - **requires**  
        [CNVnator](https://github.com/abyzovlab/CNVnator)
## wxsdown

!!! hint "pMutSig"

    - **description**  
        MutSig stands for "Mutation Significance".  MutSig analyzes lists of mutations discovered in DNA sequencing, to identify genes that were mutated more often than expected by chance given background mutation processes.
        
        For more information, see Lawrence, M. et al. Mutational heterogeneity in cancer and the search for new cancer-associated genes. Nature 499, 214-218 (2013).
        
        See [dcumentation](http://archive.broadinstitute.org/cancer/cga/mutsig_run)

    - **input**  
        - `maffile:file`: mutation table  
        - `cvgfile:file`: coverage table  
        - `cvrfile:file`: covariates table  
        - `mutdict:file`: mutation_type_dictionary_file  
        - `chrdir:file`: chr_files_hg18 or chr_files_hg19   

    - **output**  
        - `outdir:dir`: The output directory  

    - **args**  
        - `mutsig`: The path to `run_MutSigCV.sh`, default: 'mutsig'  
        - `mcr`: The Matlab MCR path  

    - **requires**  
        [MutSing](http://archive.broadinstitute.org/cancer/cga/mutsig_download)

!!! hint "pVcf2Maf"

    - **description**  
        Convert a snpEff-annotated somatic mutation vcf file (with normal and tumor samples) to [maf](https://wiki.nci.nih.gov/display/TCGA/Mutation+Annotation+Format+(MAF)+Specification) file

    - **input**  
        - `infile:file`: vcf file  

    - **output**  
        - `outfile:file`: The maf file  

    - **args**  
           `vepdata`: The path of vep data. Default: "" (default data dir of vep)
           `vep`: The path of vep excutable. Default: "vep"
           `vcf2maf`: The path of vcf2maf excutable. Default: "vcf2maf.pl"
           `reffile`: The reference fasta file.
           `nthread`: The number of threads used by vep. Default: 1
           `filtervcf`: The filter vcf
        - `params`: Other parameters for `vcf2maf.pl`, default: ""  

    - **requires**  
        [vcf2maf.py](https://github.com/mskcc/vcf2maf)

!!! hint "pMergeMafs"

    - **description**  
        Merge MAF files

    - **input**  
        - `indir:file`: The directory containing MAF files to be merged  

    - **output**  
        - `outfile:file`: The merged MAF file  

!!! hint "pMutsig4Plot"

    - **description**  
        Prepare somatic mutations for  plotting

    - **input**  
        - `msdir:file`: The mutsig output directory  

    - **output**  
        - `outfile:file`: The file for plotting  
        ```
        #PANEL: Somatic mutations
        #INFO: MT|PI
        #DESC: Mutation type|Putative impact
        # could also be bordercolor, you can have up to 4 shape features
        #TYPE: shape|bgcolor
        # could also be continuous
        # expressions for set: a,b,c
        #                 norminal: no
        #                 continuous: [0,1]
        #DATA: set|norminal
        #NCOL: 2|2
        #NAME_MT: Frameshift|Missense|Nonsense|Silent|Splice_site|TSS|Nonstop
        #NAME_PI: HIGH|MODERATE|LOW|MODIFIER
        #VALUE_MT: 0|1|20|13|4|17|14
        #EXP_MT: frameshift_variant,inframe_deletion,inframe_insertion|missense_variant,initiator_codon_variant,stop_retained_variant,rare_amino_acid_variant|stop_gained|synonymous_variant|splice_acceptor_variant,splice_donor_variant|start_lost,start_retained|stop_lost
        #
        Sample1	Sample2	Sample3	Sample4	Sample5
        ABC	missense_variant|HIGH	missense_variant|HIGH	...
        ...
        ```

    - **args**  
        - `topn`: the cutoff to select genes. If it is >= 1, top N genes will be selected, otherwise, it will be used as pvalue cutoff. Default: .05  

    - **requires**  
        [`pyvcf`](https://github.com/jamescasbon/PyVCF)

!!! hint "pMutPlot"

    - **description**  
        Plot mutations
        ```
        |           |             |           |           |---
        |- ftWidth -|  s   s   s  |- pnWidth -|- lgWidth -| snHeight
        |           |             |           |           |---
            feature1
        	feature2
        ```

    - **input**  
        - `indir:file`: The input directory containing plot files  

    - **output**  
        - `outfile:file`: The plot png file  

!!! hint "pCepip"

    - **description**  
        run CEPIP.

    - **input**  
        - `avinput:file`: The avinput file  
        - `cell`: The cell  

    - **output**  
        - `outfile:file`: The cepip result file  

    - **args**  
        - `bin-cepip`: The jar file path of cepip, default: /data2/junwenwang/shared/tools/cepip/cepip.jar  

    - **requires**  
        [`cepip`](http://jjwanglab.org/cepip/)
## wxsprep

!!! hint "pTrimmomaticPE"

    - **description**  
        Trimming Illumina NGS paired-end data

    - **input**  
        - `fqfile1:file`: The 1st fastq file (could be in .gz format)  
        - `fqfile2:file`: The 2nd fastq file  

    - **output**  
        - `outfile1:file`: The 1st output file  
        - `outfile2:file`: The 2nd output file  

    - **args**  
        - `trimmomatic`: The trimmomatic executable, default: "trimmomatic"  
        - `phred`: "phred33" (default) or "phred64"  
        - `params`: Other params for trimmomatric, default: "ILLUMINACLIP:{adapter}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"  
        	- have to replace `{adapter}` with the path of the adapter file
        - `nthread`: 1  

    - **requires**  
        [trimmomatic](http://www.usadellab.org/cms/index.php?page=trimmomatic)

!!! hint "pTrimmomaticSE"

    - **description**  
        Trimming Illumina NGS single-end data

    - **input**  
        - `fqfile:file`: The fastq file (could be in .gz format)  

    - **output**  
        - `outfile:file`: The output file  

    - **args**  
        - `trimmomatic`: The trimmomatic executable, default: "trimmomatic"  
        - `phred`: "phred33" (default) or "phred64"  
        - `params`: Other params for trimmomatric, default: "ILLUMINACLIP:{adapter}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"  
        	- have to replace `{adapter}` with the path of the adapter file
        - `nthread`: 1  

    - **requires**  
        [trimmomatic](http://www.usadellab.org/cms/index.php?page=trimmomatic)

!!! hint "pAlignPEByBWA"

    - **description**  
        Align paired-end reads to reference genome using bwa mem

    - **input**  
        - `infile1:file`: read file 1 (fastq, or fastq gzipped)  
        - `infile2:file`: read file 2 (fastq, or fastq gzipped)  
        - `reffile:file`: The reference file  

    - **output**  
        - `outfile:file`: The output sam file  

    - **args**  
        - `bwa`: The bwa executable, default: bwa  
        - `params`: Other params for bwa mem, default: "-M"  
        - `nthread`: 1  

    - **requires**  
        [bwa](https://github.com/lh3/bwa)

!!! hint "pAlignSEByBWA"

    - **description**  
        Align paired-end reads to reference genome using bwa mem

    - **input**  
        - `infile:file`: read file (fastq, or fastq gzipped)  
        - `reffile:file`: The reference file  

    - **brings**  
        - `reffile#bwt`: "{{reffile | bn}}.bwt",   
        - `reffile#sa`: "{{reffile | bn}}.sa",  
        - `reffile#ann`: "{{reffile | bn}}.ann",  
        - `reffile#amb`: "{{reffile | bn}}.amb",  
        - `reffile#pac`: "{{reffile | bn}}.pac"  

    - **output**  
        - `outfile:file`: The output sam file  

    - **args**  
        - `bwa`: The bwa executable, default: bwa  
        - `params`: Other params for bwa mem, default: "-M"  
        - `nthread`: 1  
        - `reffile`: The reference file, required  

    - **requires**  
        [bwa](https://github.com/lh3/bwa)

!!! hint "pAlignPEByNGM"

    - **description**  
        Align paired-end reads to reference genome using NextGenMap

    - **input**  
        - `infile1:file`: read file 1 (fastq, or fastq gzipped)  
        - `infile2:file`: read file 2 (fastq, or fastq gzipped)  
        - `reffile:file`: The reference file  

    - **output**  
        - `outfile:file`: The output sam/bam file  

    - **args**  
        - `ngm`: The NextGenMap executable, default: ngm  
        - `nthread`: 1  
        - `outtype`: sam or bam, default: sam (only sam for now, due to bug of ngm 0.5.3 (fixed in 0.5.4))  
        - `params`: Other params for ngm, default: "--rg-id ngm --rg-sm sample"  

    - **requires**  
        [NextGenMap](https://github.com/Cibiv/NextGenMap/wiki)

!!! hint "pAlignSEByNGM"

    - **description**  
        Align single-end reads to reference genome using NextGenMap

    - **input**  
        - `infile1:file`: read file 1 (fastq, or fastq gzipped)  
        - `infile2:file`: read file 2 (fastq, or fastq gzipped)  
        - `reffile:file`: The reference file  

    - **output**  
        - `outfile:file`: The output sam/bam file  

    - **args**  
        - `ngm`: The NextGenMap executable, default: ngm  
        - `nthread`: 1  
        - `outtype`: sam or bam, default: sam (only sam for now, due to bug of ngm 0.5.3 (fixed in 0.5.4))  
        - `params`: Other params for ngm, default: "--rg-id ngm --rg-sm sample"  

    - **requires**  
        [NextGenMap](https://github.com/Cibiv/NextGenMap/wiki)

!!! hint "pMergeBams"

    - **description**  
        Merge bam files

    - **input**  
        - `bamdir:dir`: the dir containing bam files   

    - **output**  
        - `outfile:file`: the merged bam file  

    - **args**  
        - `samtools`: the executable path of samtools, default: "samtools"  
        - `nthread`: Number of BAM/CRAM compression threads  
        - `params`: Other parameters for `samtools merge`, default: ""  

    - **requires**  
        [samtools](http://www.htslib.org/)
## wxsstat

!!! hint "pVcf2List"

    - **description**  
        Convert vcf to stat files for pCallRate

    - **input**  
        - `vcffile:file`: The vcf file  

    - **output**  
        - `outfile:file`: The stat file  

    - **args**  
        - `chroms`: SNPs on chromosomes to consider, default: "" (all chroms)  
        - use "chr1-22, chrX, chrY" for chr1 to chr22, chrX and chrY

    - **requires**  
        [`pyvcf`](https://github.com/jamescasbon/PyVCF)

!!! hint "pCallRate"

    - **description**  
        Calculate sample/snp call rate from a matrix of snp-sample
        - rows are snps, columns are samples

    - **input**  
        - `infile:file`: The snp-sample matrix file  

    - **output**  
        - `outsample:file`: The report of call rate for each sample  
        - `figsample:file`: The bar chat of sample call rates  
        - `outsnp:file`: The report of call rate for each snp  
        - `figsnp:file`: The bar chat of snp call rates  

!!! hint "pCoverageByBamstats"

    - **description**  
        Use `bamstats` to calculate coverage for bam file

    - **input**  
        - `infile:file`: The bam file  

    - **output**  
        - `outfile:file`: The report of coverage for the bam file  

    - **args**  
        - `bin`: The `bamstats` executable, default: "bamstats"  
        - `params`: Other parameters for `bamstats`, default: ""  

    - **requires**  
        [bamstats](http://bamstats.sourceforge.net/)

!!! hint "pPlotBamstats"

    - **description**  
        Plot coverage use output files generated by `bamstats` or `wxs.pCoverageByBamstats`

    - **input**  
        - `indir:file`: The directory containing bamstats output files  

    - **args**  
        - `chroms`: Chromosomes to plot. Default: "" (all chroms)  
        - Note: Whether to have "chr" prefix or not depends on your reference when mapping.
        - You can do a scope assignment: "chr1-chr22, chrX, chrY"

    - **output**  
        - `outdir:file`: The directory containing output figures  

!!! hint "pSnpEff2Stat"

    - **description**  
        Convert csvstat file from snpEff to R-readable matrix for plotting

    - **input**  
        - `indir:file`: The directory containing the csv stat files from `snpEff ann`  

    - **output**  
        - `outdir:dir`: The output directory  

    - **args**  
        - `chroms`: The chromsome filter. Default: "" (all chroms)  
        - Note: snpEff csvstat file has no "chr" prefix

!!! hint "pPlotSnpEff"

    - **description**  
        Plot snpEff annotation statistics

    - **input**  
        - `indir:file`: The snpEff result directory containing matrix files generated by pSnpEff2Stat  

    - **output**  
        - `outdir:dir`: The output directory  

    - **requires**  
        [`pwwang/corrplot`](https://github.com/pwwang/corrplot)
        - use `library(devtools); install.github("pwwang/corrplot")`
        [`ggplot2`](http://ggplot2.org/)