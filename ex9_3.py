class User():
	def __init__(self, first_name, last_name, date_birth, password):
		self.first_name = first_name
		self.last_name = last_name
		self.date_birth = date_birth
		self.password = password

	def	descride_user(self):
		summary = self.first_name.title() + ' ' + self.last_name.title()
		summary += ' ' +str(self.date_birth) + ' ' + self.password.lower()
		print(summary)

	def greet_user(self):
		print("Hello " + self.first_name + ' ' + self.last_name + '.')

trizzer = User("pop", "ndungu", 40, "popopoppp")
friend = User("jymoh", "muiruri", 38, "james")
exter = User("maish", "elephant", 20, "asshole")

trizzer.descride_user()