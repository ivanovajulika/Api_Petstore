import requests
import json
import allure
import logging


url = "https://petstore.swagger.io/v2"


class Pet:
    """Class Pet Methods"""

    def __init__(self):
        self.url = url

    def get_pet_by_id(self, id):
        """GET/pet/{petId} Find pet by ID"""
        response = requests.get(f"{url}/pet/{id}")
        status = response.status_code
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def get_pet_by_status(self, params):
        """GET/pet/findByStatus Finds Pets by status"""
        response = requests.get(f"{url}/pet/findByStatus?status={params}")
        status = response.status_code
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def post_update_pet(self, id, data):
        """POST/pet/{petId} Updates a pet in the store with form data"""
        response = requests.post(f"{url}/pet/{id}", data=data)
        status = response.status_code
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result

    def put_update_pet(self, data, headers):
        """PUT/pet Update an existing pet"""
        response = requests.post(f"{url}/pet", data=json.dumps(data), headers=headers)
        status = response.status_code
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"PUT request from url {response.request.path_url}"):
            return status, result

    def post_add_new_pet(self, data, headers):
        """POST/pet Add a new pet to the store"""
        response = requests.post(f"{url}/pet", data=json.dumps(data), headers=headers)
        status = response.status_code
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
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok} ")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result

    def post_uploads_image_path(self, id, headers, files):
        """POST/pet/{petId}/uploadImage uploads an image"""
        response = requests.post(f"{url}/pet/{id}/uploadImage", headers, files=files)
        status = response.status_code
        result = response.json()
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
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result

    def get_order_by_id(self, id):
        """GET/store/order/{orderId} Find order by ID"""
        response = requests.get(f"{url}/store/order/{id}")
        status = response.status_code
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def delete_order_by_id(self, id, headers):
        """DELETE/store/order/{orderId} Delete order by ID"""
        response = requests.delete(f"{url}/store/order/{id}", headers=headers)
        status = response.status_code
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
        result = response.json()
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result
