from flask_restful import Api
from flask_script import Manager
from app import app

manager = Manager(app)
api = Api(app)

if __name__=='__main__':
    manager.run()
