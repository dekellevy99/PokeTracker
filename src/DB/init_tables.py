import json
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poketrackerdb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def insert_pokemon_record(pokemon):
    with connection.cursor() as cursor:
        pokemon_id = pokemon["id"]
        pokemon_name = pokemon["name"]
        pokemon_height = pokemon["height"]
        pokemon_weight = pokemon["weight"]

        query = f"""INSERT INTO Pokemon VALUES({pokemon_id}, "{pokemon_name}", {pokemon_height}, {pokemon_weight})"""
        cursor.execute(query)
        connection.commit()


def insert_type_record(type):
    with connection.cursor() as cursor:
        query = f"""INSERT IGNORE INTO Type VALUES("{type}")"""
        cursor.execute(query)
        connection.commit()


def insert_pokemon_type_record(pokemon_id, pokemon_type):
    with connection.cursor() as cursor:
        query = f"""INSERT INTO PokemonType VALUES({pokemon_id}, "{pokemon_type}")"""
        cursor.execute(query)
        connection.commit()


def insert_trainer_record(trainer):
    with connection.cursor() as cursor:
        trainer_name = trainer["name"]
        trainer_town = trainer["town"]

        query = f"""INSERT IGNORE INTO Trainer VALUES("{trainer_name}", "{trainer_town}")"""
        cursor.execute(query)
        connection.commit()


def insert_pokemon_trainer_record(pokemon_id, trainer_name):
    with connection.cursor() as cursor:
        query = f"""INSERT INTO PokemonTrainer VALUES({pokemon_id}, "{trainer_name}")"""
        cursor.execute(query)
        connection.commit()


def insert_trainers_records(pokemon_id, trainers):
    for trainer in trainers:
        insert_trainer_record(trainer)
        insert_pokemon_trainer_record(pokemon_id, trainer["name"])


def file_parsing():
    poke_file = open("poke_data.json")
    poke_data = json.load(poke_file)

    for pokemon in poke_data:
        pokemon_data = {
            "id": pokemon["id"],
            "name": pokemon["name"],
            "height": pokemon["height"],
            "weight": pokemon["weight"]
        }
        insert_pokemon_record(pokemon_data)
        insert_type_record(pokemon["type"])
        insert_pokemon_type_record(pokemon["id"], pokemon["type"])
        insert_trainers_records(pokemon["id"], pokemon["ownedBy"])
