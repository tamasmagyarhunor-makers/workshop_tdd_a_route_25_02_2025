from lib.pokemon import Pokemon

class PokemonRepository():
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def all(self):
        rows = self._db_connection.execute('SELECT * from pokemons')
        pokemons = []
        for row in rows:
            item = Pokemon(row["id"], row["name"], row["type"])
            pokemons.append(item)
        return pokemons