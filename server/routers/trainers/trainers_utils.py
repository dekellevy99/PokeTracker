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


def query_teainers_pokimon(trainerName: string):
    with connection.cursor() as cursor:
        query: string = f""" SELECT Pokemon.id, Pokemon.name, Pokemon.height, Pokemon.weight
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

