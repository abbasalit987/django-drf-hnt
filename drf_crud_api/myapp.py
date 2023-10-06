import json
import requests

URL = "http://127.0.0.1:8000/crud-api/"


def getData(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    jsonData = json.dumps(data)
    r = requests.get(url=URL, data=jsonData)
    rData = r.json()
    print(rData)


# getData()

def postData():
    data = {
        "created_at": "2023-10-04T11:30:15.123456Z",
        "first_name": "Ethan",
        "last_name": "Lopez",
        "email": "ethan.l@example.com",
        "phone": "(555) 444-3333",
        "address": "555 Oak St",
        "city": "Detroit",
        "state": "MI",
        "pincode": "48201"
    }
    jsonData = json.dumps(data)
    r = requests.post(url=URL, data=jsonData)
    rData = r.json()
    print(rData)


# postData()

def updateData():
    data = {
        "id": "2",
        "first_name": "Meems",
        "last_name": "Kunwar",
        "email": "meems.k@example.com",
        "phone": "(555) 444-7777",
        "address": "555 Oak St",
        "city": "Detroit",
        "state": "MI",
        "pincode": "48201"
    }
    jsonData = json.dumps(data)
    r = requests.put(url=URL, data=jsonData)
    rData = r.json()
    print(rData)


updateData()
