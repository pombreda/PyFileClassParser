import os.path
import copy

from FileClass import FileClass
from FileClass import FileClassResults
from FileWalker import FileWalker
from FileStatistics import FileStatistics

class Session():
	"""
		contains a number of statistic objects one for each class
	"""
	def __init__(self, name="unknown", folder="./", classes=[]):
		self.name = name
		self.folder = folder # the folder to analyse
		self.classes = [] # list of FileClass objects
		self.other = FileClassResults(FileClass('other'))
		for item in classes:
			if not isinstance(item, FileClass):
				raise TypeError("Expected a FileClass object")
			else:
				self.classes.append(FileClassResults(item))
			continue


	def addFiles(self, folderObject):
		if isinstance(folderObject, FileWalker):
			self.__addFiles(folderObject.getFiles())
			return True
		else:
			return False


	def clearSessions(self):
		for fileClass in self.classes:
			fileClass.clear()

	def __addFiles(self, listOfFiles):
		for item in listOfFiles:
			added = False
			for fileClass in self.classes:
				# iterate over all files and add them to their
				# matching class
				if fileClass.insertFile(item) == True:
					# we've found a matching file class
					added = True
					break

			if not added:
				self.other.insertFile(item)
		return True

	def __str__(self):
		returnStr = ""
		returnStr += "Session: %s\n" % (self.name)
		for fileClass in self.classes:
			returnStr += " %s\n" % (fileClass)
		returnStr += " %s\n" % (self.other)
		return returnStr
