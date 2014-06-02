"""
	class: FileSize - holds a value and its unit
"""

class FileSize():

	def __init__(self, unitStr):
		self.value = 0
		if isinstance(unitStr, basestring):
			self.unitStr = unitStr
		else:
			return False


	def set(self, size):
		if isinstance(size, int):
			self.value = size
			return True

	def get(self):
		return self.value

	def clear(self):
		self.value = 0
		return True

	def add(self, size):
		if isinstance(size, int):
			self.value += size
		elif isinstance(size, FileSize):
			self.value += size.value
		else:
			return False
		return True

	def __eq__(self, right):
		if isinstance(right, int):
			return self.value == right
		elif isinstance(right, FileSize):
			return self.value == right.value
		else:
			return NotImplemented

	def __lt__(self, right):
		if isinstance(right, int):
			return self.value < right
		elif isinstance(right, FileSize):
			return self.value < right.value

	def __gt__(self, right):
		if isinstance(right, int):
			return self.value > right
		elif isinstance(right, FileSize):
			return self.value > right.value

	def __str__(self):
		if self.value >= 0 and self.value < 1000:
			return "{:6d}  {:1}" .format(self.value, self.unitStr)
		elif self.value >= 1000 and self.value < 1000000:
			return "{:6.2f} K{:1}" .format(self.value / 1000, self.unitStr)
		elif self.value < 1000000000 and self.value >= 1000000:
			return "{:6.2f} M{:1}" .format(self.value / 1000000, self.unitStr)
		else:
			return "{:6.2f} G{:1}" .format(self.value / 1000000000, self.unitStr)
