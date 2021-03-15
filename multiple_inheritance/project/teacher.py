from multiple_inheritance.project.person import Person
from multiple_inheritance.project.employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
