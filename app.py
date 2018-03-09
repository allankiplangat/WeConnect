from flask import Flask, request
from flask_restful import Resource, Api
from resources.business import BusinessResource
from models.security import authenticate, identity
from resources.auth import Register

app = Flask(__name__)
app.secret_key = 'allan'
api = Api(app) # makes it easy to add resources to the app


api.add_resource(Register, '/api/v1/auth/register')


app.run(port=5000, debug=True)