def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

def read_words():
    fin = open("words.txt")
    count = 0
    for line in fin:
        word = line.strip()
        if uses_only(word, 'acefhlo'):
            print(word)
            count += 1
    return count

print("Total words: {}".format(read_words()))