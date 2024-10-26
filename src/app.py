from repositorios.db_repositorio import get_data
from repositorios.open_cage_repositorio import obtener_ubicacion
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
open_cage_api_key = os.getenv('OPEN_CAGE_API_KEY')

animales_mendoza = [
    "Guanaco",
    "Cóndor Andino",
    "Puma",
    "Mara Patagónica",
    "Ñandú",
    "Lagartija de las Dunas",
    "Gato Montés",
    "Zorro Colorado",
    "Hurón Menor",
    "Vizcacha de la Sierra",
    "Liebre Mara",
    "Carpintero Andino",
    "Sapo Andino",
    "Iguana Colorada",
    "Ratón Andino",
    "Martineta",
    "Flamenco Andino",
    "Lagartija Cuelligruesa",
    "Serpiente Yarará",
    "Aguilucho Común"
]

#save_data(animales_mendoza)
animales = get_data('animals')
mi_ubicacion = obtener_ubicacion(open_cage_api_key)
animal_avistado = animales[12]
#data = [mi_ubicacion.city,mi_ubicacion.country,mi_ubicacion.region,mi_ubicacion.loc, animal_avistado[0]]
print(mi_ubicacion.toList())
