# Creating Class 
# Class is Blueprint

# car.speed object.Attribute

# Step 1: 
#       class Car:
# camelCase, snake_case
class User:   # Class => PascalCase
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
    
       
# user_1 = User() # Object = Class
# Creating Attribute, an attribute is a variable that's associated with an object.
# user_1.id = "001"
# user_1.username = "Masoud"

# print(user_1.username)

# Constructor or Initializing object
# def __init__(self):
#   Initialise attributes

user_1 = User("001", "Masoud")
print(user_1.username)