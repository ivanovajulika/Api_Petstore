import requests
import json


class Requests:
    @staticmethod
    def get(url, data=None, headers=None, cookies=None):
        return Requests._send(url, data, headers, cookies, "GET")

    def post(url, data=None, headers=None, cookies=None):
        return Requests._send(url, data, headers, cookies, "POST")

    def put(url, data=None, headers=None, cookies=None):
        return Requests._send(url, data, headers, cookies, "PUT")

    def delete(url, data=None, headers=None, cookies=None):
        return Requests._send(url, data, headers, cookies, "DELETE")

    @staticmethod
    def _send(url, data, headers, cookies, method):
        url = f"https://petstore.swagger.io/v2{url}"

        if data is None:
            data = {}
        elif headers is None:
            headers = {}
        elif cookies is None:
            cookies = {}

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(
                url, data=json.dumps(data), headers=headers, cookies=cookies
            )
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Very bad method '{method}'")

        return response
