from Queries import queries
from fastapi import HTTPException, status


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