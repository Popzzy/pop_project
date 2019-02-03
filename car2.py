"""class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model + '.'
		return long_name
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):
		#set the odometer reading to the given value
		
		'''set the odometer reading to the given value.
		Reject the changes if it attempts to roll the odometer back'''
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")	

	def increment_odometer(self, miles):
		#add the given amount to the odometer reading
		self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()



my_new_car = Car('audi', 'a4', 2017)
print(my_new_car.get_descriptive_name())

my_used_car.increment_odometer(100)
my_used_car.read_odometer()			
my_new_car.read_odometer()


my_new_car.update_odometer(23)
my_new_car.read_odometer()"""

class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.speed = 280

	def compony_cars(self):
		full_name = str(self.year) + ' ' + self.make + ' ' + self.model	
		return full_name
	def speed_limit(self):
		print("The new cars speed limit is " + str(self.speed))
	def update_speed(self, first):
		if first >= self.speed:
			self.speed = first
		else:
			print("You can't roll back ")
	def increment_speed(self, miles):
		self.speed += miles
my_used_car = Car('Subaru', 'outback', '2014')
print(my_used_car.compony_cars())
my_used_car.update_speed(490)
my_used_car.speed_limit()
my_used_car.update_speed(590)
my_used_car.speed_limit()						
				
full_name = Car('isuzu', 'DMax', 2019)

print(full_name.compony_cars())
full_name.update_speed(480)
full_name.speed_limit()

