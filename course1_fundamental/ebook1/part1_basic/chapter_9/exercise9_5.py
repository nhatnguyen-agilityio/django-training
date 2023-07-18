def uses_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True

def read_words():
    fin = open("words.txt")
    count = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, "aardvark"):
            print(word)
            count += 1
    return count

print("Total words: {0}".format(read_words()))