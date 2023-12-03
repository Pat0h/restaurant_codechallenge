from customer import Customer
from restaurant import Restaurant
from review import Review

customer1 = Customer('Patrick', 'Ngatia')
customer2 = Customer('Purity', 'Ngatia')

all_customers = Customer.all()
for Customer in all_customers:
    print(Customer.full_name())

restaurant = Restaurant('Angani')

review = Review(customer1, restaurant, 5)
review = Review(customer2, restaurant, 3)

all_reviews = Review.all()
for review in all_reviews:
    print(f'Rating: {review.rating()} by {review.customer.full_name()} for {review.restaurant.name()}')