
from flask_testing import TestCase
from models.user import User
from app import app
from config import config_environments

class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object(config_environments['testing'])
        return app

    def setUp(self):
        self.client =self.app.test_client()
        user = User("Allan", "allan2327")
