import requests

url = "http://127.0.0.1:5000/predict"

# Replace with actual feature names used in model training
data = {
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984126984,
    "AveBedrms": 1.023809524,
    "Population": 322.0,
    "AveOccup": 2.555555556,
    "Latitude": 37.88,
    "Longitude": -122.23
}

response = requests.post(url, json=data)
print("Response:", response.json())
