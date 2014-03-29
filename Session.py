import os.path

from FileClass import FileClass
from FileStatistics import FileStatistics

class Session():
	"""
		contains a number of statistic objects one for each class
	"""
	def __init__(self, name="unknown", folder="./", classes=[]):
		self.name = name
		self.folder = folder
		self.stat = [] # list of statistics for each class
		for item in classes:
			if not self.__exists(item):
				self.stat.append(FileStatistics(item))

	def addFileToClass(self, pathToFile, className):
		try:
			isinstance(className, basestring)
		except:
			raise
			
		stat = self.getStatisticsForClass(className)
		if isinstance(stat, FileStatistics):
			stat.addFile(pathToFile)
			print "file added"
			return True

		return False


	def getStatisticsForClass(self, className):
		for item in self.stat:
			if className == item.name:
				return item
			else:
				continue
		return False

	def getFileClasses(self):
		classes = []
		for item in self.stat:
			classes.append(item.name)

		return classes


	def clearSessions(self):
		for stat in self.classes:
			stat.clear()


	def __str__(self):
		returnStr = ""
		returnStr += "Session: %s\n" % (self.name)
		for stat in self.stat:
			returnStr += " %s\n" % (stat)
		return returnStr


	def __exists(self, className):
		if len(self.stat) == 0:
			return False
		else:
			for item in self.stat:
				if item.name == className:
					return True
				else:
					continue
		return False