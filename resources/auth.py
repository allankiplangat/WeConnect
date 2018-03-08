from datetime import datetime, timedelta

from flask import jsonify, request
from flask_restful import abort, Resource
import jwt
from models.user import User
from config import Config
from models.data import DataStore
from models.security import authenticate, identity
 
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
            _id = data["id"]
            username = data["username"]
            password = data["password"]
        except Exception:
            return {"error": "username or password is missing"}, 400
            
        user = authenticate(username, password)
        
        if user:
            return {"message": "{} already exists".format(user.username)}, 400
        else:
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            return {"message": "Successfully registered {0}".format(username)}


# class Login(Resource):
#     """Class that creates endpoints for login"""

#     def post(self):
#         """End point for login"""
#         data = request.get_json(silent=True)
#         if not data:
#             return {"error": "Login data not found"}, 400
#         try:
#             username = data["username"]
#             password = data["password"]
#         except Exception:
#             return {"error": "username or password is missing"}, 400
#         user = User.query.filter_by(username=username).first()
#         if not user:
#             return {"error": "{0} is not registered".format(username)}, 400
#         elif user and not user.check_password(password=bytes(str(password), 'utf-8')):
#             return {"error": "Invalid password"}, 403
#         else:
#             payload = {"sub": user.id,
#                        "exp": datetime.utcnow() + timedelta(minutes=30)
#                        }
#             token = jwt.encode(
#                 payload, Config.SECRET_KEY, algorithm='HS256')
#             return jsonify({"message": "Login successful",
#                             "token": token.decode('utf-8'),
#                             })
