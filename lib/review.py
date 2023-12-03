class Review:
    _all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review,_all_reviews.append(self)

    def rating(self):
        return self.rating

