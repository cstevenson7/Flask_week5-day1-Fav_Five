from flask import Flask
from config import Config

app= Flask(__name__)

app.config.from_object(Config)  # pulling in our config class

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

from fave5_assignment import routes  # don't need lines 8-10 , we have them in routes