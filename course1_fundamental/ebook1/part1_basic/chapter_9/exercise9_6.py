def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True

def read_words():
    fin = open("words.txt")
    count = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            count += 1
    return count

print("Number of words are alphabetical order: {0}".format(read_words()))