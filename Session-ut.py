import unittest

from Session import Session
from FileStatistics import FileStatistics


class TestSequence(unittest.TestCase):

	def setUp(self):
		self.session = Session('testSession', './', ['other', 'source', 'doc'])
		pass

	def tearDown(self):
		pass

	def test_constructor(self):
		stat = self.session.getStatisticsForClass('other')
		self.assertTrue(isinstance(stat, FileStatistics))

	def test_nonExistingClass(self):
		stat = self.session.getStatisticsForClass('nonExisting')
		self.assertFalse(isinstance(stat, FileStatistics))


class TestSequence2(unittest.TestCase):

	def setUp(self):
		self.session = Session('testSession', './', ['other', 'source', 'doc', 'doc'])
		pass

	def tearDown(self):
		pass

	def test_constructor(self):
		classes = self.session.getFileClasses()
		self.assertEqual(3, len(classes))

	def test_addFileForNonExistingClass(self):
		self.assertFalse(self.session.addFileToClass('FileClass.py', 'nonExisting'))

	def test_getAddFileBack(self):
		self.assertTrue(self.session.addFileToClass('FileClass.py', 'doc'))
		print self.session


if __name__ == "__main__":
    unittest.main()
