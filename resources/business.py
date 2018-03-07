from flask_restful import Resource, Api
from flask import Flask, request
from models.business import BusinessList


business_list = BusinessList()
class BusinessResource(Resource):
    def get(self):
        return {'business_details': businesses_details}
    
    def post(self):
        data = request.get_json()
       
        businesses_detail = business_list.add_business(data["_id"], data["name"], data["mobile_number"],
                                    data["description"], data["category"], data['location'])   
        return businesses_detail, 201

class GetBusiness(Resource):
    def get(self, _id):
        for business in businesses_details:
            if business['_id'] == _id:
                return business
        return {'business': None}, 404
    def delete(self, _id):
        global businesses_details
        businesses_details = list(filter(lambda x:x['_id'] != _id, businesses_details))
        return {'Message': 'Item deleted'}

    def put(self, _id):
        data = request.get_json()
        business = next(filter(lambda x: x ['_id'] == _id, businesses_details), None)
        if business is None:
            business = {
                "_id":data["_id"],
                "name":data["name"],
                "mobile_number": data["mobile_number"],
                "description": data["description"],
                "category": data["category"],
                "location": data['location'],
            }
            businesses_details.append(business)
        else:
            business.update(data)
        return business
