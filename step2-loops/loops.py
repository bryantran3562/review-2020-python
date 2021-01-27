#!/usr/bin/python

if __name__ == '__main__':

    mylist = [1,"trong",3.2]

    for item in mylist:
        print(item)

    mydict = {"name": "trong", "age": 24}

    for k,v in mydict.items():
        print(k,v)
        
    my_array = [1,2,3,4,5]
    
    for i, item in enumerate(my_array):
        print(i, item)
