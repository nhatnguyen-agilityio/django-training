def print_plus():
    print("+")

def print_row_plus():
    print("+ - - - -", end=" ")

def print_post():
    print("|        ", end=" ")

def print_dash():
    print("|")

def print_two(f):
    f()
    f()

def print_four(f):
    print_two(f)
    print_two(f)

def print_plus_line():
    print_two(print_row_plus)
    print_plus()

def print_dash_line():
    print_two(print_post)
    print_dash()

def print_rows(f):
    print_plus_line()
    print_four(f)

def print_grid():
    print_rows(print_dash_line)
    print_rows(print_dash_line)
    print_plus_line()

print_grid()