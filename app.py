from flask import Flask, request
from flask_restful import Resource, Api
from resources.business import BusinessResource
from flask_jwt import JWT ,jwt_required
from models.security import authenticate, identity
from resources.auth import Register

app = Flask(__name__)
app.secret_key = 'allan'
api = Api(app) # makes it easy to add resources to the app

jwt = JWT(app, authenticate, identity ) #auth
# api.add_resource(BusinessResource, '/api/v1/businesses')
api.add_resource(Register, '/api/v1/auth/register')
# api.add_resource(GetBusiness, '/api/v1/businesses/<int:_id>')

app.run(port=5000, debug=True)