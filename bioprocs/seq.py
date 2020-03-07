"""Processes related to DNA/protein sequences"""
from diot import Diot
from . import params, proc_factory

# pylint: disable=invalid-name

pConsvPerm = proc_factory(
    desc='Generate a null distribution of conservation scores.',
    config=Diot(annotate="""
    @name:
        pConsvPerm
    @description:
        Generate a null distribution of conservation scores.
    @input:
        `seed`: The seed to generate the random regions. Default: None
    @output:
        `outfile:file`: A file with mean conservation scores sorted descendingly.
    @args:
        `len`: The length of a random region. Default: 50
        `nperm`: Number of permutations. Default: 1000
        `gsize`: The chrom size file.
        `bedtools`: The path of bedtools.
        `bwtool`: The path of bwtool.
        `consvdir`: The directory containing bigwig files of conservation scores
            - The bigwig file should start with chr name: chrN.*
    @requires:
        [bwtool](https://github.com/CRG-Barcelona/bwtool)
        [bedtools](http://bedtools.readthedocs.io/en/latest/content/bedtools-suite.html)
    """),
    input='seed',
    output='outfile:file:consv-len{{args.len}}-nperm{{\
            args.nperm}}-{{i.seed}}.txt',
    lang=params.python.value,
    args=Diot(
        len=50,
        nperm=1000,
        consvdir=params.consvdir.value,
        gsize=params.gsize.value,
        bedtools=params.bedtools.value,
        bwtool=params.bwtool.value,
        seed=None,
    )
)

pConsv = proc_factory(
    desc='Get the conservation scores of regions.',
    config=Diot(annotate="""
    @name:
        pConsv
    @description:
        Get the conservation scores of regions.
        It uses wigFix to find the conservation scores.
        But first you have to convert those wigFix.gz files to bigWig files using ucsc-wigToBigWig
    @input:
        `bedfile:file`: The bedfile with regions in the same chromosome
        `permfile:file`:The permutaiton file generated by `pConsvPerm`, used to calculate p-values
    @output:
        `outfile:file`: The output file
    @args:
        `consvdir`:   The bigwig directory, the bigwig files must be named as "chrN.*.bw"
            - For example: `chr1.phyloP30way.bw`
        `bwtool`:   The path of bwtool executable. Default: `bwtool`
        `bedtools`: The path of bedtools executable. Default: `bedtools`
        `pval`:     Whether calculate pvalue of each region. Default: False
            - In this case, the `i.permfile` can be ignored.
    @requires:
        [bwtool](https://github.com/CRG-Barcelona/bwtool)
        [bedtools](http://bedtools.readthedocs.io/en/latest/content/bedtools-suite.html)
    """),
    input="bedfile:file, permfile:file",
    output="outfile:file:{{i.bedfile | fn}}-consv.bed",
    lang=params.python.value,
    args=Diot(
        bwtool=params.bwtool.value,
        consvdir=params.consvdir.value,
        pval=False,
    )
)

pPromoters = proc_factory(
    desc=('Get the promoter regions in bed format of '
          'a gene list give in infile.'),
    config=Diot(annotate="""
    @name:
        pPromoters
    @description:
        Get the promoter regions in bed format of a gene list give in infile.
        Gene names are supposed to be normalized by `gene.pGeneNameNorm`
    @input:
        `infile:file`: the gene list file
    @output:
        `outfile:file`: the bed file containing the promoter region
    @args:
        `region`: The region to output. Default: `Diot(up = 2000, down = None, withbody = False)`
            - `up`: The upstream distance to TSS.
            - `down`: The downstream distance to TSS. Defaults to `args.region.up` if `None`
            - `withbody`: Include gene body in the output region? Default: `False`
        base: Whether the output BED file is 0-based or 1-based
        `notfound`: How to deal with records can't be found. Default: `skip`
            - `skip` : Skip the record
            - `error`: Report error and exit
        `refgene`: The ref gene file. Default: `@params.refgene`
        `inopts` : The options for input file. Default: `Diot(cnames = False, genecol = 0, delimit = "\t")`
            - `cnames`: Whether the input file has header
            - `genecol`: The 0-based index or the colname of gene column.
            - `delimit`: The delimit of the input file.
        `outopts`:  The options for output file. Default: `Diot(cnames = False)`
    """),
    input="infile:file",
    output="outfile:file:{{i.infile | fn}}-promoters.bed",
    lang=params.python.value,
    args=Diot(
        region=Diot(up=2000, down=None, withbody=False),
        notfound='skip',  # error,
        inopts=Diot(cnames=False, delimit="\t"),
        base=0,
        genecol=0,
        refgene=params.refgene.value,
    )
)

pSeqMutate = proc_factory(
    desc='Mutate sequence with point mutations',
    config=Diot(annotate="""
                @input:
                    fafile: The input sequence file in fasta
                        - Coordinate offset supported. You can specify "chr1:1000" as
                          sequence name, denoting the start position of the given sequence
                        - It can be 0- or 1-based, indicating by `args.seqbase`
                        - "Gene::chr1:1000-2000" (used by bedtools getfasta) also supported
                    mutfile: The mutation file in BED6+ format
                        - The coordinates should be 1-based
                        - 7th col: the reference allele
                        - 8th col: the alternate allele
                @output:
                    outfile: The output sequence file
                @args:
                    nthread (int): Number of threads to use
                    seqbase (int): The base of the coordinate in `i.fafile`
                """),
    input='fafile:file,mutfile:file',
    output='outfile:file:{{i.fafile | stem2}}.mutated.fa',
    lang=params.python.value,
    args=Diot(nthread=1, seqbase=0)
)
