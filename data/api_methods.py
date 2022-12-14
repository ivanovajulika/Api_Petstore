from data.api_request import APIRequest
from data.api_data import RequestData as d


class Pet(APIRequest):
    def __init__(self, path=""):
        super().__init__()
        self.endpoint = "pet"
        self.path = path
        self.response = APIRequest()

    # def setup(self):
    #     payload = [
    #         ({"status": "sold"}),
    #         ({"status": "pending"}),
    #         ({"status": "available"}),
    #     ]
    params = {"status": "sold"}

    def post_upload_image(self, path=f"{11}/uploadImage", files=d.multiple_files, headers=d.headers):
        return self.post(self.endpoint, path, files, headers)

    def post_add_a_new_pet(self):
        return self.post(self.endpoint)

    def put_update_pet(self, json):
        return self.put(self.endpoint, json)

    def get_find_by_status(self, path="findByStatus", params=params):
        return self.get(self.endpoint, path, params)

    def get_find_pet_by_id(self, path=f"/{d.random_id}"):
        return self.get(self.endpoint, path)

    def post_update_pet_by_id(self, path=f"/{d.random_id}"):
        return self.post(self.endpoint, path)

    def delete_pet_by_id(self, path=f"/{d.random_id}"):
        return self.delete(self.endpoint, path)


class Store(APIRequest):
    def __init__(self, path=""):
        super().__init__()
        self.endpoint = "store"
        self.path = path
        self.response = APIRequest()

    def post_place_an_order(self, path=f"/order"):
        return self.post(self.endpoint, path)

    def get_find_order_by_id(self, path=f"/order/{d.random_order_id}"):
        return self.get(self.endpoint, path)

    def delete_order_by_id(self, path=f"/order/{d.random_order_id}"):
        return self.delete(self.endpoint, path)

    def get_return_pet_inventory_by_status(self, path="inventory"):
        return self.get(self.endpoint, path)


class User(APIRequest):
    def __init__(self, path=""):
        super().__init__()
        self.endpoint = "user"
        self.path = path
        self.response = APIRequest()

    def post_create_list_users_array(self, path="createWithArray"):
        return self.get(self.endpoint, path)

    def post_create_list_users_list(self, path="createWithList"):
        return self.get(self.endpoint, path)

    def get_user_by_username(self, path=f"{d.random_name}"):
        return self.get(self.endpoint, path)

    def put_user_by_username(self, path=f"{d.random_name}"):
        return self.put(self.endpoint, path)

    def delete_user_by_username(self, path=f"{d.random_name}"):
        return self.delete(self.endpoint, path)

    def get_logs_user(self, path="login"):
        return self.get(self.endpoint, path)

    def get_logs_out_user(self, path="logout"):
        return self.delete(self.endpoint, path)

    def post_create_user(self):
        return self.delete(self.endpoint)
