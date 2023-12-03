class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.all_customers.append(self)
        self.reviews = []

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f'{self._given_name} {self._family_name}'

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return list(set(review.restaurant for review in self.reviews))

    def add_review(self, review):
        self.reviews.append(review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
            return None

    @classmethod
    def find_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name == name]
