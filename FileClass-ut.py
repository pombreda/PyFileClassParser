import unittest
import random

from FileClass import FileClass

class TestSequence(unittest.TestCase):

	def setUp(self):
		self.analysis = FileClass('unittest')
		self.files = ['FileClass.py', 'FileClass-ut.py']

	def tearDown(self):
		del self.analysis

	def test_addFiles(self):
		for item in self.files:
			self.analysis.insertFile(item)

		self.analysis.insertFile(self.files[1])

		# expected: existing files are ignored
		self.assertEqual(len(self.files), len(self.analysis.getFiles()))

		self.analysis.clear()


if __name__ == "__main__":
    unittest.main()
