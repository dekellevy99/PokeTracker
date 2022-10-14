from fastapi import APIRouter, HTTPException, status
from Queries import queries
import requests

router = APIRouter()

@router.get("/pokemons/{pokemon_name}/trainers")
def get_trainers_of_pokemon(pokemon_name):
    valid_pokemon_names = queries.get_all_pokemon_names()
    if pokemon_name not in valid_pokemon_names:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "invalid pokemon name."
            }
        )
    
    pokemon_owners = queries.find_owners(pokemon_name)
    return pokemon_owners




