import math

def mysqrt(a):
    x = 3
    while True:
        y = (x + a/x) / 2
        if y == x:
            return y
        x = y

def test_square_root():
    a = 1
    print("a " + "mysqrt(a)   " + "     math.sqrt(a)   " )
    while a <= 9:
        print(a, end=" ")
        print(mysqrt(a), end="     ")
        print(math.sqrt(a))
        a += 1

test_square_root()