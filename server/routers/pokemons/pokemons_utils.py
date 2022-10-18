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


def update_pokemon_type(pokemon_id, pokemon_name):
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()
    pokemon_types = [pokemon_type["type"]["name"] for pokemon_type in data["types"]]
    for type in pokemon_types:
        queries.insert_type_record(type)
        queries.insert_pokemon_type_record(pokemon_id, type)
    return pokemon_types


def get_pokemon_data(pokemon_name):
    pokemon_data = queries.get_pokemon_by_name(pokemon_name)
    pokemon_types = update_pokemon_type(pokemon_data["id"], pokemon_name)
    pokemon_data["types"] = pokemon_types
    return pokemon_data


def add_pokemon(pokemon_name):
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()
    pokemon = {"name": pokemon_name, "height": data["height"], "weight": data["weight"]}
    queries.insert_pokemon_record(pokemon)
    pokemon["id"] = queries.get_pokemon_id_by_name(pokemon_name)
    pokemon_types = update_pokemon_type(pokemon["id"], pokemon_name)
    pokemon["types"] = pokemon_types
    return pokemon