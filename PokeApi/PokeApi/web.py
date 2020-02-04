import requests

#Obtenemos los datos generales, name y url
def get_pokemons(url, offset):

	args = {'offset':offset} if offset else {}

	response = requests.get(url, params=args)

	if response.status_code == 200:

		payload = response.json()
		results = payload.get('results', [])

		return results

#Obtenemos la foto
def get_photo(url):

    response = requests.get(url)

    if response.ok:

        data    = response.json()
        results = data.get('sprites', [])
        photo   = results['back_default']

        return photo

#Obtenemos todos los datos del pokemon
def get_pokemon(url):

    response = requests.get(url)
    results  = '' 
    if response.ok:

        data  = response.json()
        results = data
    return  results