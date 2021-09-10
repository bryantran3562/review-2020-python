#!/usr/bin/python

if __name__ == '__main__':

    mylist = [1,"trong",3.2]

    for item in mylist:
        print(item)

    mydict = {"name": "trong", "age": 24}

    #BT - For the Python dict, you must use items()
    for k,v in mydict.items():
        print(k,v)
        
    my_array = [1,2,3,4,5]
    
    #BT - For the list or array, use enumerate function.
    for i, item in enumerate(my_array):
        print(i, item)
