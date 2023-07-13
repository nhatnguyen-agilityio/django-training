def input_values():
    a = input("a=")
    b = input("b=")
    c = input("c=")
    n = input("n=")
    check_fermat(int(a), int(b), int(c), int(n))

def check_fermat(a, b, c, n):
    if n > 2:
        if ((a**n) + (b**n)) == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work")
    else: 
        return
    
input_values()
