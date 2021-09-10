#! /usr/bin/python

import json

if __name__ == '__main__':

    my_string = '''{
        "item1": 1,
        "item2": 2
    }'''

    #BT - So if you have a json string, you can convert it to Python dict.
    #     This is so that you can access it using the key and value.
    json_data = json.loads(my_string)

    print(type(json_data))

    print("============================================")
    print("Accessing the key and value")
    print("============================================")

    print(json_data['item1'])

    for key, value in json_data.items():
        print(key,value)


    ########################################################################################
    #BT - So how do you convert Python dict to json string to send it over the http. This 
    #     is where the json.dumps/dump come into play.
    ########################################################################################

    #BT - Take the json_data(Python dict) convert it back to string. indemt=4 is just an option
    #     for pretty printing purposed.
    
    json_string = json.dumps(json_data, indent=4)

    print(type(json_string))

    print(json_string)