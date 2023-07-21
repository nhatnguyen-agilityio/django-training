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
w_list = ["abc", "nhat", "your", "okokok"]
new_list = []

for k in list_words:
    if k not in w_list:
        new_list.append(k)

print(new_list)
