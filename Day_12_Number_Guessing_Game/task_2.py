# There is no Block Scope in Python!

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy_1 = enemies[0] # new_enemy is global scope
     
print(new_enemy_1)


def create_enemy():
    if game_level < 5:
        new_enemy_2 = enemies[1] # new_enemy is Local scope
        
# print(new_enemy_2) NameError: name 'new_enemy_2' is not defined