import string
import pymysql
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


def delete_pokemon_from_trainer(trainer_name, pokemon_id):
    with connection.cursor() as cursor:
        query: string = f"""DELETE FROM pokemontrainer
                            WHERE 
                            trainername = "{trainer_name}" AND pokemonId = "{pokemon_id}";"""
        cursor.execute(query)
        connection.commit()
