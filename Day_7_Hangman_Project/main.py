import random # Review: For & While Loops, If/else, Lists, Strings, Range, Modules
word_list =["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list 
chosen_word = random.choice(word_list)
letter_chosen_word = list(chosen_word)
print(chosen_word)
print(letter_chosen_word)

# TODO-2 - Ask the user to guess a letter 
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed is right or wrong.
for letter in letter_chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
