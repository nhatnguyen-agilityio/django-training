import random

suffix_map = {}
prefix = ()

def remove_header_line(fin):
    for line in fin:
        if line.startswith("*** START OF THIS"):
            break

def process_word(word, order):
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)

def shift(t, word):
    return t[1:] + (word,)

def random_text(n=100):
    start = random.choice(list(suffix_map.keys()))
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            random_text(n-i)
            return

        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)
        

def read_words():
    fin = open("gutenberg.txt")
    for line in fin:
        if line.startswith("*** START OF THIS") or line.startswith('*** END OF THIS'):
            continue
        for word in line.rstrip().split():
            process_word(word, 2)
    random_text(100)
    print()

read_words()
