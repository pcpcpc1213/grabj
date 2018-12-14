#json test

import json
import requests # we need this to request the data

def getjson(url="https://jsonplaceholder.typicode.com/todos/1", call="title"):
    r = requests.get(url) # url to get data from
    r = r.json() # converted to json so now, the json data is a python dictionary.
    print(r[call]) # notice how we can pull data from it like a normal dictionary
