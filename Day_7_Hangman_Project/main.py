import random # Review: For & While Loops, If/else, Lists, Strings, Range, Modules
word_list =["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list 
chosen_word = random.choice(word_list)
letter_random_word = list(chosen_word)
print(chosen_word)
print(letter_random_word)

# TODO-2 - Ask the user to guess a letter 
guess_letter = input("Guess a letter: ")

# TODO-3 - Check if the letter the user guessed is right or wrong.
for letter in letter_random_word:
    if letter == guess_letter:
        print("Right")
    else:
        print("Wrong")
