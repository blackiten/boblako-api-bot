import json
import requests

url = "https://api.beget.com/v1/auth"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

data = {
    "login": "login",
    "password": "password",
    "saveMe": True
}

response = requests.post(url, headers=headers, data=json.dumps(data))
response_data = response.json()
jwtToken = response_data.get("token")

url = "https://api.beget.com/v1/vps/server/list"
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

response = requests.get(url, headers=headers)

vpsList = response.json().get("vps")

for vps in vpsList:
    vps_id = vps.get("id")
    vps_ip = vps.get("ip_address")

    vps_configuration = vps.get("configuration")

    vps_cpu_count = vps_configuration.get("cpu_count")
    vps_disk_size = vps_configuration.get("disk_size")
    vps_memory = vps_configuration.get("memory")

    vps_status = vps.get("status")

    print(f"id: {vps_id}\n"
          f"----------------------------\n"
          f"status: {vps_status}\n"
          f"ip: {vps_ip}\n"
          f"cpu count: {vps_cpu_count}\n"
          f"disk size: {vps_disk_size}\n"
          f"memory: {vps_memory}\n"
          f"----------------------------\n"
          )
