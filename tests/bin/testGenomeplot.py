import unittest
from os import path
from bioprocs import params
from helpers import getfile, getbin, cmdOK, fileOK

genomeplot    = getbin('genomeplot')

class TestGenomePlot (unittest.TestCase):
	def testNoArgs(self):
		cmdOK([genomeplot], self, inerr = 'The track types. Could be data, anno, interaction or ucsc, or multiple of them.', testrc = False)

	def testNormal(self):
		cmd = [
			genomeplot, 
			'-tracks', 'anno', 'ucsc', '-inputs', getfile('test.bam'), 'snp147:AnnotationTrack', '-region', 'chr1:188891483-190087517', '-names', 'Anno', 'SNP', '-outdir', path.join(params.tmpdir.value, 'genomeplot')]
		cmdOK(cmd, self)

if __name__ == '__main__':
	unittest.main(failfast = True, verbosity = 2)