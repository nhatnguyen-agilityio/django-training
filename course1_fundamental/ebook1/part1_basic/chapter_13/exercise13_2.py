import string

def read_words():
    fin = open("gutenberg.txt")
    count = 0
    list_words = {}
    for line in fin:
        words = line.strip()
        words_in_line = words.split(" ")
        for w in words_in_line:
            word = w.strip()
            new_word = ""
            for letter in word:
                if letter not in string.punctuation:
                    new_word += letter
            if new_word not in list_words:
                list_words[new_word] = 1
                count += 1
            else:
                list_words[new_word] += 1
    return list_words

list_words = read_words()

for k in list_words:
    print(k, list_words[k])
