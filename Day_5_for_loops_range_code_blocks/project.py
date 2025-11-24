import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
 "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!", "#", "&", "%", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Version
rn_letters = ""
for letter in range(0,nr_letters):
    letter = random.choice(letters)
    rn_letters += letter
for sympol in range(0,nr_symbols):
    symbol = random.choice(symbols)
    rn_letters += symbol
for number in range(0,nr_numbers):
    number = random.choice(numbers)
    rn_letters += number
    
print(rn_letters)
# Hard Version
mixed = ''.join(random.sample(rn_letters, len(rn_letters)))
print(mixed)


# Shuffle characters in a string.  mixed = ''.join(random.sample(s, len(s)))
# Shuffle list of characters. random.shuffle(chars)