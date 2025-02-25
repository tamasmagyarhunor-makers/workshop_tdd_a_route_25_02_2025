def test_get_pokemons(db_connection, web_client):
    db_connection.seed("seeds/pokemon_store.sql")

    response = web_client.get("/pokemons")

    assert response.status_code == 200

    assert response.data.decode("utf-8") == "\n".join([
        "Pokemon(1, Pikachu, electric)",
        "Pokemon(2, Raichu, electric)",
        "Pokemon(3, Charmander, fire)"
    ])