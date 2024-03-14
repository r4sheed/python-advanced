class Address:
    # Initializes with address details
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)
    # Displays the address
    def show(self):
        print(self.street)
        print(self.city)

class Person:
    # Initializes with personal details
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)
    # Displays the personal details
    def show(self):
        print(self.name + ' ' + self.email)

class Contact(Person, Address):
    # Multiple inheritance allows Contact to inherit from both Person and Address
    # This enables a single Contact instance to embody properties and methods of both ancestors.
    def __init__(self, name, email, street, city):
        # Initializing base classes
        Person.__init__(self, name, email)
        Address.__init__(self, street, city)
    # Displays combined details from both Person and Address
    def show(self):
        Person.show(self)
        Address.show(self)
        print()

class Notebook:
    people = dict()
    # Adds a contact to the notebook
    def add(self, name, email, street, city):
        self.people[name] = Contact(name, email, street, city)
    # Displays contact details if the name exists
    def show(self, name):
        if name in self.people:
            self.people[name].show()
        else:
            print('Unknown people:', name)

notes = Notebook()
notes.add('Alice', 'alice@py.io', 'Example st. 24', 'Stockholm')
notes.add('Bob', 'bob@py.io', 'Example st. 42', 'Budapest')

notes.show('Alice')
notes.show('Martin')