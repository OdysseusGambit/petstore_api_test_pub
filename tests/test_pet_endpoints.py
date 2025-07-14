import uuid
import pytest
from api import pet_api

@pytest.fixture
def pet_data():
    return {
        "id": int(uuid.uuid4().int % 100000),
        "name": "Fluffy",
        "status": "available"
    }

def test_add_pet(pet_data):
    response = pet_api.add_pet(pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == pet_data["name"]

def test_get_pet(pet_data):
    pet_api.add_pet(pet_data)
    response = pet_api.get_pet(pet_data["id"])
    assert response.status_code == 200
    assert response.json()["id"] == pet_data["id"]

def test_update_pet(pet_data):
    pet_api.add_pet(pet_data)
    pet_data["name"] = "Snowball"
    response = pet_api.update_pet(pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Snowball"
