class User():
	def __init__(self, first_name, last_name, date_birth, password):
		self.first_name = first_name
		self.last_name = last_name
		self.date_birth = date_birth
		self.password = password
		self.login_attempts = 0

	def	descride_user(self):
		summary = self.first_name.title() + ' ' + self.last_name.title()
		summary += ' ' +str(self.date_birth) + ' ' + self.password.lower()
		print(summary)
	

	def increment_login_attempts(self, number):
		self.login_attempts += number + 1

	def reset_login_attempts(self,item):
		self.login_attempts += item - item		

	def greet_user(self):
		print("Hello " + self.first_name + ' ' + self.last_name + '.')

trizzer = User("pop", "ndungu", 40, "popopoppp")
friend = User("jymoh", "muiruri", 38, "james")
exter = User("maish", "elephant", 20, "asshole")

trizzer.increment_login_attempts(3)
friend.reset_login_attempts(4)

print(trizzer.login_attempts)
print(friend.login_attempts)
