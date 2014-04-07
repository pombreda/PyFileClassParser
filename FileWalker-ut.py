import unittest
import random

from FileWalker import FileWalker

class TestSequence(unittest.TestCase):

	def setUp(self):
		self.folder = FileWalker('Broadcom SDK', './')

	def tearDown(self):
		del self.folder

	def test_getFiles(self):
		self.assertEqual(211, len(self.folder.getFiles()))

	def test_checkPath(self):
		self.assertEqual(self.folder.path, './')
		self.assertEqual(self.folder.name, 'Broadcom SDK')

if __name__ == "__main__":
    unittest.main()
