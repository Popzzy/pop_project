class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type =  cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name.title() + " restarant offers the best " + self.cuisine_type.title() + " in the city." ) 

	def open_restaurant(self):
		print(self.restaurant_type.title() + " restarant is now open .")

restaurant = Restaurant("winda", "ugali")
housing = Restaurant("Rio", "kenyan food")
gall = Restaurant("Kamongu", "tanzanian food")

print(restaurant.restaurant_name.title() + " motel is alone the highway.")
print(restaurant.cuisine_type.title() + " hotel has a lot of warkers.")

restaurant.cuisine_type
print("\n")	

restaurant.describe_restaurant()