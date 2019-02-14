class Restaurant():
	def __init__(self, restaurant_a, restaurant_b, restaurant_c):
		self.restaurant_a = restaurant_a
		self.restaurant_b = restaurant_b
		self.restaurant_c = restaurant_c

	def gall(self):
		print(self.restaurant_a.title() + " hotel has the best gall in town.")

	def foods(self):
		print(self.restaurant_b.title() + " motel has better food than the rest.")

	def swimming_pool(self):
		print(self.restaurant_c.title() + " result has a worm swimming pool.")

describe_restaurant = Restaurant("Rio", "kamangu gardens", "KFCC")

print(describe_restaurant.restaurant_a.title() + " holel has very beautiful waiters.")
print("I love " + describe_restaurant.restaurant_b.title() + " hotel for its environment.")
print(describe_restaurant.restaurant_c.title() + " hotel has very friendly people.")

describe_restaurant.restaurant_a
print()
describe_restaurant.gall()
print()
describe_restaurant.foods()
print()
describe_restaurant.swimming_pool()		
