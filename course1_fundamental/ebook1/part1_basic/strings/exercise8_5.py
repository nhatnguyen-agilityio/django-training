def rotate_letter(letter, n):
    if letter.isupper():
        start = ord("A")
    elif letter.islower():
        start = ord("a")
    else:
        return letter
    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    result = ""
    for letter in word:
        result = result + rotate_letter(letter, n)
    return result

print(rotate_word("First", 3))
        