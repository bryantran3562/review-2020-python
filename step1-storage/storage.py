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
    print("Basic List,Tuple,Dict storage:")
    print("========================================================")

    myList = [1,2,3]

    myTuple = (4,5,6)

    myDict = {"name":"trong","age":24}

    for item in myList:
        print(item)

    for item in myTuple:
        print(item)

    for k,v in myDict.items():
        print(k,v)

    # print(dir(myList))
    #BT - You can not change the value of the tuple. But you can convert it to List and change it.
    #     You also can not add more item to the tuple.
    #print(dir(myTuple))
