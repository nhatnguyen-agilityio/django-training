def rotate_letter(letter, n):
    if letter.isupper():
        start = ord("A")
    elif letter.islower():
        start = ord("a")
    else:
        return letter
    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    result = ""
    for letter in word:
        result = result + rotate_letter(letter, n)
    return result

def read_words():
    fin = open("words.txt")
    list_words = []
    for line in fin:
        word = line.strip()
        list_words.append(word)
    return list_words

words_dict = {}
list_words = read_words()
for word in list_words:
    words_dict[word] = rotate_word(word, 3)

for word in words_dict:
    print(word, words_dict[word])
        