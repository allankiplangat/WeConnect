
class BusinessList(object):
    """This class adds a business to the data structure"""
    def __init__(self):
        self.businesses_details = []

    def add_business(self, _id, name, mobile_number, description, category, location ):
        businesses_detail= {
            "_id":_id,
            "name":name,
            "mobile_number": mobile_number,
            "description":description,
            "category": category,
            "location": location,
        }

        self.businesses_details.append(businesses_detail)

        test_input = False
        for record in self.businesses_details:
            if record.get("_id") == _id:
                test_input = True
        print(self.businesses_details)
        if test_input:
            return "Business added successfully"