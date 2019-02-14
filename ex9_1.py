class Restaurant():

	def __init__(self, restarant_name, cuisine_type):
		self.restarant_name = restarant_name
		self.cuisine_type =  cuisine_type
	def describe_restaurant(self):
		print(self.restarant_name.title() + " restarant is the best in the city.")
		print(self.restarant_name.title() + " restarant offer goods at very low prices.")

	def open_restaurant(self):
		print(self.cuisine_type.title() + " restarant is now open .")

restarant = Restaurant("winda", "The")
print(restarant.restarant_name.title() + " motel is alone the highway.")
print(restarant.cuisine_type.title() + " hotel has a lot of warkers.")

restarant.cuisine_type
print("\n")	

restarant.describe_restaurant()