import string
import random
import os

import pytest


class RequestData:
    random_name = (
        "".join(random.choice(string.ascii_lowercase) for _ in range(8))
    ).title()
    random_id = random.randrange(1, 100)
    random_order_id = random.randrange(1, 10)
    create_random_id = random.randrange(101, 1000)
    data = {
        "id": random_id,
        "category": {"id": 0, "name": "string"},
        "name": random_name,
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }

    def put_data(self):
        return {"id": 650, "name": "Barsik", "status": "available"}

    data2 = {"id": 650, "name": "Barsik", "status": "available"}
    update_data = {"name": "Bobik", "status": "sold"}
    upload_data = {"additionalMetadata": "xml"}
    store_data = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2022-12-08T09:10:58.100Z",
        "status": "placed",
        "complete": True,
    }



@pytest.fixture
def random_id():
    return random.randrange(1, 100)


@pytest.fixture
def random_name():
    return ("".join(random.choice(string.ascii_lowercase) for _ in range(8))).title()


@pytest.fixture(params=["available", "pending", "sold"])
def pet_data(random_id, random_name, request):
    data = {
        "id": random_id,
        "category": {"id": 0, "name": "string"},
        "name": random_name,
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": request.param,
    }
    return data
