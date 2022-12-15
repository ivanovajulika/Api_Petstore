import random
import string
import pytest


@pytest.fixture
def random_id():
    return random.randrange(1, 1000)


@pytest.fixture
def random_order_id():
    return random.randrange(1, 10)


@pytest.fixture
def order_id():
    return 5


@pytest.fixture
def id():
    return 888


@pytest.fixture
def random_name(num=8):
    return ("".join(random.choice(string.ascii_lowercase) for _ in range(num))).title()


@pytest.fixture(params=["available", "pending", "sold"])
def update_data(random_name, request):
    return {"name": random_name, "status": request.param}


@pytest.fixture(params=["available", "pending", "sold"])
def put_data(id, random_name, request):
    return {"id": id, "name": random_name, "status": request.param}


@pytest.fixture
def headers(k="default"):
    if k == "default":
        return {"accept": "application/json", "Content-Type": "application/json"}
    elif k == "key":
        return {
            "api_key": "special-key",
            "accept": "application/json",
            "Content-Type": "application/json",
        }
    elif k == "file":
        return {"accept": "application/json", "Content-Type": "multipart/form-data"}


# params = {"status": "available"}
