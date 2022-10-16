from unicodedata import name
from fastapi import APIRouter, status
from fastapi import Request, Response
from . import trainers_utils
from pymysql.err import IntegrityError
from Queries import queries

router = APIRouter()


@router.get('/trainer/{trainer_name}/pokemons', status_code=200)
async def get_pokemons_of_trainer(trainer_name):
    Response.headers["Content-Type"] = "application/json"
    return {"pokemons": queries.find_roster(trainer_name)}


@router.post('/trainers', status_code=201)
async def add_new_trainer(request: Request, response: Response):
    req = await request.json()
    Response.headers["Content-Type"] = "application/json"
    try:
        trainers_utils.inser_new_trainer(req["name"], req["town"])
        Response.headers["Location"] = f"/trainers/{req['name']}"
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


@router.delete('/trainer/{trainer_name}/pokemon/{pokemon_name}', status_code=204)
async def delete_pokemon_from_trainer(trainer_name, pokemon_name):
    pokemon_id = trainers_utils.get_pokemon_id_by_name(pokemon_name)
    trainers_utils.delete_pokemon_from_trainer(trainer_name, pokemon_id)


@router.put('/trainer/{trainer_name}/pokemon/{pokemon_name}', status_code=200)
async def evolve_pokemon_for_trainer(trainer_name, pokemon_name):
    trainers_utils.evolve_pokemon_for_trainer(trainer_name, pokemon_name)
