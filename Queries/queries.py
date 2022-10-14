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
    try:
        with connection.cursor() as cusor:
            query = """select name
                       from pokemon
                       where weight = (select max(weight) from pokemon)"""
            cusor.execute(query)
            result = cusor.fetchone()["name"]
            return result
    except:
        print("error")


def find_by_type(pokemon_type):
    try:
        with connection.cursor() as cusor:
            query = f"""select pokemon.name
                    from pokemon join pokemontype
                    on pokemon.id = pokemontype.pokemonId
                    where pokemontype.pokeType = "{pokemonType}";"""
            cusor.execute(query)
            result = [pokemon["name"] for pokemon in cusor.fetchall()]
            return result
    except:
        print("error")


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
