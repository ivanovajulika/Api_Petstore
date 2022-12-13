from api import Requests
from api_data import *

""" You can run all tests at once by selecting a file
pytest -s -v tests/tests_pet.py """


def test_post_add_new_pet():
    response = Requests.post("/pet", data, headers)
    assert response.status_code == 200
    assert (response.json())["name"] == data["name"]
    print((response.json())["name"])


def test_get_pet_valid_id():
    response = Requests.get(f"/pet/{id}")
    assert response.status_code == 200
    print(response.content)
