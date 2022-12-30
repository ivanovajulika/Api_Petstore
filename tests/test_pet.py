from requests import JSONDecodeError
from api import Pet
import pytest
import allure
import os


pet = Pet()

""" You can run all tests at once by selecting a file
pytest -s -v tests/test_pet.py """


@allure.epic("US_001.00.00 | Pet > Everything about your Pets")
class TestPets:
    @pytest.mark.parametrize(
        "status",
        ["available", "pending", "sold"],
        ids=["available", "pending", "sold"],
    )
    @allure.feature("TS_001.02.00 | Pet > Everything about your Pets")
    @allure.story("TC_001.02.01| Pet> POST 'Add a new pet to the store'")
    def test_post_add_new_pet(self, random_id, random_name, status, headers):
        data = {"id": random_id, "name": random_name, "status": status}
        status, result = pet.post_add_new_pet(data, headers)
        assert status == 200
        assert result["name"] == data["name"]
        pet.delete_pet(random_id, headers=headers)

    @allure.feature("TS_001.04.00 | Pet > {petId}")
    @allure.story("TC_001.04.06| Pet > {petId}> GET 'Find pet by valid ID'")
    def test_get_pet_valid_id(self, id, random_name, headers):
        status, result = pet.get_pet_by_id(id)
        if status != 200:
            data = {"id": id, "name": random_name, "status": "available"}
            pet.post_add_new_pet(data, headers)
            status, result = pet.get_pet_by_id(id)
            assert result["id"] == data['id']
        assert status == 200
        assert result["id"] == id

    @allure.feature("TS_001.04.00 | Pet > {petId}")
    @allure.story("TC_001.04.08| Pet > {petId}> GET 'Find pet by invalid ID'")
    @pytest.mark.parametrize(
        "pet_id",
        ["abc", "абв", "   ", "@"],
        ids=["string", "kirill_string", "witespace", "simbol"],
    )
    def test_get_pet_invalid_id(self, pet_id, random_name, headers):
        """Parameterization is used here, 4 tests will run"""
        status, result = pet.get_pet_by_id(pet_id)
        assert status == 404

    @allure.feature("TS_001.04.00 | Pet > {petId}")
    @allure.story(
        "TC_001.04.09| Pet > {petId}> GET 'Find pet by invalid ID (ID is empty)'"
    )
    @pytest.mark.parametrize("pet_id", [""], ids=["empty"])
    def test_get_pet_id_is_empty(self, pet_id, random_name, headers):
        with pytest.raises(JSONDecodeError):
            status, result = pet.get_pet_by_id(pet_id)
            pytest.fail("ID is empty")
            assert status == 405

    @pytest.mark.parametrize(
        "status",
        ["available", "pending", "sold"],
        ids=["available", "pending", "sold"],
    )
    @allure.feature("TS_001.03.00 | Pet > {petId}/findByStatus")
    @allure.feature("TC_001.03.01 PET> GET 'Find pets by  valid status'")
    def test_get_pet_valid_status(self, status):
        """Parameterization is used here, 4 tests will run"""
        status_code, result = pet.get_pet_by_status(params=status)
        assert status_code == 200

    @pytest.mark.parametrize(
        "status",
        [
            "",
            "@",
            "   ",
            "beautifull",
            pytest.param("string", marks=pytest.mark.xfail(reason="status is string")),
        ],
        ids=["empty", "simbol", "witespace", "non-existent status", "default"],
    )
    @allure.feature("TS_001.03.00 | Pet > {petId}/findByStatus")
    @allure.story("TC_001.03.02 PET> GET 'Find pets by  invalid status'")
    def test_get_pet_invalid_status(self, status):
        """Parameterization is used here, 4 tests will run"""
        status_code, result = pet.get_pet_by_status(params=status)
        assert status_code == 200
        assert result == []

    def test_post_update_pet(self, id, random_name, headers, update_data):
        status, result = pet.get_pet_by_id(id)
        if status != 200:
            data = {"id": id, "name": random_name, "status": "available"}
            status, result = pet.post_add_new_pet(data, headers)
        status, result = pet.post_update_pet(id, data=update_data)
        assert status == 200
        status, result = pet.get_pet_by_id(id)
        assert result["name"] == update_data["name"]
        print(result["name"])

    def test_put_update_pet(self, id, put_data, headers):
        status, result = pet.put_update_pet(put_data, headers)
        assert status == 200
        status, result = pet.get_pet_by_id(id)
        assert result["name"] == put_data["name"]
        print(result["name"])

    def test_delete_pet(self, id, random_name, headers):
        status, result = pet.get_pet_by_id(id)
        if status != 200:
            data = {"id": id, "name": random_name, "status": "available"}
            status, result = pet.post_add_new_pet(data, headers)
        status, result = pet.delete_pet(id, headers)
        assert status == 200
        assert int(result["message"]) == id
        status, result = pet.get_pet_by_id(id)
        assert status == 404

    def test_uploads_image(self, id, random_name, headers, photo="picture/34566.jpg"):
        status, result = pet.get_pet_by_id(id)
        if status != 200:
            data = {"id": id, "name": random_name, "status": "available"}
            status, result = pet.post_add_new_pet(data, headers)
        photo = os.path.join(os.path.dirname(__file__), photo)
        status, result = pet.post_uploads_image(id, photo)
        assert status == 200
        print(result["message"])

    def test_upload_image_path(self, id, headers):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, "picture/Swagger.jpg")
        file = {
            "additionalMetadata": "Swagger.jpg",
            "file": ('Swagger.jpg"', open(file_path, "rb")),
            "Content-Type": "multipart/form-data",
            "type": "image/jpg",
        }
        status, result = pet.post_uploads_image_path(id, headers, files=file)
        assert status == 200
        print(result)
