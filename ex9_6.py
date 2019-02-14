class Restaurant():

	def __init__(self, restarant_name, cuisine_type):
		self.restarant_name = restarant_name
		self.cuisine_type =  cuisine_type
	def describe_restaurant(self):
		print(self.restarant_name.title() + " restarant is the best in the city.")
		print(self.cuisine_type.title() + " restarant offer goods at very low prices.")

	

class IceCreamStand(Restaurant):
	def __init__(self, first_tast, second_tast):
		super().__init__(first_tast, second_tast)

	def flavors(self):
		print(self.cuisine_type.title() + " and " + self.restarant_name  + ", are my best icecream fravers.")	

restarant = IceCreamStand('berry', 'milk')
print(restarant.flavors())
print()

