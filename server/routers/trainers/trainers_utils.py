import string
import requests
from Queries import queries
from fastapi import HTTPException, status


def validate_trainer_name(trainer_name):
    valid_trainers_names = queries.get_all_trainers_names()
    if trainer_name not in valid_trainers_names:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "invalid trainer name."
            }
        )


def validate_pokemon_name(pokemon_name):
    valid_pokemon_names = queries.get_all_pokemon_names()
    if pokemon_name not in valid_pokemon_names:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "invalid pokemon name."
            }
        )


def evolve_pokemon_for_trainer(trainer_name: string, pokemon_name: string):
    pokemon_id = queries.get_pokemon_id_by_name(pokemon_name)
    evolve_pokemon_name = get_evolve_pokemon(pokemon_name)
    evolve_pokemon_id = queries.get_pokemon_id_by_name(evolve_pokemon_name)
    queries.evolve_pokemon_of_trainer(trainer_name, pokemon_id, evolve_pokemon_id)


def get_evolve_pokemon(pokemon_name: string):
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()
    species_url: string = data['species']['url']
    data = requests.get(species_url).json()
    evolution_chain_url: string = data['evolution_chain']['url']

    data = requests.get(evolution_chain_url).json()
    chain = data['chain']
    while (chain['species']['name'] != pokemon_name):
        chain = chain['evolves_to'][0]

    try:
        evolve_pokemon = chain['evolves_to'][0]["species"]["name"]
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "can't evolve pokemon."
            })
    return evolve_pokemon
