# Create a child class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Mike","Olsen")
x.print_name()

