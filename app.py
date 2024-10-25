# import flask library
from flask import Flask

# set up app variable, to start writing routes
app = Flask(__name__)


@app.route('/')
# Route function
def homepage():
    """Shows a greeting to the user.""" # Docstring
    return 'Are you there, world? It\'s me, Ducky!'

# < and > route variable; available in a variable called users_animal
@app.route('/animal/<users_animal>')
# Route function takes in the variable users_animals
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'









if __name__ == '__main__':
    app.run(debug=True)