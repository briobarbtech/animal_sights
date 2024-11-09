import requests
from entidades.data_managment import Ubicacion


def get_loc(api_key):
    response = requests.get(f"https://ipinfo.io?token={api_key}")
    if response.status_code == 200:
        data = response.json()
        return Ubicacion.from_json(data)
    else:
        return None
   