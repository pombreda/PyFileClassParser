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
		self.results = FileClassResults('Documents', ['.pdf', '.docx'])
		print self.results

	def test_insertFile(self):
		self.results = FileClassResults('Documents', ['.py'])

		self.assertTrue(self.results.insertFile('FileClass.py'))

		self.assertFalse(self.results.insertFile('test-run-all.sh'))

if __name__ == "__main__":
    unittest.main()
