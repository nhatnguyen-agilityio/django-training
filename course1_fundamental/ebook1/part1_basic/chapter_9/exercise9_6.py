def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True

def read_words(filename="words.txt"):
    fin = open(filename)
    count = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            count += 1
    return count

if __name__ == "__main__":
    count = read_words()
    print("Number of words are alphabetical order: {0}".format(count))