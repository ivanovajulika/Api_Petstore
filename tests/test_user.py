from api import User

user = User()

""" You can run all tests at once by selecting a file
pytest -s -v tests/test_pet.py """


def test_post_new_user_by_id(random_user_id, headers):
    """Creates new user with id, verifies if the user is created"""
    data = {"id": random_user_id, "type": "unknown", "message": random_user_id}
    status, result = user.post_new_user(data, headers)
    print(result)
    assert status == 200
    assert result["message"] == f"{random_user_id}"


def test_post_new_user_by_username(user_id, random_name, headers):
    """Creates new user with username, verifies if the user is created"""
    data = {"id": user_id, "username": random_name, "type": "unknown"}
    status, result = user.post_new_user(data, headers)
    print(result)
    assert status == 200
    assert result["message"] == f"{user_id}"
