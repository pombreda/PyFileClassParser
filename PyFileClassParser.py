"""
FileAnalysis is meant to scan a folder in the filesystem and count 
associate different file types to different classes. The module provides
statistics about:
 > total number of files per class
 > total size of files per class
 > maximum file size per class
 > minimum file size per class
 > average file size per class
"""


import os
import getpass
import re
from FileSize import FileSize
from FileClass import FileClass
from Folder import FileWalker
from Session import Session
AlreadyExists = 1

# scan a folder for files and present the results
# in a very neat way
# add interface in order to store the results into a database



class CodeAnalysis():
	"""Holds the results for a file analysis"""

	def __init__(self):
		self.folder = []
		self.isValid = False
		self.userName = getpass.getuser()
		self.db = {} # create a dictionary, file extensions to class names
		self.sessions = [] # list of sessions, stores files and statistics for a number of classes per session
		self.classes = [] # list of classes
		self.classes.append(FileClass('other'))


	def folderAdd(self, folderObject):
		"""
			each time one adds a new FileWalker object it triggers 
			a new session that is stored using the unique FileWalker 
			name
		"""
		if isinstance(folderObject, FileWalker):
			
			# clone list of classes and create new
			thisSession = Session(folderObject.name, folderObject.path, self.classes)

			# iterate over all files
			self.__addFilesToSession(folderObject.files, thisSession)

			
			# append the completed session to the list
			self.sessions.append(thisSession)

			print "add Folder: %s" % folderObject.name

		else:
			return NotImplemented
		return True


	def extAdd(self, type, extension):
		if isinstance(extension, list):
			for item in extension:
				self.db[item] = type
		elif isinstance(extension, basestring):
			self.db[extension] = type
		else:
			return nonImplemented

		# if not in self.classes
		if len(self.classes) == 0:
			self.classes.append(FileClass(type))
		elif not self.__classExists(type):
			self.classes.append(FileClass(type))
		else:
			return False
		return True

	def addFileToClassInSession(self, fileClass, pathToFile):
			
    	fileName, fileExtension = os.path.splitext(file)
    	
    	if fileExtension in self.db:
    		fileClass = self.db[fileExtension]
    		self.__addFileToClass(fileClass, os.path.join(dirpath, f))
    	else:
    		self.__addFileToClass('other', os.path.join(dirpath, f))
		
		self.isValid = True

	def __classExists(self, type):
		"""
			check whether the class exists in the database
		"""
		for item in self.classes:
			if type == item.name:
				return True
			continue

		return False
		

	def __addFileToClass(self, type, fileToPath):
		"""
			TODO : move the code into a statistics module
		"""
		for item in self.classes:
			
			if type == item.name:

				item.insertFile(fileToPath)
				
				item.statistics['numFiles'] += 1
				fileSize = os.path.getsize(fileToPath)

				item.statistics['sumSize'].add(fileSize)

				# compute MAX
				if item.statistics['maxSize'] < fileSize:
					item.statistics['maxSize'].set(fileSize)
				
				# compute MIN
				if item.statistics['minSize'] == 0:
					item.statistics['minSize'].set(fileSize)
				elif item.statistics['minSize'] > fileSize:
					item.statistics['minSize'].set(fileSize)

				# compute average
				item.statistics['avgSize'].set(item.statistics['sumSize'].get() / item.statistics['numFiles']) 
				return True
			else:
				continue

		return False

	def __getFileSize(self, path, fileName):
		return os.path.getsize(os.path.join(path, fileName))


	def __str__(self):
		str = ""
		str += "File Analysis, created by %s\n" % self.userName
		for item in self.classes:
			str += " %s\n\n" % item
		return str

	def __typePrint(self):
		return


	def __folderPrint(self):
		for folder in self.folder:
			print " folder: %s" % folder
		return

