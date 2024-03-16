# Defining the alter of words
def pig_latin(word):
    vowels = "a, e, i, o, u, A, E, I, O, U"
    if word[0] in vowels:
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


# Reading from a text file
with open("input.txt", "r") as input_file:
    input_text = input_file.read()

# splitting the input into a list
words = input_text.split()

# Converting the words to piglatin
pig_latin_words = [pig_latin(word) for word in words]

# Creating a string with spaces
output_text = " ".join(pig_latin_words)

# Writing to a text file
with open('output.txt', "w") as output_file:
    output_file.write(output_text)
