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

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a messgae with the users favorite dessert"""
    return f'How did you know I liked {users_dessert}?'







if __name__ == '__main__':
    app.run(debug=True)