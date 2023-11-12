import json
import requests


class BegetAPI:
    def __init__(self, login, password):
        self.base_url = "https://api.beget.com/v1"
        self.auth_url = f"{self.base_url}/auth"
        self.server_list_url = f"{self.base_url}/vps/server/list"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.login = login
        self.password = password
        self.jwt_token = None

    def authenticate(self):
        auth_data = {
            "login": self.login,
            "password": self.password,
            "saveMe": True
        }
        response = requests.post(self.auth_url, headers=self.headers, data=json.dumps(auth_data))
        response_data = response.json()
        self.jwt_token = response_data.get("token")

    def get_vps_list(self):
        if not self.jwt_token:
            self.authenticate()

        headers_with_auth = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.jwt_token}"
        }

        response = requests.get(self.server_list_url, headers=headers_with_auth)
        return response.json().get("vps")


class VPS:
    def __init__(self, vps_data):
        self.vps_id = vps_data.get("id")
        self.vps_ip = vps_data.get("ip_address")
        self.vps_configuration = vps_data.get("configuration")
        self.vps_cpu_count = self.vps_configuration.get("cpu_count")
        self.vps_disk_size = self.vps_configuration.get("disk_size")
        self.vps_memory = self.vps_configuration.get("memory")
        self.vps_status = vps_data.get("status")

    def display_info(self):
        print(f"id: {self.vps_id}\n"
              f"----------------------------\n"
              f"status: {self.vps_status}\n"
              f"ip: {self.vps_ip}\n"
              f"cpu count: {self.vps_cpu_count}\n"
              f"disk size: {self.vps_disk_size}\n"
              f"memory: {self.vps_memory}\n"
              f"----------------------------\n"
              )


# Пример использования
if __name__ == "__main__":
    beget_api = BegetAPI(login="", password="")
    vps_list = beget_api.get_vps_list()

    for vps_data in vps_list:
        vps_instance = VPS(vps_data)
        vps_instance.display_info()
