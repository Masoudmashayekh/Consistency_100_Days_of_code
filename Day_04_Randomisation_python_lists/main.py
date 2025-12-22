import random
import my_module
# Randomisation
random_integer = random.randint(1,10)
print(random_integer)

#Modules
print(my_module.my_favorite_number)

# Radom floating random.random()
random_float = random.random() * 10
print(random_float)

random_float_2 = random.uniform(1,10)
print(random_float_2)


random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")