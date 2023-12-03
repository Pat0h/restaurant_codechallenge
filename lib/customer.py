class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f'{self.given_name} {self.family_name}'

    @classmethod
    def all(cls):
        return cls.all_customers


# Tests
customer1 = Customer('Patrick', 'Ngatia')
customer2 = Customer('Purity', 'Ngatia')

# print(customer1.full_name())
# print(customer2.full_name())

all_customers = Customer.all()
for Customer in all_customers:
    print(Customer.full_name())
