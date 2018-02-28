from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) # makes it easy to add resources to the app

businesses_details = []

class Business(Resource):
    def get(self, business_id):
        # for business_detail in businesses_details:
        #     if business_detail['business_id'] == business_id:
        #         return business_detail
        # Use a lambda function instead of a for loop.
        business_detail = next(filter(lambda x: x['business_id']== business_id, businesses_details), None)
        return {'business_detail': business_detail}, 200 if business_detail else 404

    def post(self, business_id):
        if next(filter(lambda x: x['business_id']== business_id, businesses_details), None):
            return {"message": "A business with id'{}' already exists.".format(business_id)}, 400

        data = request.get_json()
        businesses_detail= {
            'id':data['business_id'],
            'name':data['name'],
            'mobile_number': data['mobile_number'],
            'description': data['this is my shop'],
            'category': data['technology'],
            'location': data['nairobi'],
        }
        businesses_details.append(businesses_detail)
        return businesses_detail, 201

class BusinessList(Resource):
    def get(self):
        return {'business_details': businesses_details}

api.add_resource(Business, '/api/v1/businesses/<string:business_id>')
api.add_resource(BusinessList, '/api/v1/businesses')

app.run(port=5000, debug=True)