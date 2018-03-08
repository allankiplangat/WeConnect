from .test_base import BaseTestCase
import json

class AuthTestCase(BaseTestCase):

    def test_registration_bad_format(self):
        data = json.dumps({"username": "Allan",
                           "password": 2327,
                           "invalid": "Format not supported"}
                          )

        response = self.client.post('/api/v1/auth/register',
                                    data=data,
                                    content_type='application/json',
                                    headers={}
                                    )
        self.assertEqual(response.json["error"],
                         "Invalid format. " +
                         "Only username and password are allowed")

    def test_registration_with_no_data(self):
        response = self.client.post('/api/v1/auth/register',
                                    data=json.dumps({}),
                                    content_type='application/json',
                                    headers={}
                                    )
        self.assertEqual(response.json["error"],
                         "Please enter registration data")

    def test_registration_with_missing_data(self):
        data = json.dumps({"username": "Tester"})
        response = self.client.post('/api/v1/auth/register',
                                    data=data,
                                    content_type='application/json',
                                    headers={}
                                    )
        self.assertEqual(response.json["error"],
                         "username or password is missing")

    def test_registration_with_existing_username(self):
        data = json.dumps({"username": "Alanos",
                           "password": "password"})
        response = self.client.post('/api/v1/auth/register',
                                    data=data,
                                    content_type='application/json',
                                    headers={}
                                    )
        self.assertEqual(response.json["message"], "Alanos already exists")

    def test_registration_works(self):
        data = json.dumps({"username": "Allan",
                           "password": 2327})
        response = self.client.post('/api/v1/auth/register',
                                    data=data,
                                    content_type='application/json',
                                    headers={}
                                    )
        self.assertEqual(response.json["message"],
                         "Successfully registered Allan")

    def test_login_with_invalid_password(self):
        data = json.dumps({"username": "Allan",
                           "password": "badpass"})
        response = self.client.post('/api/v1/auth/register',
                                    data=data,
                                    content_type='application/json',
                                    headers={}
                                    )
        self.assertEqual(response.json["error"], "Invalid password")

    def test_login_with_missing_data(self):
        data = json.dumps({"username": "Alanos"})
        response = self.client.post('/api/v1/auth/login',
                                    data=data,
                                    content_type='application/json',
                                    headers={}
                                    )
        self.assertEqual(response.json["error"],
                         "username or password is missing")

    def test_login_with_no_data(self):
        response = self.client.post('/api/v1/auth/login',
                                    content_type='application/json',
                                    headers={}
                                    )
        self.assertEqual(response.json["error"],
                         "Login data not found")

    def test_login_works(self):
        data = json.dumps({"username": "Alanos",
                           "password": "password"
                           })
        response = self.client.post('/api/v1/auth/login',
                                    data=data,
                                    content_type='application/json',
                                    headers={}
                                    )
        self.assertEqual(response.json["message"], "Login successful")

