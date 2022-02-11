# guess number between a range eg. 1 - 50
# prompt what number am I guessing?
# 5 total guess chances
# tell user if guess is higher or lower than anwer
# if successful print total attempts used to reach answer
# if unsuccessful print the correct answer

import random

MAX = 50
MIN = 1
total_guess = 0
number = random.randrange(MIN, MAX)
player = input("Hey, What's your name?: ")
print(f"okay! {player} What number am I guessing between {MIN} and {MAX}")

while total_guess < 5:
    guess = int(input())
    total_guess += 1
    if guess < number:
        print("Your guess is too low")
        print("Try again:")
    if guess > number:
        print("Your guess is too high")
        print("Try again:")
    if guess == number:
        break

if guess == number:
    print(f"Yah! solved in { total_guess } attempts")
else:
    print(f"Sorry you failed, correct guess is: { number }")
