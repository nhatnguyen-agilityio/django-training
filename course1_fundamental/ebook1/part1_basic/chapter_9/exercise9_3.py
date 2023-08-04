def avoid(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True

def read_words(filename="words.txt"):
    fin = open(filename)
    total = 0
    try:
        forbidden_letter = input("Enter a string of forbidden letters:")
        for word in fin:
            if avoid(word, forbidden_letter):
                total += 1
        print("Number of the words that don't contain any forbidden letters: {0}".format(total))
    except:
        raise KeyError("Please enter a string of forbidden letters!!!")

if __name__ == "__main__":
    read_words()
