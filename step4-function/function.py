#!/usr/bin/python

def callMe(a):
    print(a)

def variadict(*args, **kwargs):
    for item in args:
        print(item)
    for k,v in kwargs.items():
        print(k,v)

if __name__ == '__main__':

    callMe(3)

    variadict(1,2,3, name="test", age=24)

    mytuple = (1,2,3)
    myDict = {"name": "bt", "age":24}

    variadict(*mytuple,**myDict)
