#!/usr/bin/env python
"""Call mutatoins from 2nd-gen sequencing data"""

from os import path
from pyppl import PyPPL, Channel
from pyppl.logger import logger
from diot import Diot
from bioprocs import params

params.intype = 'bam'  # ebam, fastq
params.intype.desc = [
    'The input file types. Either bam, ebam or fastq.',
    'Ebam means the bam files need to reformatted into fastq files.'
]
params.muts = ['germ']  # or ['germ', 'soma', 'scnv', 'gcnv']
params.muts.type = list
params.muts.desc = [
    'What kind of mutations to call.',
    'Note: soma need paired information'
]
params.indir.required = True
params.indir.desc = 'The input directory containing input files.'
params.indir.callback = lambda opt: opt.set_value(path.realpath(opt.value))
params.aligner = 'bwa'
params.aligner.desc = 'The alignment tool.'
params.trimmer = 'trimmomatic'
params.trimmer.desc = 'The trimming tool.'
params.saminfo.required = True
params.saminfo.desc = """The sample information file:
Column 1: the basename of the sample file in '-indir'
Column 2: Group if '-muts' includes 'soma', basically, 'TUMOR' and 'NORMAL'
Column 3: Patient if multiple samples belong to the same patient.
Example:
```
Sample    Group    Patient
A1.bam    TUMOR    A
A2.bam    NORMAL   A
B1.bam    TUMOR    A
B2.bam    NORMAL   A
```
"""
params.nthread = 1
params.nthread.desc = 'Use multithreading if possible.'
params.outdir.required = True
params.outdir.desc = 'Where to export the result files.'
params.runner = 'local'
params.runner.desc = 'The runner to run the processes.'
params.forks = 1
params.forks.desc = 'How many jobs to run simultanuously.'
params.errhow = 'terminate'
params.errhow.desc = 'What to do if error happens. retry, terminate or halt.'
params.logfile = ''
params.logfile.desc = 'Where to save the logs.'
params.loglevel = 'info'
params.loglevel.desc = 'The logging level.'
params.compress = True
params.compress.desc = 'Use gzip and bam file to save space.'
params.ppldir = './workdir'
params.ppldir.desc = 'The pipeline directory.'
params.flowchart.desc = 'The flowchart file'
params.forcecache = True
params.forcecache.desc = ('Force processes to cache '
                          'if they had successful run before.')

def main(): # pylint: disable=too-many-statements,assigning-non-slot
    """The main entry point of the pipeline"""
    opts = params._parse(dict_wrapper=Diot)

    from bioprocs.common import pFiles2Dir
    from bioprocs.sambam import pBam2Gmut, pBamPair2Smut
    from bioprocs.utils.sampleinfo import SampleInfo2 as SampleInfo
    from bioprocs.sets.wxs import aPrepareBam, aBam2SCNV, aBam2GCNV

    starts = []
    saminfo = SampleInfo(opts.saminfo)
    aPrepareBam.pFastq2Sam.args.tool = opts.aligner
    aPrepareBam.pFastqTrim.args.tool = opts.trimmer
    aPrepareBam.args.nthread = opts.nthread

    if (aPrepareBam.pSam2Bam.args.tool == 'elprep' and
            aPrepareBam.pSam2Bam.args.steps.recal):
        aPrepareBam.modules.norecal()
    if opts.compress:
        aPrepareBam.args.gz = True
        aPrepareBam.pFastq2Sam.args.outfmt = 'bam'

    pBamDir = pFiles2Dir # pylint: disable=invalid-name
    pBamDir.runner = 'local'
    if opts.intype == 'ebam':
        logger.title(
            'Mutcall: External BAMs received, try to refactorize them.'
        )
        #aPrepareBam.input = [
        #   Channel.fromPattern(path.join(opts.indir, '*.bam'))]
        aPrepareBam.modules.ebam(restore=False)
        aPrepareBam.input = Channel.create(saminfo.toChannel(
            opts.indir)).unique()

        pBamDir.depends = aPrepareBam
        pBamDir.input = lambda ch: [ch.flatten()]

        starts.append(aPrepareBam)

    elif opts.intype in ('fq', 'fastq'):
        # pair-end fastq files
        # *.fq, *.fq.gz *.fastq, *.fastq.gz
        # sample info should be:
        # +--------------+----------+---------+
        # | Sample       | Patient  | Group   |
        # | x_Tumor.bam  | x        | TUMOR   |
        # | x_Normal.bam | x        | NORMAL  |
        # | ...          | ...      | ...     |
        # +--------------+----------+---------+
        # corresponding fastq files would be:
        # x_Tumor_1.fq(.gz)  / x_Tumor_1.fastq(.gz)
        # x_Tumor_2.fq(.gz)  / x_Tumor_2.fastq(.gz)
        # x_Normal_1.fq(.gz) / x_Normal_1.fastq(.gz)
        # x_Normal_2.fq(.gz) / x_Normal_2.fastq(.gz)
        def bam2fqpair(fastq):
            fqdir = path.dirname(fastq)
            bname = path.splitext(path.basename(fastq))[0]
            exts1 = ['_1.fq', '_1.fq.gz', '_1.fq.gz', '_1.fastq.gz']
            exts2 = ['_2.fq', '_2.fq.gz', '_2.fq.gz', '_2.fastq.gz']
            fqfiles1 = [path.join(fqdir, bname + ext) for ext in exts1]
            fqfile1 = [fqfile for fqfile in fqfiles1 if path.isfile(fqfile)][0]
            fqfiles2 = [path.join(fqdir, bname + ext) for ext in exts2]
            fqfile2 = [fqfile for fqfile in fqfiles2 if path.isfile(fqfile)][0]
            return fqfile1, fqfile2

        aPrepareBam.modules.fastq()
        aPrepareBam.input = [
            bam2fqpair(fastq) for fastq in saminfo.toChannel(opts.indir)
        ]
        pBamDir.depends = (aPrepareBam.pSam2Bam
                           if aPrepareBam.pSam2Bam.args.tool == 'elprep'
                           else aPrepareBam.pBamRecal)
        pBamDir.input = lambda ch: [ch.flatten()]

        starts.append(aPrepareBam)
    else:
        pBamDir.input = [saminfo.toChannel(opts.indir)]
        starts.append(pBamDir)

    if 'germ' in opts.muts:
        pBam2Gmut.depends = pBamDir
        pBam2Gmut.input = lambda ch: ch.expand(0, "*.bam")
        pBam2Gmut.args.nthread = opts.nthread
        pBam2Gmut.config.export_dir = path.join(opts.outdir, 'germline')
    if 'soma' in opts.muts:
        pBamPair2Smut.depends = pBamDir
        pBamPair2Smut.input = lambda ch: saminfo.toChannel(ch.get(),
                                                           paired=True)
        pBamPair2Smut.args.nthread = opts.nthread
        pBamPair2Smut.config.export_dir = path.join(opts.outdir, 'somatic')
    if 'scnv' in opts.muts:
        aBam2SCNV.modules.plots()
        aBam2SCNV.pBamDir.depends = pBamDir
        aBam2SCNV.pSampleInfo.input = [opts.saminfo]
        aBam2SCNV.args.nthread = opts.nthread
        aBam2SCNV.ends.config.export_dir = path.join(opts.outdir, 'scnv')
        starts.append(aBam2SCNV)
    if 'gcnv' in opts.muts:
        aBam2GCNV.modules.plots()
        aBam2GCNV.pBamDir.depends = pBamDir
        aBam2GCNV.pSampleInfo.input = [opts.saminfo]
        aBam2GCNV.args.nthread = opts.nthread
        aBam2GCNV.ends.config.export_dir = path.join(opts.outdir, 'gcnv')
        starts.append(aBam2GCNV)

    ppl = PyPPL(forks=int(opts.forks),
                ppldir=opts.ppldir,
                cache='force' if opts.forcecache else True,
                errhow=opts.errhow,
                logger_level=opts.loglevel,
                logger_file=opts.logfile).start(starts)
    if opts.flowchart:
        ppl.flowchart(fcfile=opts.flowchart)
    ppl.run(opts.runner)

if __name__ == "__main__":
    main()