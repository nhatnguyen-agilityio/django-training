def read_words():
    fin = open("words.txt")
    list_words = []
    for line in fin:
        word = line.strip().lower()
        list_words.append(word)
    return list_words


dict_words = {}
list_words = read_words()

for word in list_words:
    new_list = list(word)
    new_list.sort()
    sort_word = "".join(new_list)
    if sort_word not in dict_words:
        dict_words[sort_word] = [word]
    else:
        dict_words[sort_word].append(word)

for value in dict_words.values():
    if len(value) > 1:
        print(value) 