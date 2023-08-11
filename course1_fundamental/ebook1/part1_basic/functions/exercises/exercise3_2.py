def do_twice(f, value):
    f(value)
    f(value)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

def print_spam(value):
    print(value)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_four(print_spam, 'spam')

# do_twice(print_twice, 'string')