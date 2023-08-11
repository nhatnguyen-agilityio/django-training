import anagram_sets
import shelve

def store_anagrams():
    anagram_map = anagram_sets.all_anagrams('words.txt')
    shelf = shelve.open("chapter14.db", "c")
    for word, list_word in anagram_map.items():
        shelf[word] = list_word
    shelf.close()


def read_anagrams(filename, word):
    shelf = shelve.open(filename)
    w = anagram_sets.signature(word)
    try:
        return shelf[w]
    except:
        print("Something went wrong!")


store_anagrams()
print(read_anagrams("chapter14.db", "aecrs"))
