def input_values():
    a = input("a=")
    b = input("b=")
    c = input("c=")
    is_triangle(int(a), int(b), int(c))

def is_triangle(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        print("No")
    else:
        print("Yes")

input_values()