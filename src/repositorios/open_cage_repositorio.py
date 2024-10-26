import requests
import json

def obtener_ubicacion(api_key):
    ip_public = requests.get("https://api.ipify.org")
    response = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={ip_public}&key={api_key}")
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            result = data['results'][0]
            return Ubicacion(
                    formatted=result.get('formatted'),
                    geometry=result['geometry'],
                    city=result['components'].get('city'),
                    state=result['components'].get('state'),
                    country=result['components'].get('country')
                )
        else:
            return None
    else:
        return None

class Ubicacion:
    def __init__(self, formatted, geometry, city, state, country):
        self.formatted = formatted
        self.geometry = geometry
        self.city = city
        self.state = state
        self.country = country

    def toJson(self):
        return json.dumps({
            'direccion': self.formatted,
            'coordenadas': self.geometry,
            'ciudad': self.city,
            'region': self.state,
            'pais': self.country
        }, ensure_ascii=False, indent=4)
    def toList(self):
        return [self.formatted, self.geometry, self.city, self.state, self.country]

    @classmethod
    def fromList(cls, lista):
        if len(lista) != 5:
            raise ValueError("La lista debe contener exactamente 5 elementos.")
        return cls(
            formatted=lista[0],
            geometry=lista[1],
            city=lista[2],
            state=lista[3],
            country=lista[4]
        )
