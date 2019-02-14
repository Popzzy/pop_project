class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.increment_reading = 1
	def age(self):
		print(self.first_name.title() + " is 21 years old.")
		print(self.first_name.title() + " is addicted to python.")

	def nickname(self):
		print(self.last_name.title() + " nickname is pop or popzy.")
	def read_increment(self):
		print("THis is the new increasement " + str(self.increment_reading) + '.')


	def increment_login_attempts(self, increment):
		if increment >= self.increment_reading:
			self.increment_reading = increment
		else:
			print("There is only increasement and does not decrease.")
	def add_increacement(self, addition):
		self.increment_reading += addition

	def reset_loging_attempts(self, addition):
		self.increment_reading -= addition

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.can_add_post = "can add post"
		self.can_delete_post = "can delete post"
		self.can_ban_user = "can ban user"
	def show_privaleges(self):
		print(self.can_add_post + ', ' + self.can_delete_post + ', ' + self.can_ban_user + '.')
describe_user = Admin("paul", "ndung'u")
print(describe_user.show_privaleges())
print()
