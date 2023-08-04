def has_no_e(word):
    if "e" not in word:
        return True
    return False

def read_words(filename='words.txt'):
    fin = open(filename)
    total_words = 0
    total_words_no_e = 0
    for word in fin:
        total_words += 1
        if has_no_e(word):
            total_words_no_e += 1
            print(word)
    
    percentage_no_e = (total_words_no_e*100)/total_words
    print(percentage_no_e)
    
if __name__ == '__main__':
    read_words()
