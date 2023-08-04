def is_palindrome(word):
    return word == word[::-1]

def find_number(number):
    if is_palindrome(str(number)[2:]):
        number += 1
        if is_palindrome(str(number)[1:]):
            number += 1
            if is_palindrome(str(number)[1:5]):
                number += 1
                if is_palindrome(str(number)):
                    return True
    return False

if __name__ == "__main__":
    for n in range(300000, 3000000):
        if find_number(n):
            print("Number: {0}".format(n))