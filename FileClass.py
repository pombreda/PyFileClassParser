from FileSize import FileSize
from FileStatistics import FileStatistics
import os.path

class FileClass():

	def __init__(self, className):
		"""this is a constructor for a File Object"""
		self.statistics = FileStatistics(className)
		self.name = className
		self.extensions = []
		self.files = set([])	# unique list of files

	def insertFile(self, pathToFile):
		""" Check file name against regexp and add if matched, return true if added """
		if isinstance(pathToFile, list):
			raise TypeError
		elif isinstance(pathToFile, basestring):
			return self.__addFile(pathToFile)		

		return False

	def addExtension(self, extensions):
		if isinstance(extensions, list):
			return self.__addListExt(extensions)
		elif isinstance(extensions, basestring):
			return self.__addSingleExt(extensions)
		else:
			raise TypeError

	def getExtensions(self):
		return self.extensions

	def __addFile(self, file):
		"""Compare agains the list of regexp and add the file if it matches """
		if len(self.extensions) == 0:
			self.files.add(file)
			self.statistics.addFile(file)
			return True
		else:
			for ext in self.extensions:
				fileName, fileExtension = os.path.splitext(file)

				if fileExtension == ext:
					self.files.add(file)
					self.statistics.addFile(file)
					print "added %s, matching EXT: %s" % (file, ext)
					return True

		return False

	def __addListExt(self, extensions):
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
		return True

	def __addSingleExt(self, ext):
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
