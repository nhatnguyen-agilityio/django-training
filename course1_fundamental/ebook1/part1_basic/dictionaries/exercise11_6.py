def read_dict():
    fin = open("c06d.txt")
    dict_words = {}
    for line in fin:
        if line[0] == '#':
            continue
        t = line.split()
        word = t[0].lower()
        pron = " ".join(t[1:])
        dict_words[word] = pron
    return dict_words

dict_words = read_dict()
for key, value in dict_words.items():
    print(key, value)
