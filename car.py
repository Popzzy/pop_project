class Hard_ware():

	def __init__(self, shop_a, shop_b):
		#initialize name of the two shops
		self.shop_a = shop_a
		self.shop_b = shop_b

	def cement(self):
		#simulate a hardware inresponce to a command
		print(self.shop_a.title() + " cement is sold in the shop.")

	def iron_sheet(self):
		#simulate a hardware in responce to a command
		print(self.shop_b.title() + " iron sheet is sold her")

wachuhi = Hard_ware('Tembo', 'Nyumba')
print("Wachuhi shop B hardware sells " + wachuhi.shop_a.title() + " cement.")
	
print("Wachuhi shop A hardware sells " + wachuhi.shop_b.title() + " ironsheet.")
new_kamangu = Hard_ware('matress', 'plates')
print("new " + new_kamangu.shop_a.title() + " are sold by pop.")
print(new_kamangu.shop_a.title() + ' are also sold her.')
new_kamangu.shop_a
wachuhi.shop_a
wachuhi.shop_b
wachuhi.cement()
wachuhi.iron_sheet() 

class Car():
	def __init__(self, make, model, year):
		"""initialize attributes to desribe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_read = 0
		self.speed = 280

	def descride_car(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer_read(self):
		#print a statment showing the car mileage
		print("This car is " + str(self.odometer_read) + " miles on it")

	def speed_limit(self):
		print("My new car has a seed limit is " + str(self.speed))

	def update_odometer(self, mileage):
		#set the odometer reading to the given value	
		self.odometer_read = mileage

my_new_car = Car('BMW', 'Discovery', 2017)
print(my_new_car.descride_car())
my_old_car = Car('Isuzu', 'DMax', 2012)
print(my_old_car.descride_car())		
my_old_car.read_odometer_read()
my_old_car.speed_limit()

my_old_car.odometer_read = 23
my_old_car.read_odometer_read()
my_old_car.speed = 480
my_old_car.speed_limit()
 