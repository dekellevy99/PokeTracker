from fastapi.testclient import TestClient
from unittest.mock import patch as mock_patch
from fastapi import status
from server import app


client = TestClient(app)


@mock_patch('Queries.queries.find_roster')
@mock_patch('routers.trainers.trainers_utils.validate_trainer_name')
def test_get_pokemons_of_trainer(validate_trainer_name, find_roster):
    validate_trainer_name.return_value = None
    find_roster.return_value = ["pikachu, charizard"]

    response = client.get("/trainers/dekel/pokemons")
    response_message = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_message == {"pokemons": ["pikachu, charizard"]}


@mock_patch('routers.trainers.trainers_utils.evolve_pokemon_for_trainer')
@mock_patch('routers.trainers.trainers_utils.validate_pokemon_name')
@mock_patch('routers.trainers.trainers_utils.validate_trainer_name')
def test_evolve_pokemon_for_trainer(validate_trainer_name, validate_pokemon_name, evolve_pokemon_for_trainer):
    validate_trainer_name.return_value = None
    validate_pokemon_name.return_value = None
    evolve_pokemon_for_trainer.return_value = "pikachu"

    response = client.put("/trainers/elik/pokemon/pichu")
    assert response.status_code == status.HTTP_200_OK


@mock_patch('Queries.queries.delete_pokemon_from_trainer')
@mock_patch('Queries.queries.get_pokemon_id_by_name')
@mock_patch('routers.trainers.trainers_utils.validate_pokemon_name')
@mock_patch('routers.trainers.trainers_utils.validate_trainer_name')
def test_delete_pokemon_from_trainer(validate_trainer_name, validate_pokemon_name, get_pokemon_id_by_name, delete_pokemon_from_trainer):
    validate_trainer_name.return_value = None
    validate_pokemon_name.return_value = None
    get_pokemon_id_by_name.return_value = 0
    delete_pokemon_from_trainer.return_value = None

    response = client.delete("/trainers/elik/pokemons/dekel")
    assert response.status_code == status.HTTP_204_NO_CONTENT


@mock_patch('Queries.queries.insert_trainer_record')
def test_add_new_trainer(insert_trainer_record):
    insert_trainer_record.return_value = None

    response = client.post(
        "/trainers", json={"name": "Dekel", "town": "Jerusalem"})
    response_message = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert response.headers["Location"] == "/trainers/Dekel"
    assert response_message == {"name": "Dekel", "town": "Jerusalem"}
