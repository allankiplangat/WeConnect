import unittest
from models.business import BusinessList

class BusinessListTestCase(unittest.TestCase):
    def setUp(self):
        self.business_list = BusinessList()

    def test_create_new_business(self):
        response = self.business_list.add_business(1, "invalskies", 3535646, "we sell stuff",
                                                    "category", "kisumu")
        self.assertEqual(response, "Business added successfully")

if __name__ == '__main__':
    unittest.main()