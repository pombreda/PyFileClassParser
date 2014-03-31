import unittest
import random

from FileClass import FileClass

class TestSequence(unittest.TestCase):

	def setUp(self):
		self.analysis = FileClass('unittest')
		self.analysis.clear()

	def tearDown(self):
		del self.analysis

	def test_emptyWhenConstructed(self):

		self.assertEqual(len(self.analysis.getFiles()), 0)


	def test_addOneElement(self):
		
		# 'files = ['FileClass.py', 'FileClass-ut.py']'
		self.analysis.insertFile('FileClass.py')

		# expected: existing files are ignored
		self.assertEqual(len(self.analysis.getFiles()), 1)


	def test_doubledItemIgnored(self):
		
		# 'files = ['FileClass.py', 'FileClass-ut.py']'
		self.analysis.insertFile('FileClass.py')

		# expected: existing files are ignored
		self.assertEqual(len(self.analysis.getFiles()), 1)

		self.analysis.insertFile('FileClass.py')

		self.assertEqual(len(self.analysis.getFiles()), 1)


	def test_NoItemsWhenCleared(self):

		self.analysis.insertFile('FileClass.py')

		# expected: existing files are ignored
		self.assertEqual(len(self.analysis.getFiles()), 1)

		self.analysis.clear()

		self.assertEqual(len(self.analysis.getFiles()), 0)


if __name__ == "__main__":
    unittest.main()
