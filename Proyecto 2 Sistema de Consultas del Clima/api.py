import requests
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def consultar_clima(ciudad):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"

    try: 
        respuesta = requests.get(url)
        datos = respuesta.json()

        if respuesta.status_code != 200:
            print(f"Error: {datos.get('message', 'No se pudo obtener el clima')}")
            return None
        
        resultado = {
            "ciudad": datos['name'],
            "temperatura": datos['main']['temp'],
            "descripcion": datos['weather'][0]['description']
        }

        return resultado
    except requests.exceptions.RequestException:
        return None