def uses_all(word, letters="aalii"):
    for letter in letters:
        if letter not in word:
            return False
    return True

def read_words(filename="words.txt"):
    fin = open(filename)
    count = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, "aardvark"):
            print(word)
            count += 1
    return count

if __name__ == "__main__":
    count = read_words()
    print("Total words: {0}".format(count))