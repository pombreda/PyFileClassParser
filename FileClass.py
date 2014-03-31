from FileSize import FileSize
from FileStatistics import FileStatistics
import os.path

class FileClass():

	def __init__(self, className):
		"""this is a constructor for a File Object"""
		self.statistics = FileStatistics(className)

		self.name = className
		self.files = set([])	# list of files associated to this class
		

	def insertFile(self, pathToFile):
		self.files.add(pathToFile)
		self.statistics.addFile(pathToFile)
		return True

	def clear(self):
		self.statistics.clear()
		self.files.clear()


	def getFiles(self):
		return list(self.files)


	def __str__(self):

		"""Print a file object and its properties"""

		returnStr = "FileClass: \"%s\"\n" % (self.name)
		
		returnStr += " %s" % self.statistics
		return returnStr
