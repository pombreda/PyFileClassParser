import os.path
import copy

from FileClass import FileClass
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
				print "Added FileClass: %s" % (item.name)
				self.classes.append(copy.copy(item))
			continue
		print "done constructor"


	def addFiles(self, folderObject):
		if isinstance(pathToFile, FileWalker):
			return True
		else:
			return False


	def clearSessions(self):
		for stat in self.classes:
			stat.clear()


	def __str__(self):
		returnStr = ""
		returnStr += "Session: %s\n" % (self.name)
		for stat in self.stat:
			returnStr += " %s\n" % (stat)
		return returnStr
