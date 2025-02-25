def test_get_pokemons(db_connection, web_client):
    db_connection.seed("seeds/pokemon_store.sql")

    response = web_client.get("/pokemons")

    assert response.status_code == 200

    assert response.data.decode("utf-8") == "\n".join([
        "Pokemon(1, Pikachu, electric)",
        "Pokemon(2, Raichu, electric)",
        "Pokemon(3, Charmander, fire)"
    ])

def test_create_pokemon(db_connection, web_client):
    db_connection.seed("seeds/pokemon_store.sql")

    response = web_client.post("pokemons", data={
        "name": "Charizard",
        "type": "fire"
    })

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Pokemon added successfully"

    response2 = web_client.get("pokemons")

    assert response2.data.decode("utf-8") == "\n".join([
        "Pokemon(1, Pikachu, electric)",
        "Pokemon(2, Raichu, electric)",
        "Pokemon(3, Charmander, fire)",
        "Pokemon(4, Charizard, fire)"
    ])
