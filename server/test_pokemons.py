from fastapi.testclient import TestClient
from server import app
from unittest.mock import patch
from fastapi import status

client = TestClient(app)


@patch('routers.pokemons.pokemons_utils.validate_pokemon_name')
@patch('Queries.queries.find_owners')
def test_get_trainers_of_pokemon(find_owners, validate_pokemon_name):
    validate_pokemon_name.return_value = None
    find_owners.return_value = ["Giovanni", "Jasmine", "Whitney"]
    response = client.get("/pokemons/charmander/trainers")
    response_message = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_message == {"trainers": ["Giovanni", "Jasmine", "Whitney"]}


@patch('routers.pokemons.pokemons_utils.validate_pokemon_name')
@patch('Queries.queries.find_by_type')
def test_get_pokemons_by_type(find_by_type, validate_pokemon_name):
    validate_pokemon_name.return_value = None
    find_by_type.return_value = ['caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna',
                                'beedrill', 'paras', 'parasect', 'venonat', 'venomoth', 'scyther', 'pinsir']
    
    response = client.get("/pokemons?type=bug")
    response_message = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_message == {"pokemons": ['caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna',
                                'beedrill', 'paras', 'parasect', 'venonat', 'venomoth', 'scyther', 'pinsir']}


@patch('routers.pokemons.pokemons_utils.validate_pokemon_name')
@patch('routers.pokemons.pokemons_utils.get_pokemon_data')
def get_pokemon_by_name(get_pokemon_data, validate_pokemon_name):
    validate_pokemon_name.return_value = None
    get_pokemon_data.return_value = {
                                        "id": 3,
                                        "name": "venusaur",
                                        "height": 20,
                                        "weight": 1000,
                                        "types": ["grass", "poison"]
                                    }
    
    response = client.get("/pokemons/venusaur")
    response_message = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_message == {
                                    "id": 3,
                                    "name": "venusaur",
                                    "height": 20,
                                    "weight": 1000,
                                    "types": ["grass", "poison"]
                                }


@patch('routers.pokemons.pokemons_utils.add_pokemon')
def test_add_pokemon(add_pokemon):
    add_pokemon.return_value = {
                                    "name": "yanma",
                                    "height": 12,
                                    "weight": 380,
                                    "id": 152,
                                    "types": ["bug", "flying"]
                                }

    response = client.post("/pokemons/yanma")
    response_message = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert response_message ==  {
                                    "name": "yanma",
                                    "height": 12,
                                    "weight": 380,
                                    "id": 152,
                                    "types": ["bug", "flying"]
                                }