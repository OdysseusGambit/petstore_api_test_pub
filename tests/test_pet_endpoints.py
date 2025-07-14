import logging
import random
import pytest
from api import pet_api

@pytest.fixture
def pet_data():
        pet_id = random.randint(99999, 100000)
        logging.info(f"Generated pet ID: {pet_id}")
        return {
            "id": pet_id,
            "name": "Pesek",
            "status": "available"
    }

def test_update_pet(pet_data):
    pet_api.add_pet(pet_data)
    pet_data["name"] = "Bleki"
    response = pet_api.update_pet(pet_data)
    logging.info(f"response: {response.json()}")
    assert response.status_code == 200
    assert response.json()["name"] == "Bleki"

def test_add_pet(pet_data):
    response = pet_api.add_pet(pet_data)
    logging.info(f"response: {response.json()}")
    assert response.status_code == 200
    assert response.json()["name"] == pet_data["name"]

def test_get_pet(pet_data):
    pet_api.add_pet(pet_data)
    response = pet_api.get_pet(pet_data["id"])
    logging.info(f"response: {response.json()}")
    assert response.status_code == 200
    assert response.json()["id"] == pet_data["id"]