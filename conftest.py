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
def random_user_id():
    return random.randrange(1, 1000)


@pytest.fixture
def order_id():
    return 5


@pytest.fixture
def user_id():
    return 7


@pytest.fixture
def id():
    return 88


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
def headers():
    return {"accept": "application/json", "Content-Type": "application/json"}
