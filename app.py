import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/', methods=['GET'])
def index():
    return "Welcome to our little web app"

@app.route('/', methods=['POST'])
def index_post():
    name = request.form['name']
    return f"This is the POST index for {name}"

@app.route('/pokemons', methods=['GET'])
def get_pokemons():
    connection = get_flask_database_connection(app)
    repository = PokemonRepository(connection)

    pokemons = repository.all()

    return "\n".join([
        str(pokemon) for pokemon in pokemons
    ])

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

