import json
import logging
import allure
import requests
from jsonschema import validate

url = "https://petstore.swagger.io/v2"

pet_schema = {
    "required": ["name", "photoUrls"],
    "properties": {
        "id": {"type": "integer", "format": "int64"},
        "category": {"$ref": "#/definitions/Category"},
        "name": {"type": "string", "example": "doggie"},
        "photoUrls": {
            "type": "array",
            "xml": {"name": "photoUrl", "wrapped": True},
            "items": {"type": "string"},
        },
        "tags": {
            "type": "array",
            "xml": {"name": "tag", "wrapped": True},
            "items": {"$ref": "#/definitions/Tag"},
        },
        "status": {
            "type": "string",
            "description": "pet status in the store",
            "enum": ["available", "pending", "sold"],
        },
    },
}


def validate_json(data):
    try:
        loaded = json.loads(data)
    except ValueError as e:
        logging.error(e)
        return False
    return True


def validate_json_schema(data):
    try:
        validate(instance=data, schema=pet_schema)
    except ValueError as e:
        logging.error(e)
        return False
    return True


class Pet:
    """Class Pet Methods"""

    def __init__(self):
        self.url = url

    def get_pet_by_id(self, id):
        """GET/pet/{petId} Find pet by ID"""
        response = requests.get(f"{url}/pet/{id}")
        status = response.status_code
        data = response.content
        if id != '':
            assert validate_json(data) is True
        assert validate_json_schema(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def get_pet_by_status(self, params):
        """GET/pet/findByStatus Finds Pets by status"""
        response = requests.get(f"{url}/pet/findByStatus?status={params}")
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        assert validate_json_schema(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def post_update_pet(self, id, data):
        """POST/pet/{petId} Updates a pet in the store with form data"""
        response = requests.post(f"{url}/pet/{id}", data=data)
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        assert validate_json_schema(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result

    def put_update_pet(self, data, headers):
        """PUT/pet Update an existing pet"""
        response = requests.post(f"{url}/pet", data=json.dumps(data), headers=headers)
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        assert validate_json_schema(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"PUT request from url {response.request.path_url}"):
            return status, result

    def post_add_new_pet(self, data, headers):
        """POST/pet Add a new pet to the store"""
        response = requests.post(f"{url}/pet", data=json.dumps(data), headers=headers)
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        assert validate_json_schema(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result

    def delete_pet(self, id, headers):
        """DELETE/pet/{petId} Deletes a pet"""
        response = requests.delete(f"{url}/pet/{id}", headers=headers)
        status = response.status_code
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"DELETE request from url {response.request.path_url}"):
            return status, result

    def post_uploads_image(self, id, photo):
        """POST/pet/{petId}/uploadImage uploads an image"""
        files = {
            "file": ("photo", open(photo, "rb")),
            "Content-Type": "multipart/form-data",
        }
        response = requests.post(f"{url}/pet/{id}/uploadImage", files=files)
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        assert validate_json_schema(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok} ")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result

    def post_uploads_image_path(self, id, headers, files):
        """POST/pet/{petId}/uploadImage uploads an image"""
        response = requests.post(f"{url}/pet/{id}/uploadImage", headers, files=files)
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        assert validate_json_schema(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok} ")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result


class Store:
    """Class Store Methods"""

    def __init__(self):
        self.url = url

    def get_store_inventory(self):
        """GET/store/inventory Returns pet inventories by status"""
        response = requests.get(f"{url}/store/inventory")
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def post_order(self, data, headers):
        """POST/store/order Place an order for a pet"""
        response = requests.post(
            f"{url}/store/order", data=json.dumps(data), headers=headers
        )
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result

    def get_order_by_id(self, id):
        """GET/store/order/{orderId} Find order by ID"""
        response = requests.get(f"{url}/store/order/{id}")
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def delete_order_by_id(self, id, headers):
        """DELETE/store/order/{orderId} Delete order by ID"""
        response = requests.delete(f"{url}/store/order/{id}", headers=headers)
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"DELETE request from url {response.request.path_url}"):
            return status, result


class User:
    """Class User Methods"""

    def __init__(self):
        self.url = url

    def post_new_user(self, data, headers):
        """POST/user Create user"""
        response = requests.post(f"{url}/user", data=json.dumps(data), headers=headers)
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result

    def get_user_by_username(self, username):
        """GET/user/{username} Find user by username"""
        response = requests.get(f"{url}/user/{username}")
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def delete_user_by_username(self, username, headers):
        """DELETE/user/{username} Delete user by username"""
        response = requests.delete(f"{url}/user/{username}", headers=headers)
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"DELETE request from url {response.request.path_url}"):
            return status, result

    def put_update_user_by_username(self, username, headers, data):
        """PUT/user/{username} Update user by username"""
        response = requests.put(
            f"{url}/user/{username}", data=json.dumps(data), headers=headers
        )
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"DELETE request from url {response.request.path_url}"):
            return status, result

    def get_user_login(self, params, headers):
        """GET/user/login"""
        response = requests.get(f"{url}/user/login", params=params, headers=headers)
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def get_user_logout(self, headers):
        """GET/user/login"""
        response = requests.get(f"{url}/user/logout", headers=headers)
        status = response.status_code
        data = response.content
        assert validate_json(data) is True
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result
