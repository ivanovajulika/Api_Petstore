import requests
import os

def test_pet_upload(photo="picture/34566.jpg"):
    url1 = "https://petstore.swagger.io/v2/pet/88/uploadImage"
    photo = os.path.join(os.path.dirname(__file__), photo)
    photo = photo.replace("\\", "/")
    print(photo)
    files = {
        "file": ("sampleFile", open(photo, "rb")),
        "Content-Type": "multipart/form-data",
    }
    response = requests.post(url=url1, files=files)
    print(response.status_code)
    print(response.json())
