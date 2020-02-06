#!/usr/bin/python

def myfunc(n):
    return lambda a : a * n

if __name__ == "__main__":

    #BT - First time, you call to set the n variable and then assigned the lambda function to a variable
    mydouble = myfunc(3)

    #BT - Then call it again
    print(mydouble(3))

    #BT - It just a anonymous function.
    x = lambda a : a + 3

    print(x(3))
