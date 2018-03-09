from flask import jsonify, request
from flask_restful import Resource
from models.user import User
from config import Config
from models.security import authenticate, identity, save_data
 
class Register(Resource):
    """
    This class creates end points for registering users.
    """

    def post(self):
        """Endpoint for registering users"""
        data = request.get_json(silent=True)
        if not data:
            return {"error": "Please enter registration data"}, 400
        elif len(data) > 2:
            return {"error": "Invalid format. " +
                    "Only username and Password are allowed"}, 400
        try:
            username = data["username"]
            password = data["password"]
        except Exception:
            return {"error": "username or password is missing"}, 400
            
        user = authenticate(username, password)
        
        if user:
            return {"message": "{} already exists".format(user.username)}, 400
        else:
            save_data(username, password)
            
            return {"message": "Successfully registered {0}".format(username)}
