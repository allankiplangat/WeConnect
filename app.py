from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) # makes it easy to add resources to the app

businesses_details = []


app.run(port=5000, debug=True)