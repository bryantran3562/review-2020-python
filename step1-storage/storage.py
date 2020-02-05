#!/usr/bin/python

if __name__ == '__main__':

    print()
    print("========================================================")
    print("Basic builtin storage:")
    print("========================================================")

    myInt = 2
    myFloat = 3.2
    myBool = True
    myString = "This is a test"

    myComment = '''
    This is a longer comment
    span to multiline. This is another
    line.
    '''

    print(myInt)
    print(myFloat)
    print(myBool)
    print(myString)
    print(myComment)
    print("The int value is: {} - The bool value is: {}".format(myInt, myBool))

    print()
    print("========================================================")
    print("Basic Array,Tuple,Dict storage:")
    print("========================================================")

    myArray = [1,2,3]

    myTuple = (4,5,6)

    myDict = {"name":"trong","age":24}

    for item in myArray:
        print(item)

    for item in myTuple:
        print(item)

    for k,v in myDict.items():
        print(k,v)
