from fave5_assignment import app
from flask import render_template


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

#Home page route
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/favorite_five')
def favorite_five():
    climber_dict= {"Sarah Hueniken" : "First North American woman to climb an M14 rated mixed climb", "Lynn Hill": " First PERSON to climb the The Nose on El Capitan", "Margo Hayes": "First woman to climb a 5.15a - La Rambla", "Tommy Caldwell": "Part of the first ascent team to climb The Dawn Wall - took 19 days", "Kevin Jorgeson": "Part of the first ascent team to climb The Dawn Wall - took 19 days"}
    return render_template("favorite_five.html", climber_dict = climber_dict)
