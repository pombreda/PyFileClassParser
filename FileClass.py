#FileClass

from FileStatistics import FileStatistics
import os.path

class FileClass():
	"""docstring for FileClass"""
	def __init__(self, name, extensions=[]):
		self.name = name
		self.extensions = set(extensions)

	def addExtension(self, extensions):
		if isinstance(extensions, list):
			for item in extensions:
				self.extensions.add(item)
		elif isinstance(extensions, basestring):
			self.extensions.add(item)
		else:
			return False
		return True

	def getExtensions(self):
		return list(self.extensions)

	def __str__(self):
		returnStr = "FileClass: %s (%s)\n" % (self.name, self.__class__.__name__)
		returnStr += " Contained Extensions: "
		if len(self.extensions) == 0:
			returnStr += " none"
		for item in list(self.extensions):
			returnStr += "\'%s\' " % (item)
		return returnStr



class FileClassResults(FileClass):
	"""docstring for FileClassResults"""
	def __init__(self, name, extensions):
		FileClass.__init__(self, name , extensions)
		self.files = set([]) # initiate set with empty list
		self.statistics = FileStatistics(name)

	def insertFile(self, pathToFile):
		""" Check file name against regexp and add if matched, return true if added """
		if isinstance(pathToFile, list):
			raise TypeError
		elif isinstance(pathToFile, basestring):
			if not os.path.isfile(pathToFile):
				return False
			else:
				return self.__addFile(pathToFile)
		else:
			return False

	def clear(self):
		self.statistics.clear()
		self.files.clear()

	def getFiles(self):
		return list(self.files)


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
					return True

		return False
