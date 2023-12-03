class Customer:
    all_customers = []
    def __init__(self,given_name,family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.all_customers.append(self)

    def given_name(self):
        return self.given_name

