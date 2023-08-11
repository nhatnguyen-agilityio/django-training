def read_words():
    fin = open("words.txt")
    list_words = []
    for line in fin:
        word = line.strip()
        list_words.append(word)
    return list_words

def revert(word):
    return word[::-1]

list_words = read_words()
for item in list_words:
    if revert(item) in list_words:
        print(item, revert(item))


