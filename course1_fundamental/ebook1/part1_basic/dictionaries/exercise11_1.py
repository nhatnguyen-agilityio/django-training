def read_words():
    fin = open("words.txt")
    dict_words = {}
    for line in fin:
        word = line.strip()
        dict_words[word] = "abc"
    return dict_words

dict_words = read_words()
print("aa" in dict_words)
print("nhat" in dict_words)
