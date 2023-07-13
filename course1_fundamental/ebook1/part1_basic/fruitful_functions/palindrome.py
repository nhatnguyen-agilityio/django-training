def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1: -1]

def is_palindrome(value):
    if len(value) <= 1:
        return True
    if first(value) != last(value):
        return False
    return is_palindrome(middle(value))

print(is_palindrome("join"))
print(is_palindrome("joinnioj"))




# print(middle("sd"))
# print(type(middle("a")))
# print(len(middle("")))