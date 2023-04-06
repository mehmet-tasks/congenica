import requests


class APIUtilities:
    base_url = "https://jsonplaceholder.typicode.com"

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.url = f"{self.base_url}/{self.endpoint}"

    def send_request(self, method, **kwargs):
        response = requests.request(method, **kwargs)
        return response
