def find_words_one_elenment(word):
    list_words = word.split()
    if len(list_words) == 1:
        return True
    return False

def read_words1():
    fin = open("words.txt")
    list_words = []
    for line in fin:
        word = line.strip()
        if find_words_one_elenment(word):
            list_words.append(word)
    return list_words

def read_words2():
    fin = open("words.txt")
    list_words = []
    for line in fin:
        word = line.strip()
        if find_words_one_elenment(word):
            list_words = list_words + [word]
    return list_words

print("List words only have one element: {0}".format(read_words1()))
print("List words only have one element: {0}".format(read_words2()))
