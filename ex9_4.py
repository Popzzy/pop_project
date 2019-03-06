class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type =  cuisine_type
		self.number_served = 0
	def describe_restaurant(self):
		print(self.restaurant_name.title() + " restarant offers the best " + self.cuisine_type.title() + " in the city." ) 


	def set_number_served(self, served):
		if served > self.number_served:
			print("The new number of customers served is :")
			self.number_served = served
		else:
			print("number_served must increase")
	def increment_number_served(self, customers):
		print("The new number of customers served is :")
		self.number_served += customers
					
	def open_restaurant(self):
		print(self.restaurant_type.title() + " restarant is now open .")

restaurant = Restaurant("winda", "ugali")
restaurant.describe_restaurant()
restaurant.set_number_served(40)
restaurant.increment_number_served(80)
print(restaurant.number_served)