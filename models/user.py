from werkzeug.security import generate_password_hash, check_password_hash
from models.data import DataStore
class User:
    

    def __init__(self, _id,  username, password):
        self.id = _id
        self.username = username
        self.set_password(password=bytes(str(password), 'utf-8'))
        self.password = self.pwd_hash
        self.users = []

    def set_password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def add_user(self, data):
        data['password']=self.set_password(data['password'])
        
        DataStore().append_user(data)


    def authenticate(self, username, password):
        username_mapping = {u.username: u for u in self.users}
        user = username_mapping.get(username, None)
        if user and user.password == password:
            return user

    def identity(self, payload):
        userid_mapping = {u.id: u for u in self.users}
        user_id = payload[identity]
        return userid_mapping.get(user_id, None)

