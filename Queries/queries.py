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
        query = f"""select T.name 
                    from Pokemon P, Trainer T, PokemonTrainer PT
                    where
                        P.id = PT.pokemonId and
                        T.name = PT.trainerName and 
                        P.name = "{pokemon_name}";"""
        cursor.execute(query)
        result = [trainer["name"] for trainer in cursor.fetchall()]
        return result

def find_roster(trainer_name):
    with connection.cursor() as cursor:
        query = f"""select P.name 
                    from Pokemon P, PokemonTrainer PT
                    where
                        P.id = PT.pokemonId and
                        PT.trainerName = "{trainer_name}";"""
        cursor.execute(query)
        result = [pokemon["name"] for pokemon in cursor.fetchall()]
        return result