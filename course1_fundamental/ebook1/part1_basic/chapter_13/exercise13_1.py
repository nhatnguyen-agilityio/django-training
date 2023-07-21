import string

def read_words():
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        new_word = ""
        for letter in word:
            if letter not in string.punctuation:
                new_word += letter
        print(new_word.lower())

read_words()
