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
        person_found = None
        for person in self.people:
            if (person.name == search) or (person.celphone == search):
                person_found = person
                break
        return person_found

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

def main():

    phonebook = Phonebook()
    while True:
        print "Selecione a opcao desejada"
        print "1 - Adicionar numero"
        print "2 - Mostrar lista"
        print "3 - Procurar pessoa por nome ou numero"
        print "4 - Deletar pessoa por nome ou numero"

        opcao = raw_input()

        if opcao == '1':
            print "digite o nome"
            nome = raw_input()
            print "digite o numero"
            numero = raw_input()
            person = Person(nome, numero)
            phonebook.add_person(person)

        elif opcao == '2':
            phonebook.show_people()
        
        elif opcao == '3':
            print "Entre com o nome ou numero da pessoa"
            search = raw_input()
            phonebook.search_and_show_person(search)

        elif opcao == '4':
            print "Entre com o nome ou numero da pessoa"
            search = raw_input()
            phonebook.delete_person(search)

        else:
            print "opcaoo invalida"
