# unit test for FileClass object
import unittest

from FileClass import FileClass


class TestSequence(unittest.TestCase):

	def setUp(self):
		self.fileClass = FileClass('Test1')
		pass

	def tearDown(self):
		pass

	def test_constructor(self):
		self.assertTrue(self.fileClass.addExtension(['.cc', '.C', '.cc', '.exe', '.EXE']))
		self.assertEqual(4, len(self.fileClass.getExtensions()))
		print self.fileClass

if __name__ == "__main__":
    unittest.main()
