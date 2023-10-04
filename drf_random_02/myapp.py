import requests
import json

URL = "http://127.0.0.1:8000/create-record/"

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

if r.status_code == 200:
    try:
        response_data = r.json()
        print("Response:", response_data)
    except json.JSONDecodeError:
        print("Server response is not valid JSON.")
else:
    print(f"Request failed with status code: {r.status_code}")
