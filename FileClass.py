from FileSize import FileSize
from FileStatistics import FileStatistics
import os.path

class FileClass():

	def __init__(self, className):
		"""this is a constructor for a File Object"""
		self.statistics = FileStatistics(className)
		self.name = className
		self.extensions = []
		self.files = set([])	# list of files associated to this class

	def insertFile(self, pathToFile):
		""" Check file name against regexp and add if matched """
		if isinstance(extensions, list):
			return False
		elsif isinstance(extensions, basestring):
			self.files.add(pathToFile)
		self.statistics.addFile(pathToFile)
		return True

	def addExtension(self, extensions):
		if isinstance(extensions, list):
			return self.__addList(extensions)
		elif isinstance(extensions, basestring):
			return self.__addSingle(extensions)
		else:
			raise TypeError

	def getExtensions(self):
		return self.extensions

	def __addList(self, extensions):
		for ext in extensions:
			found = False
			for index in self.extensions:
				if ext == index:
					found = True
					break;
			
			if found:
				continue
			else:
				self.extensions.append(ext)
				print "added %s" % ext
		return True

	def __addSingle(self, ext):
		for index in self.extensions:
			if ext == index:
				return True
		
		self.extensions.append(ext)
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
