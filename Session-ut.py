import unittest

from Session import Session
from FileClass import FileClass
from FileClass import FileClassResults
from FileStatistics import FileStatistics


class TestSequence(unittest.TestCase):

	def setUp(self):
		class1 = FileClass('documents', ['.pdf', '.doc'])
		class2 = FileClass('C-code', ['.c', '.h'])
		self.session = Session('testSession', './', [class1, class2])
		pass

	def tearDown(self):
		pass

	def test_constructor(self):
		self.assertEqual(2, len(self.session.classes))
		print self.session

if __name__ == "__main__":
    unittest.main()
