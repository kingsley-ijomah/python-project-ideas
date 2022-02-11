import random

"""
Rock vs paper -> paper wins
Rock vs scissor -> Rock wins
paper vs scissor -> scissor wins 
"""

ROCK = 1
PAPER = 2
SCISSOR = 3

choice_names = {ROCK: "Rock", PAPER: "Paper", SCISSOR: "Scissor"}

while True:
    print("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor\n")

    # Accept user input and start the game
    user_choice = int(input("Your turn: "))

    # validate input
    while user_choice > SCISSOR or user_choice < ROCK:
        user_choice = int(input("Enter valid input: "))

    # print out chosen name
    print("Your choice is: " + choice_names[user_choice])

    # computer makes random selection
    comp_choice = random.randint(ROCK, SCISSOR)

    # handle a tie
    while comp_choice == user_choice:
        comp_choice = random.randint(ROCK, SCISSOR)

    # print computer's selection
    print("Computer's choice is: " + choice_names[comp_choice])

    # calculate results
    if (user_choice == ROCK and comp_choice == PAPER) or (
        user_choice == PAPER and comp_choice == ROCK
    ):
        result = choice_names[PAPER]
    elif (user_choice == ROCK and comp_choice == SCISSOR) or (
        user_choice == SCISSOR and comp_choice == ROCK
    ):
        result = choice_names[ROCK]
    else:
        result = choice_names[SCISSOR]

    # check who owns the result
    if result == choice_names[user_choice]:
        print("You won!!! :)")
    else:
        print("Computer wins :(")

    print("Do you want to play again? (Y/N)")
    answer = input()

    if answer.lower() == "n":
        break

print("\nThanks for playing")

