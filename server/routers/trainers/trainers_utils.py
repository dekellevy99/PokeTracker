import string
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poketrackerdb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def query_trainers_pokemon(trainerName: string):
    with connection.cursor() as cursor:
        query: string = f"""SELECT Pokemon.id, Pokemon.name, Pokemon.height, Pokemon.weight
                            FROM PokemonTrainer join Pokemon
                            ON PokemonTrainer.pokemonId = Pokemon.id
                            WHERE PokemonTrainer.trainerName = "{trainerName}";"""
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def inser_new_trainer(name: string, town: string):
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
