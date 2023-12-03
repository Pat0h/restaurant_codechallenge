class Review:

    _all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self._rating = rating
        Review._all_reviews.append(self)

    def get_rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls._all_reviews
