import random # Review: For & While Loops, If/else, Lists, Strings, Range, Modules
word_list =["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list 
chosen_word = random.choice(word_list)
list_chosen_word = list(chosen_word)
print(chosen_word)
print(list_chosen_word)
num_chosen_word = list(len(chosen_word)*"_")

# TODO-2 - Ask the user to guess a letter 
print(num_chosen_word)
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed is right or wrong.
position = []
for letter in list_chosen_word:
    if letter == guess:
        n = list_chosen_word.index(letter)
        print(n)
        position.append(n)
    else:
        pass 
print(position)
            
                   
print("".join(num_chosen_word))