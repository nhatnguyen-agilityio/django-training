def read_words():
    fin = open("words.txt")
    list_words = []
    for line in fin:
        word = line.strip()
        list_words.append(word)
    return list_words

def in_bisect(list_words, word):
    part_list = len(list_words) // 2
    if len(list_words) == 0:
        return False
    if list_words[part_list] == word:
        return True
    elif list_words[part_list] > word:
        return in_bisect(list_words[:part_list], word)
    else:
        return in_bisect(list_words[part_list+1:], word)

list_words = read_words()
list_words_need_check = ["aa", "abacus", "jargoon", "sneerer", "nhat"]

for item in list_words_need_check:
    if in_bisect(list_words, item):
        print("Word {0} in the list".format(item))
    else:
        print("Word {0} not in the list".format(item))


