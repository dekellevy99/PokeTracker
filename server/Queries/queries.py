import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poketrackerdb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def get_heaviest_pokimon():
    with connection.cursor() as cursor:
        query = """ SELECT name
                    FROM Pokemon
                    WHERE weight = (select max(weight) from pokemon)"""
        cursor.execute(query)
        result = cursor.fetchone()["name"]
        return result


def find_by_type(pokemon_type):
    with connection.cursor() as cusor:
        query = f"""SELECT P.name
                    FROM Pokemon P join PokemonType PT on P.id = PT.pokemonId
                    WHERE PT.pokeType = "{pokemon_type}";"""
        cusor.execute(query)
        result = [pokemon["name"] for pokemon in cusor.fetchall()]
        return result


def find_owners(pokemon_name):
    with connection.cursor() as cursor:
        query = f"""SELECT T.name 
                    FROM Pokemon P, Trainer T, PokemonTrainer PT
                    WHERE
                        P.id = PT.pokemonId AND
                        T.name = PT.trainerName AND 
                        P.name = "{pokemon_name}";"""
        cursor.execute(query)
        result = [trainer["name"] for trainer in cursor.fetchall()]
        return result


def find_roster(trainer_name):
    with connection.cursor() as cursor:
        query = f"""SELECT P.name 
                    FROM Pokemon P JOIN PokemonTrainer PT
                    ON P.id = PT.pokemonId
                    WHERE PT.trainerName = "{trainer_name}";"""
        cursor.execute(query)
        result = [pokemon["name"] for pokemon in cursor.fetchall()]
        return result


def find_most_owned_pokemon():
    with connection.cursor() as cursor:
        query = """ SELECT P.name, count(*)
                    FROM Pokemon P join PokemonTrainer PT on P.id = PT.pokemonId
                    GROUP BY P.name
                    HAVING count(*) >= ALL (SELECT COUNT(*)
                                            FROM PokemonTrainer
                                            GROUP BY pokemonId);"""
        cursor.execute(query)
        result = [pokemon["name"] for pokemon in cursor.fetchall()]
        return result


def get_all_pokemon_names():
    with connection.cursor() as cursor:
        query = """ SELECT name FROM Pokemon;"""
        cursor.execute(query)
        result = [pokemon["name"] for pokemon in cursor.fetchall()]
        return result


def get_all_pokemon_types():
    with connection.cursor() as cursor:
        query = """ SELECT pokeType FROM Type;"""
        cursor.execute(query)
        result = [type["pokeType"] for type in cursor.fetchall()]
        return result


def get_all_trainers_names():
    with connection.cursor() as cursor:
        query = """ SELECT name FROM Trainer;"""
        cursor.execute(query)
        result = [trainer["name"] for trainer in cursor.fetchall()]
        return result


def get_pokemon_by_name(pokemon_name):
    with connection.cursor() as cursor:
        query = f"""SELECT *
                    FROM Pokemon
                    WHERE Pokemon.name = "{pokemon_name}";"""
        cursor.execute(query)
        result = cursor.fetchone()
        return result


def insert_type_record(type):
    with connection.cursor() as cursor:
        query = f"""INSERT IGNORE INTO Type VALUES("{type}")"""
        cursor.execute(query)
        connection.commit()


def insert_pokemon_type_record(pokemon_id, pokemon_type):
    with connection.cursor() as cursor:
        query = f"""INSERT IGNORE INTO PokemonType VALUES({pokemon_id}, "{pokemon_type}")"""
        cursor.execute(query)
        connection.commit()
