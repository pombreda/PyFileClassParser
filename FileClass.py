from FileSize import FileSize
from FileStatistics import FileStatistics
import os.path

class FileClass():

	def __init__(self, className):
		"""this is a constructor for a File Object"""
		self.statistics = FileStatistics(className)
		self.name = className
		self.files = []	# list of files associated to this class
		

	def insertFile(self, pathToFile):
		if isinstance(pathToFile, basestring):
			if not pathToFile in self.files:
				self.files.append(pathToFile)
				self.statistics.addFile(pathToFile)
			else:
				return 
			return True
		else:	
			return NotImplemented

	def clear(self):
		self.statistics.clear()


	def getFiles(self):
		return self.files


	def __str__(self):

		"""Print a file object and its properties"""

		returnStr = "FileClass: \"%s\"\n" % (self.name)
		
		if self.statistics['numFiles'] > 0:
			returnStr += ' numFiles: {:10d}, minSize: {:10}, maxSize: {:10}, avgSize: {:10}, totalSize: {:10}' \
				.format( \
					self.statistics['numFiles'],	self.statistics['minSize'], \
					self.statistics['maxSize'], 	self.statistics['avgSize'], \
					self.statistics['sumSize'] \
				)
		else:
			returnStr += " No files found"
		return returnStr
