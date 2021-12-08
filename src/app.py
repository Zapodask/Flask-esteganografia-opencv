from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from .routes import Encrypt, Decrypt


app = Flask(__name__)
CORS(app)
api = Api(app)

# Resources
api.add_resource(Encrypt, "/encrypt")
api.add_resource(Decrypt, "/decrypt")
