# FileStatistics

import unittest
import os
import sys

sys.path.append('../')

from FileStatistics import FileStatistics

class TestSequence(unittest.TestCase):

	def setUp(self):
		self.stat = FileStatistics('other')
		pass

	def tearDown(self):
		pass

	def test_addFiles(self):
		self.stat.addFile('../FileClass.py')
		self.assertEqual(1, self.stat.getNumFiles())

	def test_getFiles(self):
		files = self.stat.getFiles()
		self.assertEqual(0, len(files))

		self.stat.addFile('../FileClass.py')
		self.assertEqual(1, len(files))		

if __name__ == "__main__":
    unittest.main()
