import pymysql
from . import sql_queries_constants

DEFAULT_HOST = "localhost"
DEFAULT_USER = "root"
DEFAULT_DB = "poketrackerdb"
DEFAULT_PWD = ""

class DB_Manager:
    def __init__(self, host = DEFAULT_HOST, user = DEFAULT_USER, pwd = DEFAULT_PWD, db = DEFAULT_DB):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=pwd,
            db=db,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
    
    def get_heaviest_pokimon(self):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_HEAVIEST_POKEMON)
            result = cursor.fetchone()["name"]
            return result


    def find_by_type(self, pokemon_type):
        with self.connection.cursor() as cusor:
            cusor.execute(sql_queries_constants.GET_POKEMONS_BY_TYPE, pokemon_type)
            result = [pokemon["name"] for pokemon in cusor.fetchall()]
            return result


    def find_owners(self, pokemon_name):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_OWNERS_OF_POKEMON, pokemon_name)
            result = [trainer["name"] for trainer in cursor.fetchall()]
            return result


    def find_roster(self, trainer_name):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_POKEMONS_OF_TRAINER, trainer_name)
            result = [pokemon["name"] for pokemon in cursor.fetchall()]
            return result


    def find_most_owned_pokemon(self):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_MOST_OWNED_POKEMON) 
            result = [pokemon["name"] for pokemon in cursor.fetchall()]
            return result


    def get_all_pokemon_names(self):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_ALL_POKEMONS_NAMES)
            result = [pokemon["name"] for pokemon in cursor.fetchall()]
            return result


    def get_all_pokemon_types(self):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_ALL_POKEMONS_TYPES)
            result = [type["pokeType"] for type in cursor.fetchall()]
            return result


    def get_all_trainers_names(self):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_ALL_TRAINERS_NAMES)
            result = [trainer["name"] for trainer in cursor.fetchall()]
            return result


    def get_pokemon_by_name(self, pokemon_name):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_POKEMON_BY_NAME, pokemon_name) 
            result = cursor.fetchone()
            return result


    def insert_type_record(self, type):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.INSERT_TYPE_RECORD, type) 
            self.connection.commit()


    def insert_pokemon_type_record(self, pokemon_id, pokemon_type):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.INSERT_POKEMON_TYPE_RECORD, [pokemon_id, pokemon_type]) 
            self.connection.commit()


    def get_pokemon_id_by_name(self, pokemon_name):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_POKEMON_ID_BY_NAME, pokemon_name)
            result = cursor.fetchone()['id']
            return result


    def insert_pokemon_record(self, pokemon):
        with self.connection.cursor() as cursor:
            pokemon_name = pokemon["name"]
            pokemon_height = pokemon["height"]
            pokemon_weight = pokemon["weight"]
            cursor.execute(sql_queries_constants.INSERT_POKEMON_RECORD, [pokemon_name, pokemon_height, pokemon_weight]) 
            self.connection.commit()


    def insert_trainer_record(self, name, town):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.INSERT_TRAINER_RECORD, [name, town]) 
            self.connection.commit()


    def evolve_pokemon_of_trainer(self, trainer_name, pokemon_id, evolve_pokemon_id):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.EVOLVE_POKEMON_OF_TRAINER, [trainer_name, pokemon_id, evolve_pokemon_id])
            self.connection.commit()


    def delete_pokemon_from_trainer(self, trainer_name, pokemon_id):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.DELETE_POKEMON_FROM_TRAINER, [trainer_name, pokemon_id])
            self.connection.commit()

db_manager = DB_Manager()