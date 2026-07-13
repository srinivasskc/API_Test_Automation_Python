import requests


class APIClient:
    BASE_URL = "https://fakerestapi.azurewebsites.net/"

    def __init__(self):
        self.header = {"accept": "text/plain; v=1.0"}

    def get(self, endpoint):
        get_url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url=get_url, headers=self.header, timeout=5000)
        return response
