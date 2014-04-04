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

class TestSequencer(unittest.TestCase):

	def setUp(self):
		pass

	def test_instantiateSubClass(self):
		self.results = FileClassResults('Documents', ['.pdf', '.docx'])

		print self.results

if __name__ == "__main__":
    unittest.main()
