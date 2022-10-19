from telnetlib import STATUS
from fastapi import APIRouter, Response, status
from . import pokemons_utils
from Queries import queries


router = APIRouter()


@router.get("/pokemons/{pokemon_name}/trainers")
def get_trainers_of_pokemon(pokemon_name):
    pokemons_utils.validate_pokemon_name(pokemon_name)
    pokemon_owners = queries.find_owners(pokemon_name)
    return {"trainers": pokemon_owners}


@router.get("/pokemons")
def get_pokemons_by_type(type):
    pokemons_utils.validate_pokemon_type(type)
    pokemons = queries.find_by_type(type)
    return {"pokemons": pokemons}


@router.get("/pokemons/{pokemon_name}")
def get_pokemon_by_name(pokemon_name):
    pokemons_utils.validate_pokemon_name(pokemon_name)
    pokemon_data = pokemons_utils.get_pokemon_data(pokemon_name)
    return pokemon_data


@router.post("/pokemons/{pokemon_name}")
def add_pokemon(pokemon_name, response: Response):
    pokemon_data = pokemons_utils.add_pokemon(pokemon_name)
    response.headers["Location"] = f"/pokemons/{pokemon_name}"
    response.status_code = status.HTTP_201_CREATED
    return pokemon_data
