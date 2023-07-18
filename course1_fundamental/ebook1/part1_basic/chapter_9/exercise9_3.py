def avoid(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True

def read_words():
    fin = open("words.txt")
    total = 0
    forbidden_letter = input("Enter a sting of forbidden letters:")
    for word in fin:
        # print(word)
        # print(avoid(word, forbidden_letter))
        if avoid(word, forbidden_letter):
            total += 1
    print("Number of the words that don't contain any forbidden letters: {0}".format(total))

read_words()
