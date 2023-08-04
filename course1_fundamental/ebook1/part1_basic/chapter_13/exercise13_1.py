import string

def read_words(filename="words.txt"):
    fin = open(filename)
    for line in fin:
        word = line.strip()
        new_word = ""
        for letter in word:
            if letter not in string.punctuation:
                new_word += letter
        print(new_word.lower())

if __name__ == "__main__":
    read_words()
