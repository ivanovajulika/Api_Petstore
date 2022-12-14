import string
import random
import os


class RequestData:
    random_name = (
        "".join(random.choice(string.ascii_lowercase) for _ in range(8))
    ).title()
    random_id = random.randrange(1, 100)
    random_order_id = random.randrange(1, 10)
    create_random_id = random.randrange(101, 1000)
    data = {
        "id": random_id,
        "category": {"id": 0, "name": "string"},
        "name": random_name,
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }

    def put_data(self):
        return {"id": 650, "name": "Barsik", "status": "available"}

    data2 = {"id": 650, "name": "Barsik", "status": "available"}
    update_data = {"name": "Bobik", "status": "sold"}
    upload_data = {"additionalMetadata": "xml"}
    store_data = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2022-12-08T09:10:58.100Z",
        "status": "placed",
        "complete": True
    }
    current_dir = os.path.abspath(
        os.path.dirname(__file__)
    )  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(
        current_dir, "Swagger.jpg"
    )  # добавляем к этому пути имя файла
    print(file_path)
    headers = {'Content-Type': 'multipart/form-data'}
    files = {'Swagger.jpg': open('Swagger.jpg', 'rb')}
    multiple_files = {'images', ('Swagger.jpg', open(file_path, 'rb'), 'image/jpg')}