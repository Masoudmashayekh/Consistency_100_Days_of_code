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
# Unlimited Arguments
def add(*args):
    number = 0
    for n in args:
        number += n
    return number
        
print(add(5,5,5))



