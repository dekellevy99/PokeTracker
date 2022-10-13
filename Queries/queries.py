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
