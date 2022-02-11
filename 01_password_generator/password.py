# The password to have at least one lowercase letter
# It should also have at least one uppercase letter
# At least on digit included
# It should contain a symbol e.g (!@>^)
# The password should be 16 characters minimum
# Program to generate a new set of random password every time it is called
# Example password: 5Vpa8c[@}*5$'cP>

import random
import string


def generate_password():
    # generate one lowercase, one digit, one uppsercase and symbol
    password = random.choice(string.ascii_lowercase)  # e.g b
    password += random.choice(string.ascii_uppercase)  # e.g T
    password += random.choice(string.digits)  # e.g 9
    password += random.choice(string.punctuation)  # e.g @

    # add 12 random letters, digits and punctuations into the mix
    random_source = string.ascii_letters + string.digits + string.punctuation
    for i in range(12):
        password += random.choice(random_source)

    password_list = list(password)  # ['s','T','$'...]
    random.shuffle(password_list)

    # join list back into string and return result
    password = "".join(password_list)
    return password


print("Random Password is: ", generate_password())
