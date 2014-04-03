import unittest

from Session import Session
from FileClass import FileClass
from FileStatistics import FileStatistics


class TestSequence(unittest.TestCase):

	def setUp(self):
		class1 = FileClass('AimValley')
		class2 = FileClass('Broadcom')
		self.session = Session('testSession', './', [class1, class2])
		pass

	def tearDown(self):
		pass

	def test_constructor(self):
		pass

if __name__ == "__main__":
    unittest.main()
