def find_consecutive_double_letters(word):
    number_double_letter = 0
    index = 0
    while index < len(word)-1:
        if word[index] == word[index+1]:
            number_double_letter += 1
            if number_double_letter == 3:
                return True
            index += 2
        else:
            index += 1
            number_double_letter = 0

def read_words(filename="words.txt"):
    fin = open(filename)
    count = 0
    for line in fin:
        word = line.strip()
        if find_consecutive_double_letters(word):
            print("The word is consecutive double letters: {0}".format(word))
            count += 1
    return count

if __name__ == "__main__":
    count = read_words()
    print("Number of word is consecutive double letters: {0}".format(count))