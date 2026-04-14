# Advanced Python Arguments
#-------------------------------------------------------------------------
# keyword Arguments
# def my_function(a, b, c):
#     Do this with a
#     Then do this with b
#     Finally do this with c
    
# my_function(c= 3, a= 4, b= 5)
#-------------------------------------------------------------------------
# Arguments wiht Default Values : *args: Many positional arguments
# def my_function(c= 3, a= 4, b= 5):
#     Do this with a
#     Then do this with b
#     Finally do this with c
    
# my_function()
# if I want to change something then:
# my_function(b=8)
#-------------------------------------------------------------------------
# Unlimited positional Arguments: *args
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
        
# print(add(3,5,6,4,6,8,9,6,4,2,22,44,66,67))
#-------------------------------------------------------------------------
# **kwargs: Many keyworded Arguments
# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
    
# calculate(2, add= 3, multiply= 5)
#-------------------------------------------------------------------------
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model") # kwargs["model"] is not ok use get
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")
        
my_car = Car(make= "Nissan")
print(my_car.make)
print(my_car.model)

        