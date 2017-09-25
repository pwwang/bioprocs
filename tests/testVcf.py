import os, sys, unittest, addPath

from pyppl import PyPPL, Box, Channel, Proc
from bioprocs.fastx import pFastqPESim
from bioprocs.vcf import pVcfFilter, pVcfAnno, pCallRate
from bioprocs.vcfnext import pStats2Matrix, pPlotStats
from bioprocs.web import pDownloadGet
from bioprocs.common import pFiles2Dir
from bioaggrs import params

params = params.toDict()

unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: cmp(x, y)

class TestVcf (unittest.TestCase):
	
	data = Box()
	def test0_prepareData(self):
		
		pDownloadGet.input = ["https://raw.githubusercontent.com/jamescasbon/PyVCF/master/vcf/test/example-4.1.vcf"]
		pAddChr = Proc ()
		pAddChr.input = "infile:file"
		pAddChr.output = "outfile:file:{{in.infile | bn}}"
		pAddChr.depends = pDownloadGet
		pAddChr.script = """
		awk '$0 ~ /^#/ && $0 !~ /^##contig/ {print} $0 ~ /##contig/ {print "##contig=<ID=chr20,length=63025520>"} $0 !~ /^#/ {print "chr"$0}' "{{in.infile}}" > "{{out.outfile}}"
		"""
		pAddChr.callback = lambda p: self.data.update({'vcfs': p.channel})
		PyPPL().start(pDownloadGet).run()
		
	def test2_pVcfFilter (self):
		
		pVcfFilter.input        = self.data.vcfs
		pVcfFilter.forks        = 2
		
		pVcfFilter1             = pVcfFilter.copy()
		pVcfFilter2             = pVcfFilter.copy()
		pVcfFilter3             = pVcfFilter.copy()
		pVcfFilter4             = pVcfFilter.copy()
		pVcfFilter1.args.tool   = 'gatk'
		pVcfFilter2.args.tool   = 'bcftools'
		pVcfFilter3.args.tool   = 'snpsift'
		pVcfFilter4.args.tool   = 'vcflib'
		pVcfFilter5             = pVcfFilter1.copy()
		pVcfFilter6             = pVcfFilter2.copy()
		pVcfFilter7             = pVcfFilter3.copy()
		pVcfFilter8             = pVcfFilter4.copy()
		
		pVcfFilter1.args.ref            = params.ref
		pVcfFilter5.args.ref            = params.ref
		pVcfFilter1.args.selectors.type = "indel"
		pVcfFilter1.expect              = 'grep 1230237 {{out.outfile}} && grep 1234567 {{out.outfile}} && !(grep 14370 {{out.outfile}}) && !(grep 17330 {{out.outfile}}) && !(grep 1110696 {{out.outfile}})'
		
		pVcfFilter2.args.selectors.filter = "PASS"
		pVcfFilter2.expect                = 'grep 1230237 {{out.outfile}} && grep 1234567 {{out.outfile}} && grep 14370 {{out.outfile}} && !(grep 17330 {{out.outfile}}) && grep 1110696 {{out.outfile}}'
		
		pVcfFilter3.args.selectors.genotype = {0: '0/0'}
		pVcfFilter3.expect                  = 'grep 1230237 {{out.outfile}} && !(grep 1234567 {{out.outfile}}) && grep 14370 {{out.outfile}} && grep 17330 {{out.outfile}} && !(grep 1110696 {{out.outfile}})'
		
		pVcfFilter4.args.selectors.type     = "snp"
		pVcfFilter4.args.selectors.genotype = {2: '1/1'}
		pVcfFilter4.expect = '!(grep 1230237 {{out.outfile}}) && !(grep 1234567 {{out.outfile}}) && grep 14370 {{out.outfile}} && !(grep 17330 {{out.outfile}}) && !(grep 1110696 {{out.outfile}})'
		
		pVcfFilter5.args.selectors.type  = "snp"
		pVcfFilter5.args.filters.lowQUAL = "QUAL < 10"
		pVcfFilter5.args.filters.lowDP   = "DP < 10"
		pVcfFilter5.args.keep            = False
		pVcfFilter5.expect               = '!(grep 1230237 {{out.outfile}}) && !(grep 1234567 {{out.outfile}}) && grep 14370 {{out.outfile}} && !(grep 17330 {{out.outfile}}) && grep 1110696 {{out.outfile}}'
		
		pVcfFilter6.args.selectors.type     = "snp"
		pVcfFilter6.args.filters.lowQUAL    = "QUAL < 10 | DP < 10"
		pVcfFilter6.expect = '!(grep 1230237 {{out.outfile}}) && !(grep 1234567 {{out.outfile}}) && grep 14370 {{out.outfile}} && !(grep 17330 {{out.outfile}}) && grep 1110696 {{out.outfile}}'
		
		pVcfFilter7.args.selectors.type     = "snp"
		pVcfFilter7.args.filters.lowQUAL    = "(QUAL < 10) | (DP < 10)"
		pVcfFilter7.args.keep               = False
		pVcfFilter7.expect = '!(grep 1230237 {{out.outfile}}) && !(grep 1234567 {{out.outfile}}) && grep 14370 {{out.outfile}} && !(grep 17330 {{out.outfile}}) && grep 1110696 {{out.outfile}}'
		
		pVcfFilter8.args.selectors.type     = "snp"
		pVcfFilter8.args.filters.lowQUAL    = "QUAL < 10"
		pVcfFilter8.args.filters.lowDP      = "DP < 10"
		pVcfFilter8.args.gz                 = True
		pVcfFilter8.expect = '!(zcat {{out.outfile}} | grep 1230237) && !(zcat {{out.outfile}} | grep 1234567) && zcat {{out.outfile}} | grep 14370 && !(zcat {{out.outfile}} | grep 17330) && zcat {{out.outfile}} | grep 1110696'
		
		starts = [
			pVcfFilter1,
			#pVcfFilter2,
			#pVcfFilter3,
			#pVcfFilter4,
			#pVcfFilter5,
			#pVcfFilter6,
			#pVcfFilter7,
			#pVcfFilter8,
		]
		PyPPL().start(*starts).run()
	
	def test2_pVcfAnno (self):
		pVcfAnno.input        = self.data.vcfs
		pVcfAnno.forks        = 2
		pVcfAnno1             = pVcfAnno.copy()
		pVcfAnno2             = pVcfAnno.copy()
		pVcfAnno3             = pVcfAnno.copy()
		pVcfAnno1.args.tool   = 'snpeff'
		pVcfAnno2.args.tool   = 'vep'
		pVcfAnno2.args.dbpath = '/data2/junwenwang/shared/reference/hg19/vep/cache/'
		pVcfAnno2.args.params = '--port 3337'
		pVcfAnno2.args.genome = 'GRCh37'
		pVcfAnno3.args.tool   = 'annovar'
		pVcfAnno3.args.dbpath = '/data2/junwenwang/shared/tools/annovar/humandb/'
		pVcfAnno3.args.gz     = True
		pVcfAnno1.callback    = lambda p: self.data.update({'vcfs': p.channel.colAt(0)})
		
		starts = [
			pVcfAnno1,
			pVcfAnno2,
			pVcfAnno3
		]
		PyPPL().start(*starts).run()
		
	def test3_pCallRate (self):
		pFiles2Dir1 = pFiles2Dir.copy('vcfstats')
		pFiles2Dir1.input = [Channel.create(self.data.vcfs).flatten() * 4]
		pCallRate1 = pCallRate.copy()
		pCallRate1.depends =  pFiles2Dir1
		
		PyPPL().start(pFiles2Dir1).run()
		
	def test4_pPlotStats(self):
		pVcfAnno4             = pVcfAnno.copy()
		pVcfAnno4.args.tool   = 'snpeff'
		pVcfAnno4.args.snpeffStats = True
		
		pFiles2Dir2 = pFiles2Dir.copy()
		pFiles2Dir2.depends = pVcfAnno4
		pFiles2Dir2.tag = 'plotstats'
		pFiles2Dir2.input = lambda ch: [ch.colAt(1).expand(0, '*.stats.csv').flatten()*4]
		
		pStats2Matrix.depends = pFiles2Dir2
		pStats2Matrix.expect  = 'ls {{out.outdir}}/*.mat.txt'
		pPlotStats.depends = pStats2Matrix
		PyPPL().start(pVcfAnno4).run()
		
		
if __name__ == '__main__':
	unittest.main(failfast=True)