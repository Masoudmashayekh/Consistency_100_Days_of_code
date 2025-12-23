# How to Modify a Global Variable


enemies = 1

# def increase_enemies():
#     enemies += 2 # UnboundLocalError: cannot access local variable 'enemies' where it is not associated with a value
#     print(f"enemies inside function {enemies}")

def increase_enemies():
    global enemies
    enemies += 2 
    print(f"enemies inside function {enemies}")    

increase_enemies()
print(f"enemies outside function {enemies}")
