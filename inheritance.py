class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles
class Battery():
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		'''print a statemennt describing the battery size'''
		print("This car has a " + str(self.battery_size) + "-kmh battery.")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += "miles on a full charge."
		print(message)		
			
class ElecticCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery_size = 70
		self.GPRS = 384
		self.battery = Battery()

	def describe_bettery(self):
		'''print a statement decreibing the battery size.'''
		print("The car has a " + str(self.battery_size) + "-km battery.")
	def describe_Gprs(self):
		print("The car has a GPRS of " + str(self.GPRS) + "-mgp .")	
		
	def fill_gas_tank11():
		'''Electric cars do not have gas tannks'''
		print("This car does not need a gass tank!")	
my_tesla = ElecticCar('tesla', "model's", 2016)
print()
print(my_tesla.get_descriptive_name())
print()
my_tesla.describe_bettery()
print()
my_tesla.describe_Gprs()
print()
my_tesla.battery.describe_battery()
print()
my_tesla.battery.get_range()
print()