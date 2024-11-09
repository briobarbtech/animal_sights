from repositorios.db_repositorio import get_data
from repositorios.ubicacion_repositorio import get_loc
from entidades.data_managment import Animales
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Datos necesarios
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
ipinfo_api_key = os.getenv('ip_info_apikey')


# Traemos la info
animales = Animales(animales=get_data('animals'))
mi_ubicacion = get_loc(ipinfo_api_key)


# Mostramos la info
print(mi_ubicacion.to_list())
print(animales.traer_un_animal(2))

