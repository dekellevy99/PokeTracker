from unicodedata import name
from fastapi import APIRouter
from fastapi import Request, Response
from . import trainers_utils
from pymysql.err import IntegrityError
router = APIRouter()


@router.get('/trainer/{trainerName}/pokemons', status_code=200)
def get_teainers_pokimon(trainerName):
    Response.headers["Content-Type"] = "application/json"
    return {"pokemons": trainers_utils.query_teainers_pokimon(trainerName)}


@router.post('/trainers', status_code=201)
async def add_new_trainer(request: Request, response: Response):
    req = await request.json()
    Response.headers["Content-Type"] = "application/json"
    try:
        trainers_utils.inser_new_trainer(req["name"], req["town"])
    except KeyError:
        response.status_code = 400
        return {
            "error": "KeyError",
            "details": "json key should be 'name' and 'town'"
        }
    except IntegrityError:
        response.status_code = 400
        return {
            "error": "primery key already exists",
            "details": "json key should be 'name' and 'town'"
        }
