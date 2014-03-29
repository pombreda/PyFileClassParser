import unittest
import random

from PyFileClassParser import CodeAnalysis
from FileWalker import FileWalker

class TestSequence(unittest.TestCase):

	def setUp(self):
		self.analysis = CodeAnalysis()

	def tearDown(self):
		del self.analysis

	def test_invalidFolder(self):
		self.assertTrue(True)

	def test_folderAdd(self):

		# declare own file classes, everything else will be counted as OTHER
		self.analysis.extAdd('source', ['.c', '.C', '.cc', '.h', '.CC', '.py'])
		self.analysis.extAdd('make', ['.in', '.am', '.mk'])
		self.analysis.extAdd('script', ['.sh'])
		self.analysis.extAdd('doc', ['.pdf', '.txt', '.doc'])
		self.analysis.extAdd('container', ['.tar.gz', '.zip'])

		self.folder = FileWalker(name='Broadcom SDK', pathToFolder='/Users/bastian/Jobb/Transmode/R21-EDU/Software/AIMVALLEY-Titan-R1_03_00-LD3.0-20121119')

		self.analysis.folderAdd(self.folder)

		print self.analysis


if __name__ == "__main__":
    unittest.main()
