import unittest
import random

from FileWalker import FileWalker

class TestSequence(unittest.TestCase):

	def setUp(self):
		self.folder = FileWalker('Broadcom SDK', '/Users/bastian/Jobb/Transmode/R21-EDU/Software/AIMVALLEY-Titan-R1_03_00-LD3.0-20121119')

	def tearDown(self):
		del self.folder

	def test_getFiles(self):
		self.assertEqual(206, len(self.folder.getFiles()))

	def test_checkPath(self):
		self.assertEqual(self.folder.path, '/Users/bastian/Jobb/Transmode/R21-EDU/Software/AIMVALLEY-Titan-R1_03_00-LD3.0-20121119')
		self.assertEqual(self.folder.name, 'Broadcom SDK')

if __name__ == "__main__":
    unittest.main()
