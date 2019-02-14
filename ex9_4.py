class Restaurant():

	def __init__(self, restarant_name, cuisine_type):
		self.restarant_name = restarant_name
		self.cuisine_type =  cuisine_type
		self.number_served  = 0


	def describe_restaurant(self):
		print(self.restarant_name.title() + " restaurant is the best in the city.")
		print(self.restarant_name.title() + " restaurant offer goods at very low prices.")

	def open_restaurant(self):
		print(self.cuisine_type.title() + " restarant is now open .")

	def restaurant(self):
		print("The number of customers server were " + str(self.number_served))	
	
	def set_number (self, served):
		if served >= self.number_served:
			self.number_served = served
		else:
			print("no customer was served")
	def increment_number_served(self, numbers):
		self.number_served += numbers
				
customer_served = Restaurant('Winda', "kamangu_garden")
print(customer_served.restaurant())
 
customer_served.set_number(100)
customer_served.restaurant()

customer_served.increment_number_served(200)
customer_served.restaurant()