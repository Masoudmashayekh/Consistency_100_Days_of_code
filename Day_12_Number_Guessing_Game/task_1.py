# Name spaces: Local Vs. Global scope

# Global scope
enemies = 1

def increase_enemies():
    # Local scope
    enemies = 2
    print(f"enemies inside function {enemies}")
    

increase_enemies()
print(f"enemies outside function {enemies}")


# Local scope
def drink_potion():
    potion_strength = 2
    print( potion_strength)
    
drink_potion()
#print(potion_strength)   NameError: name 'potion_strength' is not defined

# Global scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)
    
    
drink_potion()