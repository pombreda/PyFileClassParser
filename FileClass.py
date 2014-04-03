#FileClass

class FileClass():
	"""docstring for FileClass"""
	def __init__(self, name="Unknown", extensions=[]):
		self.name = name
		self.extensions = set([])

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
		returnStr = "FileClass: %s\n" % (self.name)
		returnStr += " Contained Extensions: "
		for item in list(self.extensions):
			returnStr += "\'%s\' " % (item)
		return returnStr
