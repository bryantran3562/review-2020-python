#!/usr/bin/python

class Person:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def showPerson(self):
        print("Name: {} - age: {}".format(self.name, self.age))

if __name__ == '__main__':

    p = Person("bt",24)
    p.showPerson()
