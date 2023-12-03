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

review1 = Review(customer1, restaurant1, 5)
review2 = Review(customer2, restaurant2, 3)
review3 = Review(customer2, restaurant1, 7)
review4 = Review(customer3, restaurant2, 4)
# get all reviews
all_reviews = Review.all()
for review in all_reviews:
    print(f"Rating: {review.get_rating()} by {review.customer.full_name()} for {review.restaurant._name}")

# Add some reviews to Restaurant 1
review_1_1 = Review(customer1, restaurant1, 5)
restaurant1.add_review(review_1_1)
review_1_2 = Review(customer2, restaurant1, 7)
restaurant1.add_review(review_1_2)

# Get reviews for a specific restaurant
print("\nReviews for Restaurant Angani:")
restaurant_reviews = [review.get_rating() for review in restaurant1.reviews]
print(restaurant_reviews)

# Calculate average star rating for Restaurant A
print("\nAverage Star Rating for Restaurant Angani:")
print(restaurant1.star_rating())

# Get unique customers who reviewed Restaurant A
print("\nCustomers who reviewed Restaurant A:")
restaurant_customers = [customer.full_name() for customer in restaurant1.customers()]
print(restaurant_customers)

# Find all customers with a given name
customers_with_given_name = Customer.find_by_given_name("Purity")
if customers_with_given_name:
    print("\nCustomers with Given Name:")
    for customer in customers_with_given_name:
        print(customer.full_name())

# Find customer by full name
found_customer = Customer.find_name("Patrick Ngatia")
if found_customer:
    print("\nFound Customer by Name:")
    print(found_customer.full_name())