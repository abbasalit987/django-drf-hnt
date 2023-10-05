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


getData()
