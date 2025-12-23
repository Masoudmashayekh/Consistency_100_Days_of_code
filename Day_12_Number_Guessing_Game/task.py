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


# Global scope