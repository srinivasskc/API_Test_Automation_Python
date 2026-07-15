import requests


class APIClient:
    BASE_URL = "https://fakerestapi.azurewebsites.net/"

    def __init__(self):
        self.header = {"accept": "text/plain; v=1.0"}

    def get_activities(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url=url, headers=self.header, timeout=5000)
        return response

    def post_activities(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url=url, headers=self.header, json=data, timeout=5000)
        return response
