import allure

from api import User
import pytest
import random
import string

user = User()

# """ You can run all tests at once by selecting a file
# pytest -s -v tests/test_pet.py """
#
#
# # def random_user_id():
# #     return random.randrange(1, 1000)
#
#
# # def random_name(num=8):
# #     return ("".join(random.choice(string.ascii_lowercase) for _ in range(num))).title()
#
#
# @allure.epic("US_003.00.00 | User > Operations about user - positive")
# @pytest.mark.parametrize(
#     "id",
#     [random_user_id()],
#     ids=["random"],
# )
# @pytest.mark.parametrize(
#     "name",
#     [random_name().upper(), random_name().lower()],
#     ids=["upper", "lower"],
# )
# def test_post_new_user_positive(id, name, headers):
#     """Creates new user, verifies if the user is created"""
#     data = {"id": id, "username": name, "message": id}
#     status, result = user.post_new_user(data, headers)
#     assert status == 200
#     assert result["message"] == f"{id}"
#     status, result = user.get_user_by_username(name)
#     assert status == 200
#     assert result["username"] == f"{name}"
#     status, result = user.delete_user_by_username(name, headers)
#     assert status == 200
#     status, result = user.get_user_by_username(name)
#     assert status == 404
#
#
# @allure.epic("US_003.00.00 | User > Operations about user - negative")
# @pytest.mark.xfail
# @pytest.mark.parametrize(
#     "user_id",
#     ["", "blabla", "-6", "67 97 ", "$%^"],
#     ids=["empty", "string", "negative", "whitespace", "simbols"],
# )
# @pytest.mark.parametrize(
#     "name",
#     ["", "Анролрa", "-6", "67 97 ", "$%^", random_name(1000)],
#     ids=[
#         "empty",
#         "russian_string",
#         "negative_integer",
#         "whitespace_integer",
#         "simbols",
#         "very_long_name",
#     ],
# )
# def test_post_new_user_negative(user_id, name, headers):
#     """Creates new user, verifies if the user is created"""
#     data = {"id": user_id, "username": name, "message": user_id}
#     status, result = user.post_new_user(data, headers)
#     assert status == 200
#     assert result["message"] == f"{user_id}"
#     status, result = user.get_user_by_username(name)
#     assert status == 200
#     assert result["username"] == f"{name}"
#     status, result = user.delete_user_by_username(name, headers)
#     assert status == 200
#     status, result = user.get_user_by_username(name)
#     assert status == 404


def test_put_user(random_user_id, random_name, headers):
    """Create user, update user, verifies if the user is updated"""
    data = {"id": random_user_id, "username": random_name}
    status, result = user.post_new_user(data, headers)
    assert status == 200
    print(random_name, random_user_id)
    print(result['message'])
    data = {"username": 'Mikelandjelo'}
    status, result = user.put_update_user_by_username(
        username=random_name, headers=headers, data=data
    )
    assert status == 200
    print(result)
    status, result = user.get_user_by_username(username='Mikelandjelo')
    assert status == 200
    print(result)
