import requests

class LinkedInService:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.linkedin.com/v2"

    def get_profile(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.base_url}/me", headers=headers)
        return response.json()

