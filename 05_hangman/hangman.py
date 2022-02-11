import random

HANGMAN = (
    """
-----
|   |
|
|
|
|
|
|
|
--------
""",
    """
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
    """
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
    """
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
    """
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
    """
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
    """
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
    """
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
    """
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
    """
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
    """
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""",
)

# list of words to guess
word_list = ["python", "table", "chairs", "computer"]

# choose first word at random
word = list(random.choice(word_list))  # ['p','y'...]

# list of guessed letters or '_' if not guessed
display = []

# list holding all guessed letters
guessed_letters = []

# hold same content as word
display.extend(word)
guessed_letters.extend(display)

for i in range(len(display)):
    display[i] = "_"

print(" ".join(display))
print()
print("Total letters: ", len(display))
print()

# we are counting life from 0 - 10
life = len(HANGMAN)

while list.count(display, "_") > 0 and life != 0:
    guess = input("Please guess a letter or full word: ")
    guess = guess.lower()

    if guess == "".join(word):
        display = list(guess)
        print("\nYay! You scored all letters!")
        print(" ".join(display))
        break

    for i in range(len(word)):
        if word[i] == guess and guess in guessed_letters:
            display[i] = guess
            guessed_letters.remove(guess)

    if guess not in display:
        print("Sorry, wrong guess")
        # decrease life by 1
        life -= 1

    # as life is lost, this will count from 1, 2, 3 etc
    print(HANGMAN[(len(HANGMAN) - 1) - life])
    print(" ".join(display))
    print()

print("\nGame Over!")
