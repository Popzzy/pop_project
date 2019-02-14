from ex9_6 import Restaurant

class IceCreamStand(Restaurant):
	def __init__(self, first_tast, second_tast):
		super().__init__(first_tast, second_tast)

	def flavors(self):
		print(self.cuisine_type.title() + " and " + self.restarant_name  + ", are my best icecream fravers.")	

restarant = IceCreamStand('berry', 'milk')
print(restarant.flavors())
print()

restarant = Restaurant("milk", 'batter')
restarant.describe_restaurant()


	