import requests

def get_loc():
    response = requests.get("https://ipinfo.io/")
    if response.status_code == 200:
        data = response.json()

        return Ubicacion.from_json(data)
    else:
        return None

class Ubicacion:
    def __init__(self, city, region,country,loc):
        self.city = city 
        self.region = region
        self.country = country
        self.loc = loc
    def mostrar_info(self):
        print(f"Ciudad: {self.city}")
        print(f"Región: {self.region}")
        print(f"País: {self.country}")
        print(f"Coordenadas: {self.loc}")

    @classmethod
    def from_json(cls, data_json):
        city = data_json.get('city')
        region = data_json.get('region')
        country = data_json.get('country')
        loc = data_json.get('loc')
        
        return cls(city, region, country, loc)
    def to_list(self):
        return [self.city, self.region, self.country, self.loc]

    @classmethod
    def from_list(cls, data_list):
        city, region, country, loc = data_list
        return cls(city, region, country, loc)