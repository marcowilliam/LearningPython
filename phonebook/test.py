import unittest
from phonebook import *

class PersonTest(unittest.TestCase):
	def testPrintCelphone(self):
		person = Person("marco", "123456")
		self.assertEqual(person.celphone, "123456")

class PhonebookTest(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		person = Person("Marco", "123456")
		person2 = Person("Felipe", "1234567")
		phonebook = Phonebook()

	def testAddPerson(self):
		phonebook.add_person(person1)
		self.assertEqual(phonebook.show_people, "Marco - 123456")

if __name__ == '__main__':
    unittest.main()
