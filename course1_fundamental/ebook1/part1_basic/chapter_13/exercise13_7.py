import string
import random

def read_words(filename="gutenberg.txt"):
    fin = open(filename)
    list_words = []
    for line in fin:
        words_in_line = line.strip().split(" ")
        for w in words_in_line:
            word = w.strip()
            new_word = ""
            for letter in word:
                if letter not in string.punctuation:
                    new_word += letter
            list_words.append(new_word)
    return list_words

def find_index(list):
    number_of_list = len(list)
    return random.randint(0, number_of_list-1)

if __name__ == "__main__":
    list_words = read_words()
    print("Word: {0}".format(list_words[find_index(list_words)]))
    print("Word: {0}".format(list_words[find_index(list_words)]))
    print("Word: {0}".format(list_words[find_index(list_words)]))