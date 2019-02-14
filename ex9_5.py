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

describe_user = User("paul", "ndung'u")
print(describe_user.first_name.title() + " is a male.")
print(describe_user.last_name.title() + " love coding.")
print(describe_user.first_name.title() + " live in kikuyu.")
print(describe_user.first_name.title() + " is black in color and white eyes.")
describe_user.first_name
print()
describe_user.increment_login_attempts(12)
describe_user.read_increment()
describe_user.add_increacement(300)
describe_user.read_increment()
print()
describe_user.reset_loging_attempts(200)
describe_user.read_increment()
describe_user.reset_loging_attempts(80)
describe_user.read_increment()
describe_user.reset_loging_attempts(32)
describe_user.read_increment()
print()


describe_user.age()
print()

friend_user = User("james", "muiruri")
print(friend_user.first_name.title() + " is a male.")
print(friend_user.last_name.title() + " love coding.")
print(friend_user.first_name.title() + " live in kikuyu.")
print(friend_user.first_name.title() + " he has only two followers in facebook..")

friend_user.first_name
print()
another_friend = User("kimathi", "Maina")#
print(another_friend.first_name.title() + " is my friends first name.")
print(another_friend.last_name.title() + " is his last name. ")
print()
another_friend.first_name

