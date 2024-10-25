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


@app.route('/madlibs/<adjective>/<noun>')
def two_string(adjective, noun):
    """Display a funny but work-appropriate story using adjective and noun"""
    story = f'Today, I tried to get some {adjective} work done from home, but my 3-year-old had other plans.\n'
    story += f'First, he turned my {noun} into a {adjective} fort and insisted I help guard it from imaginary {noun}.\n'
    story += f'Then, while I was on a video call, he brought me a {adjective} drawing of a {noun} and proudly declared it his “masterpiece.” \n'
    story += f'By noon, my laptop was covered in {adjective} stickers, and my to-do list had turned into a {noun}. But somehow, between the {noun} \n'
    story += f'and the giggles, we both managed to accomplish something: him—an {adjective} nap; me—a sense of {noun}.'

    return story



if __name__ == '__main__':
    app.run(debug=True)