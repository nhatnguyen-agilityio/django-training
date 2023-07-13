def gcd(a, b):
    if a == 0 or b == 0:
        return a + b
    elif a != b:
        if a > b:
            return gcd(a-b, b)
        else:
            return gcd(a, b-a)
    return a
    
print(gcd(2, 4))