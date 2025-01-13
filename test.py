import requests

url = "http://localhost:4001/predict"
data = {
    "square_meters": 100.0,
    "floors": 2,
    "sleeping_rooms": 3,
    "bathrooms": 2
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())