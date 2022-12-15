from api import Pet
import pytest


pet = Pet()


""" You can run all tests at once by selecting a file
pytest -s -v tests/test_pet.py """


@pytest.mark.parametrize(
    "status",
    ["available", "pending", "sold"],
    ids=["available", "pending", "sold"],
)
def test_post_add_new_pet(random_id, random_name, status, headers):
    data = {"id": random_id, "name": random_name, "status": status}
    status, result = pet.post_add_new_pet(data, headers)
    assert status == 200
    assert result["name"] == data["name"]
    print(result)
    pet.delete_pet(random_id, headers=headers)


def test_get_pet_valid_id(id, random_name, headers):
    status, result = pet.get_pet_by_id(id)
    if status != 200:
        data = {"id": id, "name": random_name, "status": "available"}
        pet.post_add_new_pet(data, headers)
        status, result = pet.get_pet_by_id(id)
    print(result)
    assert status == 200


@pytest.mark.parametrize(
    "status",
    ["", "available", "pending", "sold"],
    ids=["empty", "available", "pending", "sold"],
)
def test_get_pet_valid_status(status):
    """Parameterization is used here, 4 tests will run"""
    status, result = pet.get_pet_by_status(params=status)
    assert status == 200
    print(result)


def test_post_update_pet(id, random_name, headers, update_data):
    status, result = pet.get_pet_by_id(id)
    if status != 200:
        data = {"id": id, "name": random_name, "status": "available"}
        status, result = pet.post_add_new_pet(data, headers)
    status, result = pet.post_update_pet(id, data=update_data)
    assert status == 200
    status, result = pet.get_pet_by_id(id)
    assert result["name"] == update_data["name"]
    print(result["name"])


def test_put_update_pet(id, put_data, headers):
    status, result = pet.put_update_pet(put_data, headers)
    assert status == 200
    status, result = pet.get_pet_by_id(id)
    assert result["name"] == put_data["name"]
    print(result["name"])


def test_delete_pet(id, random_name, headers):
    status, result = pet.get_pet_by_id(id)
    if status != 200:
        data = {"id": id, "name": random_name, "status": "available"}
        status, result = pet.post_add_new_pet(data, headers)
    status, result = pet.delete_pet(id, headers)
    assert status == 200
    assert int(result["message"]) == id
    status, result = pet.get_pet_by_id(id)
    assert status == 404


"""Here we will fix the test when we figure out how to send the file"""
# def test_uploads_image(pet_photo='images/cat1.jpg'):
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#     headers = headers_mult
#     status, result = pet.post_uploads_image(id, pet_photo, headers('file'))
#     assert status == 200
#     print(result["message"])
