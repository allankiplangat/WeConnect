from flask_jwt import jwt
from flask_testing import TestCase
from models.user import User
from app import app
from config import Config

class BaseTestCase(TestCase):

    def create_app(self):
        return app

    def setUp(self):
        self.client =self.app.test_client()
        user = User(1, "Allan", "allan2327")
