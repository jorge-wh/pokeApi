from __future__         import absolute_import, unicode_literals
from django.shortcuts   import render
from PokeApi.web import get_pokemons, get_pokemon, get_photo
import requests

# Visualizar los datos de los pokemon
def all_pokemons(request):
    
    pokemons = get_pokemons('http://pokeapi.co/api/v2/pokemon/',0)
    dictionary = { }
    data = { }
    index = 0
    
    if pokemons:
        
        for pokemon in pokemons:
            
            index   = index + 1
            
            name    = pokemon['name']
            url     = pokemon['url']

            # Obtenemos el ID
            get_id  = get_pokemon(url)
            id      = get_id.get('id')

            # Obtenemos la foto
            photo   = get_photo(url)
            
            dictionary  = {  'nombre': name, 'foto': photo, 'url': url, 'id' : id }
            data[index] = dictionary

    return render(request, 'pokemones.html', {'pokemons': data} )

# Visualizar los datos de un pokemon
def one_pokemon(request, id):

    url = 'http://pokeapi.co/api/v2/pokemon/' + id
    pokemons    = get_pokemon(url)
    
    # Obtenemos la foto
    result_photo    = pokemons.get('sprites', [])
    photo           = result_photo['back_shiny']
    
    name        = pokemons.get('name')
    height      = pokemons.get('height')
    weight      = pokemons.get('weight')

    # Obtenemos el tipo
    result_type = pokemons.get('types', [])
    tipo        = result_type[0]["type"]["name"]

    dictionary = { }
    data_ability = { }
    data_move = { }
    index = 0

    if pokemons:

        # Obtenemos las habilidades
        get_abilities = pokemons.get('abilities', [])
        
        for ability in get_abilities:

            index               = index + 1
            name_ability        =  ability.get('ability', [])['name']
            dictionary          = { 'ability' : name_ability }
            data_ability[index] = dictionary

        # Obtenemos los movimientos
        get_moves = pokemons.get('moves', [])

        for move in get_moves:
            
            index               = index + 1
            name_move           = move.get('move', [])['name']
            dictionary          = { 'move': name_move }
            data_move[index]    = dictionary

    return render(request, 'pokemon.html', {
        'photo':            photo,
        'name':             name,
        'height':           height,
        'weight':           weight,
        'tipo':             tipo,
        'get_abilities':    data_ability,
        'get_moves':        data_move,
    } )

# Visualizar pokemones de un mismo tipo
def list_pokemon_type(request, tipo):

    url = 'http://pokeapi.co/api/v2/type/' +  tipo
    types = get_pokemon(url)
    pokemons = { }
    data = { }
    index = 0

    if types:
        # Entramos al diccionario de pokemones
        name_types = types.get('pokemon', [])
       
        for names in name_types:
            
            index        = index + 1

            # Obtenemos el nombre y el url
            name_pokemon = names.get('pokemon', [])['name']
            url_pokemon = names.get('pokemon', [])['url']

            # Obtenemos el id
            get_id  = get_pokemon(url_pokemon)
            id      = get_id.get('id')

            # Obetenemos la foto
            photo   = get_photo(url_pokemon) 

            pokemons  = { 'nombre' : name_pokemon,  'url': url_pokemon, 'id': id, 'foto': photo}
            data[index] = pokemons

            if index==10:
				break
        
        return render(request, 'pokemones.html', {'pokemons': data} )  