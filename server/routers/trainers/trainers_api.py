from fastapi import APIRouter, status
from fastapi import Request, Response
from . import trainers_utils
from pymysql.err import IntegrityError
from Queries import queries


router = APIRouter()


@router.get('/trainers/{trainer_name}/pokemons')
async def get_pokemons_of_trainer(trainer_name):
    trainers_utils.validate_trainer_name(trainer_name)
    trainer_pokemons = queries.find_roster(trainer_name)
    return {"pokemons": trainer_pokemons}


@router.post('/trainers')
async def add_new_trainer(request: Request, response: Response):
    req = await request.json()
    try:
        queries.insert_trainer_record(req["name"], req["town"])
        response.headers["Location"] = f"/trainers/{req['name']}"
        response.status_code = status.HTTP_201_CREATED
        return {
            "name": req["name"],
            "town": req["town"]
        }
    except KeyError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "error": "KeyError",
            "details": "json key should be 'name' and 'town'"
        }
    except IntegrityError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "error": "primery key already exists",
            "details": "json key should be 'name' and 'town'"
        }


@router.delete('/trainers/{trainer_name}/pokemons/{pokemon_name}')
async def delete_pokemon_from_trainer(trainer_name, pokemon_name, response: Response):
    trainers_utils.validate_trainer_name(trainer_name)
    trainers_utils.validate_pokemon_name(pokemon_name)
    pokemon_id = queries.get_pokemon_id_by_name(pokemon_name)
    queries.delete_pokemon_from_trainer(trainer_name, pokemon_id)
    response.status_code = status.HTTP_204_NO_CONTENT


@router.put('/trainers/{trainer_name}/pokemon/{pokemon_name}')
async def evolve_pokemon_for_trainer(trainer_name, pokemon_name):
    trainers_utils.validate_trainer_name(trainer_name)
    trainers_utils.validate_pokemon_name(pokemon_name)
    trainers_utils.evolve_pokemon_for_trainer(trainer_name, pokemon_name)
