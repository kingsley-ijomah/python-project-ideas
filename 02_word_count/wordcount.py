# Lines
# Words
# Characters


def wordcount(file):
    filename = file
    numLines = 0
    numWords = 0
    numChars = 0

    with open(filename, "r") as file:
        for line in file:
            numLines += 1
            numWords += len(line.split())
            numChars += len(line)

    return f"Lines: {numLines}\nWords: {numWords}\nCharacters: {numChars}"


print(wordcount("words.txt"))
