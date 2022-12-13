from api import Pet
from api_data import *
import pytest

pet = Pet()

""" You can run all tests at once by selecting a file
pytest -s -v tests/tests_pet.py """


def test_post_add_new_pet():
    status, result = pet.post_add_new_pet(data, headers)
    assert status == 200
    assert result["name"] == data["name"]
    print(result["name"])


def test_get_pet_valid_id():
    status, result = pet.get_pet_by_id(id)
    assert status == 200
    print(result)


@pytest.mark.parametrize(
    "params",
    ["", "available", "pending", "sold"],
    ids=["empty", "available", "pending", "sold"],
)
def test_get_pet_valid_status(params):
    """Parameterization is used here, 4 tests will run"""
    status, result = pet.get_pet_by_status(params=params)
    assert status == 200
    print(result)


def test_post_update_pet():
    status, result = pet.post_update_pet(id, data=update_data)
    assert status == 200
    status, result = pet.get_pet_by_id(id)
    assert result["name"] == update_data["name"]
    print(result["name"])


def test_put_update_pet():
    status, result = pet.put_update_pet(update_data_2, headers)
    assert status == 200
    status, result = pet.get_pet_by_id(id)
    assert result["name"] == update_data_2["name"]
    print(result["name"])


def test_delete_pet():
    status, result = pet.delete_pet(id, headers)
    assert status == 200
    assert int(result["message"]) == id
    status, result = pet.get_pet_by_id(id)
    assert status == 404


"""Here we will fix the test when we figure out how to send the file"""
# def test_uploads_image(pet_photo='images/cat1.jpg'):
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#     headers = headers_mult
#     status, result = pet.post_uploads_image(id, pet_photo, headers)
#     assert status == 200
#     print(result["message"])
