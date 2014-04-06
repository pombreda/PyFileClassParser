# unit test for FileClass object
import unittest

from FileClass import FileClass
from FileClass import FileClassResults


class TestSequence(unittest.TestCase):

	def setUp(self):
		self.fileClass = FileClass('Test1')
		pass

	def tearDown(self):
		pass

	def test_IgnoreDoubledExtensions(self):
		self.assertTrue(self.fileClass.addExtension(['.cc', '.C', '.cc', '.exe', '.EXE']))
		self.assertEqual(4, len(self.fileClass.getExtensions()))
		print self.fileClass

class TestFileClassResults(unittest.TestCase):

	def setUp(self):
		pass

	def test_instantiateSubClass(self):
		self.fileClass = FileClass('Documents', ['.pdf', '.docx'])
		self.results = FileClassResults(self.fileClass)
		print self.results

	def test_insertFile(self):
		self.fileClass = FileClass('Documents', ['.py'])
		self.results = FileClassResults(self.fileClass)

		self.assertTrue(self.results.insertFile('FileClass.py'))

		self.assertFalse(self.results.insertFile('test-run-all.sh'))

	def test_clearFileClassResults(self):
		self.fileClass = FileClass('Documents', ['.py'])
		self.results = FileClassResults(self.fileClass)

		self.assertTrue(self.results.insertFile('FileClass.py'))

		self.assertEqual(1, len(self.results.getFiles()))

		self.results.clear()

		self.assertEqual(0, len(self.results.getFiles()))

		print self.results	


if __name__ == "__main__":
    unittest.main()
