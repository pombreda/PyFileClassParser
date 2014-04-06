

import os.path
from FileSize import FileSize


class FileStatistics():
	""" class that holds the statics when analysing folders """
	def __init__(self, name):
		self.name = name
		self.files = []
		self.statistics = {} # dictionary
		self.statistics['maxSize']  = FileSize('B')
		self.statistics['minSize']  = FileSize('B')
		self.statistics['avgSize']  = FileSize('B')
		self.statistics['sumSize']  = FileSize('B')
		self.statistics['numFiles'] = 0


	def addFile(self, pathToFile):
		"""
			add just the size of a file to the class
			computes MIN, MAX, AVG and SUM
		"""
		try:
			isinstance(pathToFile, basestring)
		except:
			raise

		size = os.path.getsize(pathToFile)
		self.files.append(pathToFile)

		self.statistics['numFiles'] += 1

		self.statistics['sumSize'].add(size)

		# compute MAX
		if self.statistics['maxSize'] < size:
			self.statistics['maxSize'].set(size)

		# compute MIN
		if self.statistics['minSize'] == 0:
			self.statistics['minSize'].set(size)
		elif self.statistics['minSize'] > size:
			self.statistics['minSize'].set(size)

		# compute average
		self.statistics['avgSize'].set(self.statistics['sumSize'].get() / self.statistics['numFiles'])
		return True

	def getNumFiles(self):
		return self.statistics['numFiles']

	def getFiles(self):
		return self.files

	def clear(self):
		""" reset the statistics and remove all attached files """
		self.statistics['maxSize'].clear()
		self.statistics['minSize'].clear()
		self.statistics['avgSize'].clear()
		self.statistics['sumSize'].clear()
		self.statistics['numFiles'] = 0
		self.files = []

	def __str__(self):
		"""
			Print a file object and its properties
		"""

		returnStr = "Statistics: {:10s}" .format(self.name)

		if self.statistics['numFiles'] > 0:
			returnStr += '\n numFiles: {:10d}, minSize: {:10}, maxSize: {:10}, avgSize: {:10}, totalSize: {:10}' \
				.format( \
					self.statistics['numFiles'],	self.statistics['minSize'], \
					self.statistics['maxSize'], 	self.statistics['avgSize'], \
					self.statistics['sumSize'] \
				)
		else:
			returnStr += " No files found"
		return returnStr
		return returnStr
