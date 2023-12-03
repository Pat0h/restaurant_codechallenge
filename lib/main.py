from customer import Customer
from restaurant import Restaurant
from review import Review

customer1 = Customer('Patrick', 'Ngatia')
customer2 = Customer('Purity', 'Ngatia')
customer3 = Customer('George', 'Washington')

# one customer name
print(customer3.full_name())

# customer change name
customer3._given_name = 'Jane'
print(customer3.full_name())

# get all customers
all_customers = Customer.all()
for Customer in all_customers:
    print(Customer.full_name())

restaurant1 = Restaurant('Angani')
restaurant2 = Restaurant('Comfort')

# get all restaurants
all_restaurants = [ restaurants._name for restaurants in [restaurant2, restaurant1]]
print(all_restaurants)

review = Review(customer1, restaurant1, 5)
review1 = Review(customer2, restaurant2, 3)
review2 = Review(customer1, restaurant1, 7)

# get all reviews
all_reviews = Review.all()
for review in all_reviews:
    print(f"Rating: {review.get_rating()} by {review.customer.full_name()} for {review.restaurant._name}")

# Get reviews for a specific restaurant
print("\nReviews for Restaurant 2:")
restaurant_reviews = [review.get_rating() for review in restaurant2.reviews]
print(restaurant_reviews)


