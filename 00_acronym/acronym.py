# Accept text input
# Take first letter from each word
# Ignore the word `and` if in the list
# Convert result into uppercase letters

# Talk to You later => TTYL
# pretty Awesome new Stuff => PANS
# This and That => TT

words = input("Enter words: ")  # This and That


def acronym(words):
    words = words.split()  # ["This", "and", "That"]
    string = ""
    for word in words:
        if word != "and":
            string += str(word[0])  # T
    return string.upper()


result = acronym(words)
print(result)  # TT
