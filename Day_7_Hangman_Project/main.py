import random # Review: For & While Loops, If/else, Lists, Strings, Range, Modules
from hangman_words import word_list
from hangman_art import HANGMANPICS

# TODO-1 - Randomly choose a word from the word_list 
chosen_word = random.choice(word_list)
list_chosen_word = list(chosen_word)
print(chosen_word)
print(list_chosen_word)
num_chosen_word = list(len(chosen_word)*"_")

# TODO-2 - Ask the user to guess a letter 
print(num_chosen_word)


lives = 6
hangman = 0
game_over = False
while not game_over :
    print(f"*** {lives}/6 Lives left ***")
    guess = input("Guess a letter: ").lower()
    
    # TODO-3 - Check if the letter the user guessed is right or wrong.
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            num_chosen_word[i] = guess  
    
    final_word = "".join(num_chosen_word)
    print(final_word)
    if guess in num_chosen_word:
        hangman == hangman
        print(HANGMANPICS[hangman])
        if "_" not in num_chosen_word:
            print("You Win!")
            game_over = True
    else:
        hangman += 1
        lives -= 1
        print(HANGMANPICS[hangman])
        if lives == 0:
            game_over = True
            print("Game Over!")
            
    
    

            
                   