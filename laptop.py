class Laptop():
	""" A class to manage the laptop info"""

	def __init__(self, color, model, RAM, OS, manu):
		""" Initialize the class."""
		self.color = color
		self.model = model
		self.RAM = RAM
		self.OS = OS
		self.manu = manu

	def lap_desc(self):
		desc = f"Model ==>> {self.model}\nManufacturer ==>> {self.manu}\n"
		desc += f"Color ==>> {self.color}\nOperating Sysytem ==>> {self.OS}\n"
		desc += f"RAM == {self.RAM}"
		return desc

	def update_model(self, model):
		self.model = model

	def update_ram(self, ram):
		self.RAM = ram

	def update_os(self, os):
		self.OS = os

my_laptop = Laptop('Grey', 'HP ProBook 430 G2', '4G',
				   'Windows Microsoft 8 Enterprise',
				   'Hewlett-Packard')
lynx_laptop = Laptop('Golden', 'HP Pavilion', '8GB',
					 'Windows Microsoft 10 Home',
					 'Hewlett-Packard')

'''print(my_laptop.lap_desc())
my_laptop.update_model('Dell xps 15')
print(my_laptop.lap_desc())'''
print(lynx_laptop.lap_desc())