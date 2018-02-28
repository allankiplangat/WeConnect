from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) # makes it easy to add resources to the app

businesses_details = []
class BusinessList(Resource):
    def get(self):
        return {'business_details': businesses_details}
    
    def post(self,):
        data = request.get_json()
        businesses_detail= {
            "name":data["name"],
            "mobile_number": data["mobile_number"],
            "description": data["description"],
            "category": data["category"],
            "location": data['location'],
        }

        businesses_details.append(businesses_detail)
        return businesses_detail, 201
        
api.add_resource(BusinessList, '/api/v1/businesses')

app.run(port=5000, debug=True)