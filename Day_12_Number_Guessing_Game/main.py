import random
play_again = True
print("Welcome to Number Guessing Game!")
while play_again:
    print("I'm thinking of a number between 1 and 100.")
    ANSWER_NUMBER = random.randint(1,100)
    print(ANSWER_NUMBER)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").capitalize()
    if difficulty == "Easy":
        i = 10
    elif difficulty == "Hard":
        i = 5
    else:
        print("You type wrong input!!!")
    while i > 0:    
        print(f"You have {i} attempts remaining to guess the number.")
        guess_num = int(input("Make a guess: "))
        if guess_num > ANSWER_NUMBER:
            print("Too high.")
            print("Guess again.")
            i -= 1
            if i == 0:
                print("loss")
        elif guess_num < ANSWER_NUMBER:
            print("Too lowr.")
            print("Guess again.")
            i -= 1
            if i == 0:
                print("loss")
        else:
            print("You win!")
            i = 0
    play = input("Do you want to play again? Type 'y' or 'n'. ").capitalize()
    if play == "N":
        play_again = False
        print("See you later Good boy!")