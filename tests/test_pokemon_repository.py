from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon

def test_get_all_records(db_connection):
    db_connection.seed("seeds/pokemon_store.sql")
    repository = PokemonRepository(db_connection)

    pokemons = repository.all()

    assert pokemons == [
        Pokemon(1, 'Pikachu', 'electric'),
        Pokemon(2, 'Raichu', 'electric'),
        Pokemon(3, 'Charmander', 'fire')
    ]

def test_create_new_pokemon(db_connection):
    db_connection.seed("seeds/pokemon_store.sql")
    repository = PokemonRepository(db_connection)

    repository.create(Pokemon(None, "Bulbasaur", "grass/poison"))

    pokemons = repository.all()

    assert pokemons == [
        Pokemon(1, 'Pikachu', 'electric'),
        Pokemon(2, 'Raichu', 'electric'),
        Pokemon(3, 'Charmander', 'fire'),
        Pokemon(4, "Bulbasaur", "grass/poison")
    ]