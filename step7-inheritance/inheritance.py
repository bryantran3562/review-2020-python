#!/usr/bin/python

class Person:
    
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def showPerson(self):
        print("Name: {} - age: {}".format(self.name, self.age))

class Teacher(Person):

    #BT - You also need to pass in the args to the Parent.
    def __init__(self, name, age, position, salary):
        super().__init__(name, age)
        self.position = position
        self.salary = salary

    def showTeacher(self):

        print("Name: {} - age: {} - position: {} - salary: {}".format(self.name, self.age,self.position,self.salary))

if __name__ == '__main__':

    t = Teacher("bt",24,"teacher",20000)

    t.showTeacher()
    t.showPerson()
