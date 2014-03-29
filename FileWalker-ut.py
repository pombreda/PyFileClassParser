import unittest
import random

import Folder

class TestSequence(unittest.TestCase):

	def setUp(self):
		self.folder = Folder.FileWalker('Broadcom SDK', '/Users/bastian/Jobb/Transmode/R21-EDU/Software/AIMVALLEY-Titan-R1_03_00-LD3.0-20121119')

	def tearDown(self):
		del self.folder

	def test_getFiles(self):
		self.assertEqual(205, len(self.folder.getFiles()))

	def test_checkPath(self):
		self.assertEqual(self.folder.path, '/Users/bastian/Jobb/Transmode/R21-EDU/Software/AIMVALLEY-Titan-R1_03_00-LD3.0-20121119')
		self.assertEqual(self.folder.name, 'Broadcom SDK')

if __name__ == "__main__":
    unittest.main()
