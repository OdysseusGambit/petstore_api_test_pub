import requests
from utils.config import BASE_URL, HEADERS

def add_pet(data):
    return requests.post(f"{BASE_URL}/pet", json=data, headers=HEADERS)

def get_pet(pet_id):
    return requests.get(f"{BASE_URL}/pet/{pet_id}", headers=HEADERS)

def update_pet(data):
    return requests.put(f"{BASE_URL}/pet", json=data, headers=HEADERS)
