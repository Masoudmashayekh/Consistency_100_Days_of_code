import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}


URL = "https://opentdb.com/api.php"

response = requests.get(url= URL, params= parameters)
response.raise_for_status()

question_data = response.json()["results"]

def hi(age: int):
    print("heloo")
    
    
