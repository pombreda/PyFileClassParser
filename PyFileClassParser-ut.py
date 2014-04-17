import unittest
import random

from PyFileClassParser import CodeAnalysis
from FileWalker import FileWalker

class TestSequence(unittest.TestCase):

	def setUp(self):
		self.name = 'Kinder'
		self.analysis = CodeAnalysis(self.name)

	def tearDown(self):
		del self.analysis

	def test_definedNameMatches(self):
		self.assertEqual(self.name, self.analysis.name)

	def test_FileCLassOtherNotSupported(self):
		# self.assertRaises(TypeError, self.analysis.extAdd('other', ['.tar.gz', '.zip']))
		pass

	def test_folderAdd(self):

		# declare own file classes, everything else will be counted as OTHER
		self.analysis.extAdd('source', ['.c', '.C', '.cc', '.h', '.CC', '.py'])
		self.analysis.extAdd('make', ['.in', '.am', '.mk'])
		self.analysis.extAdd('script', ['.sh'])
		self.analysis.extAdd('doc', ['.pdf', '.txt', '.doc'])
		self.analysis.extAdd('container', ['.tar.gz', '.zip'])
		self.analysis.extAdd('fpga-code', ['.vhdl', '.v'])
		self.analysis.extAdd('images', ['.iso', '.bin'])

		self.folder = FileWalker(name='Broadcom SDK', pathToFolder='./')

		self.analysis.folderAdd(self.folder)

		self.analysis.export2File(mode='csv', name='simpleExport.csv')

		print self.analysis


if __name__ == "__main__":
    unittest.main()
