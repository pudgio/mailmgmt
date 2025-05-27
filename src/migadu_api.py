import requests

class MigaduAPI:
    def __init__(self, api_key, domain):
        self.api_key = api_key
        self.domain = domain
        self.base_url = f"https://api.migadu.com/v1/domains/{self.domain}/mailboxes"

    def create_mailbox(self, local_part, password):
        data = {
            "local_part": local_part,
            "password": password
        }
        response = requests.post(
            self.base_url,
            auth=(self.api_key, ""),
            json=data
        )
        return response.json()

    def delete_mailbox(self, local_part):
        url = f"{self.base_url}/{local_part}"
        response = requests.delete(
            url,
            auth=(self.api_key, "")
        )
        if response.status_code != 204:
            print("Error:", response.status_code, response.text)
        return response.status_code == 204