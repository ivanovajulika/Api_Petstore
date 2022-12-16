from api import Pet, Store, User
import pytest
import allure
import os


pet = Pet()

""" You can run all tests at once by selecting a file
pytest -s -v tests/test_pet.py """


@allure.epic("US_001.00.00 | Pet > Everything about your Pets")
class TestPets:
    def test_upload_image_path(self, id, headers):
        current_dir = os.path.abspath(
            os.path.dirname(__file__)
        )  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(
            current_dir, "Swagger.jpg"
        )  # добавляем к этому пути имя файла
        file = {
            "additionalMetadata": "Swagger.jpg",
            "file": ('Swagger.jpg"', open(file_path, "rb")),
            "Content-Type": "multipart/form-data",
            "type": "image/jpg",
        }
        status, result = pet.post_uploads_image(id, headers, files=file)
        print(result)

    @pytest.mark.parametrize(
        "status",
        ["available", "pending", "sold"],
        ids=["available", "pending", "sold"],
    )
    def test_post_add_new_pet(self, random_id, random_name, status, headers):
        data = {"id": random_id, "name": random_name, "status": status}
        status, result = pet.post_add_new_pet(data, headers)
        assert status == 200
        assert result["name"] == data["name"]
        print(result)
        pet.delete_pet(random_id, headers=headers)

    def test_get_pet_valid_id(self, id, random_name, headers):
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
    def test_get_pet_valid_status(self, status):
        """Parameterization is used here, 4 tests will run"""
        status_code, result = pet.get_pet_by_status(params=status)
        assert status_code == 200
        print(result)

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

store = Store()


@allure.epic("US_002.00.00 | Store > Access to Petstore orders")
class TestStore:
    def test(self):
        pass


user = User()


@allure.epic("US_003.00.00 | User > Operations about user")
class TestUser:
    def test_1(self):
        pass
