import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poketrackerdb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")


def get_heaviest_pokimon():
    try:
        with connection.cursor() as cusor:
            query = "select max(weight) from pokemon;"
            cusor.execute(query)
            return cusor.fetchall()
    except:
        print("error")


def findByType(pokemonType):
    print(
        f'select pokemon.name from pokemon join pokemontype on pokemon.id = pokemontype.pokemonId where pokemontype.pokeType = "{pokemonType}";')

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


print(findByType("grass"))

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