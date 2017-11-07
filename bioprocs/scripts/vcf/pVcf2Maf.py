import shlex
{{ runcmd }}
{{ params2CmdArgs }}

{% if args.tool | lambda x: x == 'vcf2maf' %}
from os import path
from subprocess import check_output
vep = check_output(['which', {{args.vep | quote}}]).strip()

params = {{args.params}}

# vcf2maf.pl --input-vcf ZYYP-ZYYB.vcf  --output-maf ZYYP-ZYYB.snpEff.maf --tumor-id ZXLT-ZXLB_TUMOR --normal-id ZXLT-ZXLB_NORMAL --vep-data /data2/junwenwang/shared/reference/hg19/vep/cache/ --filter-vcf /data2/junwenwang/shared/reference/hg19/vep/ExAC_nonTCGA.r0.3.1.sites.vep.vcf.gz --ref-fasta /data2/junwenwang/shared/reference/hs37d5/phase2_reference_assembly_sequence/hs37d5.fa --vep-path /data2/junwenwang/shared/tools/miniconda2/bin
params['input-vcf']  = {{in.infile | quote}}
params['output-maf'] = {{out.outfile | quote}}
params['vep-data']   = {{args.vepDb | quote}}
params['filter-vcf'] = {{args.filtervcf | quote}}
params['ref-fasta']  = {{args.ref | quote}}
params['vep-path']   = path.dirname(vep)

runcmd ('{{args.vcf2maf}} %s' % params2CmdArgs(params, equal=' '))

{% endif %}