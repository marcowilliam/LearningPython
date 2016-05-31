class Person(object):
	def __init__(self, name, celphone):
		self.name = name
		self.celphone = celphone

	def __str__(self):
		return self.name

	def printCelphone(self):
		print self.celphone

