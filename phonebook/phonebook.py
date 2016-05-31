class Person(object):
	def __init__(self, name, celphone):
		self.name = name
		self.celphone = celphone

	def __str__(self):
		return self.name

	def printCelphone(self):
		print self.celphone

class Phonebook(object):
	def __init__(self):
		self.people = []

	def add_person(self, person):
		self.people.append(person)

	def show_people(self):
		for person in self.people:
			print person.name + " - " + person.celphone

	def search_person(self, search):
		for person in self.people:
			if (person.name == search) or (person.celphone == search):
				return person
			else:
				return False

	def search_and_show_person(self, search):
		person = self.search_person(search)
		if person:
			print person.name + " - " + person.celphone
		else:
			print "Nenhuma pessoa encontrada"

	def delete_person(self, search):
		person = self.search_person(search)
		if person:
			self.people.remove(person)
			print "pessoa removida com sucesso"
		else:
			print "pessoa nao encontrada"

