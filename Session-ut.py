import unittest

from Session import Session
from FileClass import FileClass
from FileClass import FileClassResults
from FileStatistics import FileStatistics
from FileWalker import FileWalker


class TestSequence(unittest.TestCase):

	def setUp(self):
		class1 = FileClass('documents', ['.pdf', '.doc'])
		class2 = FileClass('C-code', ['.c', '.h', '.py'])
		self.session = Session('testSession', './', [class1, class2])
		pass

	def tearDown(self):
		pass

	def test_constructor(self):
		self.assertEqual(2, len(self.session.classes))
		print self.session

	def test_addingFiles(self):
		self.folder = FileWalker('localDir', './')
		self.assertTrue(self.session.addFiles(self.folder))

		print self.session

if __name__ == "__main__":
    unittest.main()
