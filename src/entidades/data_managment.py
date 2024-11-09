class Ubicacion:
    def __init__(self, city, region,country,lat, lng):
        self.city = city 
        self.region = region
        self.country = country
        self.lat = lat
        self.lng = lng
        return None

    def mostrar_info(self):
        print(f"Ciudad: {self.city}")
        print(f"Región: {self.region}")
        print(f"País: {self.country}")
        print(f"Longitud: {self.lat}")
        print(f"Latitud: {self.lng}")

    @classmethod
    def from_json(cls, data_json):
        city = data_json.get('city')
        region = data_json.get('region')
        country = data_json.get('country')
        lat = data_json.get('loc').split(',')[0]
        lng = data_json.get('loc').split(',')[1]
        
        return cls(city, region, country, lat, lng)
    def to_list(self):
        return [self.city, self.region, self.country, self.lat, self.lng]

    @classmethod
    def from_list(cls, data_list):
        city, region, country, lat,lng = data_list
        return cls(city, region, country, lat,lng)


class Animales:
    def __init__(self,animales):
        self.animales =animales


    def mostrar_animales(self):
        for i in range(len(self.animales)):
            print(f'{i}| {self.animales[i][0]}')
    
    def traer_un_animal(self,id):
        return self.animales[id]