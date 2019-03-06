class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type =  cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name.title() + " restarant offers the best " + self.cuisine_type.title() + " in the city." ) 

	def open_restaurant(self):
		print(self.restaurant_type.title() + " restarant is now open .")

	

class IceCreamStand(Restaurant):
	def __init__(self, first_tast, second_tast):
		super().__init__(first_tast, second_tast)

	def flavors(self):
		print(self.cuisine_type.title() + " and " + self.restarant_name  + ", are my best icecream fravers.")	

restarant = IceCreamStand('berry', 'milk')
print(restarant.flavors())
print()

