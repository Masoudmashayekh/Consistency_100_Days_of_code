# Creating Class 
# Class is Blueprint

# car.speed object.Attribute

# Step 1: 
#       class Car:
# camelCase, snake_case
class User:   # Class => PascalCase
    def __init__(self, user_id, username):
        self.id = user_id # Attributes
        self.username = username # Attributes
        self.followers = 0
        self.following = 0
        
    def follow(self, user):  # method
       user.followers += 1
       self.following += 1
       
# user_1 = User() # Object = Class
# Creating Attribute, an attribute is a variable that's associated with an object.
# user_1.id = "001"
# user_1.username = "Masoud"

# print(user_1.username)

# Constructor or Initializing object
# def __init__(self):
#   Initialise attributes

user_1 = User("001", "Masoud")
user_2 = User("002", "Angela")
# The attributes are the things that the object has and the methods are the things that the object does.

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)