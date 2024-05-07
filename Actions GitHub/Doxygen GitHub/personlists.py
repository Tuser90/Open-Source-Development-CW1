class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Occupation: {self.occupation})"


class PersonList:
    def __init__(self):
        self.persons = []

    def add_person(self, name, age, occupation):
        person = Person(name, age, occupation)
        self.persons.append(person)

    def remove_person(self, name):
        self.persons = [p for p in self.persons if p.name != name]

    def display_persons(self):
        if not self.persons:
            print("No persons in the list.")
        else:
            print("Persons in the list:")
            for person in self.persons:
                print(person)


# Example usage:
person_list = PersonList()

# Adding persons to the list
person_list.add_person("John Doe", 30, "Engineer")
person_list.add_person("Alice Smith", 25, "Teacher")
person_list.add_person("Bob Johnson", 35, "Doctor")

# Display all persons
person_list.display_persons()

# Removing a person
person_list.remove_person("Alice Smith")

# Display updated list
person_list.display_persons()
