#!/usr/bin/python

if __name__ == '__main__':

    #BT - Using the with statement - you don't have to worry about closing file. It will
    #     automatically taking care it for you.
    with open("test.txt",'w') as f:
        f.write("Hello...")

    with open("test.txt",'r') as f:
        for line in f:
            print(line)


