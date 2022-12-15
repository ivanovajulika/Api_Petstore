import requests
import json
import allure

# from requests_toolbelt.multipart.encoder import MultipartEncoder

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
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def get_pet_by_status(self, params):
        """GET/pet/findByStatus Finds Pets by status"""
        response = requests.get(f"{url}/pet/findByStatus?status={params}")
        status = response.status_code
        result = response.json()
        with allure.step(f"GET request from url {response.request.path_url}"):
            return status, result

    def post_update_pet(self, id, data):
        """POST/pet/{petId} Updates a pet in the store with form data"""
        response = requests.post(f"{url}/pet/{id}", data=data)
        status = response.status_code
        result = response.json()
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result

    def put_update_pet(self, data, headers):
        """PUT/pet Update an existing pet"""
        response = requests.post(f"{url}/pet", data=json.dumps(data), headers=headers)
        status = response.status_code
        result = response.json()
        with allure.step(f"PUT request from url {response.request.path_url}"):
            return status, result

    def post_add_new_pet(self, data, headers):
        """POST/pet Add a new pet to the store"""
        response = requests.post(f"{url}/pet", data=json.dumps(data), headers=headers)
        status = response.status_code
        result = response.json()
        with allure.step(f"POST request from url {response.request.path_url}"):
            return status, result

    def delete_pet(self, id, headers):
        """DELETE/pet/{petId} Deletes a pet"""
        response = requests.delete(f"{url}/pet/{id}", headers=headers)
        status = response.status_code
        result = response.json()
        with allure.step(f"DELETE request from url {response.request.path_url}"):
            return status, result

    """Here we will fix the method when we figure out how to send the file"""
    # def post_uploads_image(self, id, pet_photo, headers):
    #         """POST/pet/{petId}/uploadImage uploads an image"""
    #         data = MultipartEncoder(
    #             fields={'file': (pet_photo, open(pet_photo, 'rb'))})

    #         response = requests.post(f"{url}/pet/{id}/uploadImage", data, headers)
    #         status = response.status_code
    #         result = response.json()
    #         return status, result
