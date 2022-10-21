GET_HEAVIEST_POKEMON = """  SELECT name
                            FROM Pokemon
                            WHERE weight = (select max(weight) from pokemon)"""

GET_POKEMONS_BY_TYPE = """  SELECT P.name
                            FROM Pokemon P join PokemonType PT on P.id = PT.pokemonId
                            WHERE PT.pokeType = %s"""

GET_OWNERS_OF_POKEMON = """ SELECT T.name 
                            FROM Pokemon P, Trainer T, PokemonTrainer PT
                            WHERE
                                P.id = PT.pokemonId AND
                                T.name = PT.trainerName AND 
                                P.name = %s"""

GET_MOST_OWNED_POKEMON = """SELECT P.name, count(*)
                            FROM Pokemon P join PokemonTrainer PT on P.id = PT.pokemonId
                            GROUP BY P.name
                            HAVING count(*) >= ALL (SELECT COUNT(*)
                                            FROM PokemonTrainer
                                            GROUP BY pokemonId);"""

GET_ALL_POKEMONS_NAMES = """ SELECT name FROM Pokemon """

GET_ALL_POKEMONS_TYPES= """ SELECT pokeType FROM Type """

GET_POKEMON_BY_NAME = """SELECT *
                         FROM Pokemon
                         WHERE Pokemon.name = %s """
                         
GET_POKEMON_ID_BY_NAME = """SELECT id
                            FROM Pokemon
                            WHERE name = %s;"""


GET_POKEMONS_OF_TRAINER = """SELECT P.name 
                             FROM Pokemon P JOIN PokemonTrainer PT
                             ON P.id = PT.pokemonId
                             WHERE PT.trainerName = %s;"""

GET_ALL_TRAINERS_NAMES = """ SELECT name FROM Trainer """


INSERT_TYPE_RECORD = """INSERT IGNORE INTO Type VALUES(%s)"""

INSERT_POKEMON_TYPE_RECORD = """INSERT IGNORE INTO PokemonType VALUES(%s, %s)"""

INSERT_POKEMON_RECORD = """INSERT INTO Pokemon VALUES(null, %s, %s, %s)"""

INSERT_TRAINER_RECORD = """ INSERT INTO trainer (Name, Town)
                            VALUES (%s, %s);"""


EVOLVE_POKEMON_OF_TRAINER = """ UPDATE PokemonTrainer
                                SET pokemonId = %s
                                WHERE trainername = %s AND pokemonId = %s"""


DELETE_POKEMON_FROM_TRAINER = """DELETE FROM PokemonTrainer
                                 WHERE trainerName = %s AND pokemonId = %s"""
    