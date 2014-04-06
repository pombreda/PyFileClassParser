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
		for item in classes:
			if not isinstance(item, FileClass):
				raise TypeError("Expected a FileClass object")
			else:
				self.classes.append(FileClassResults(item))
			continue


	def addFiles(self, folderObject):
		if isinstance(pathToFile, FileWalker):
			return True
		else:
			return False


	def clearSessions(self):
		for fileClass in self.classes:
			fileClass.clear()


	def __str__(self):
		returnStr = ""
		returnStr += "Session: %s\n" % (self.name)
		for fileClass in self.classes:
			returnStr += " %s\n" % (fileClass)
		return returnStr
