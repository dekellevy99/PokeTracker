from email.policy import HTTP
import string
from telnetlib import STATUS
from urllib import request
import pymysql
import requests
from Queries import queries
from fastapi import HTTPException, status

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poketrackerdb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

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


def insert_new_trainer(name: string, town: string):
    with connection.cursor() as cursor:
        query: string = f"""INSERT INTO trainer (Name, Town)
                            VALUES ('{name}', '{town}');"""
        cursor.execute(query)
        connection.commit()


def get_pokemon_id_by_name(pokemon_name: string):
    with connection.cursor() as cursor:
        query: string = f"""SELECT id
                            FROM Pokemon
                            WHERE name = "{pokemon_name}";"""
        cursor.execute(query)
        result = cursor.fetchone()['id']
        return result


def delete_pokemon_from_trainer(trainer_name: string, pokemon_id: string):
    with connection.cursor() as cursor:
        query: string = f"""DELETE FROM pokemontrainer
                            WHERE 
                            trainername = "{trainer_name}" AND pokemonId = {pokemon_id};"""
        cursor.execute(query)
        connection.commit()


def evolve_pokemon_for_trainer(trainer_name: string, pokemon_name: string):
    pokemon_id = get_pokemon_id_by_name(pokemon_name)
    evolve_pokemon_name = get_evolve_pokemon(pokemon_name)
    evolve_pokemon_id = get_pokemon_id_by_name(evolve_pokemon_name)
    update_pokemon_for_evolved(trainer_name, pokemon_id, evolve_pokemon_id)


def update_pokemon_for_evolved(trainer_name: string, pokemon_id: string, evolve_pokemon_id: string):
    with connection.cursor() as cursor:
        query: string = f"""UPDATE Pokemontrainer
                            SET pokemonId = {evolve_pokemon_id}
                            WHERE 
                            trainername = "{trainer_name}" AND pokemonId = {pokemon_id};"""
        cursor.execute(query)
        connection.commit()


def get_evolve_pokemon(pokemon_name: string):
    data = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()
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


print(evolve_pokemon_for_trainer("dekel", "pidgeot"))
