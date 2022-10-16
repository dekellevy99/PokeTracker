from Queries import queries
from fastapi import HTTPException, status
import requests


def validate_pokemon_name(pokemon_name):
    valid_pokemon_names = queries.get_all_pokemon_names()
    if pokemon_name not in valid_pokemon_names:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "invalid pokemon name."
            }
        )


def validate_pokemon_type(pokemon_type):
    valid_pokemon_types = queries.get_all_pokemon_types()
    if pokemon_type not in valid_pokemon_types:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "invalid pokemon type."
            }
        )


def get_pokemon_data(pokemon_name):
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()
    pokemon_types = [pokemon_type["type"]["name"] for pokemon_type in data["types"]]
    pokemon_data = queries.get_pokemon_by_name(pokemon_name)
    pokemon_data["types"] = pokemon_types
    for type in pokemon_types:
        queries.insert_type_record(type)
        queries.insert_pokemon_type_record(pokemon_data["id"], type)   
    return pokemon_data