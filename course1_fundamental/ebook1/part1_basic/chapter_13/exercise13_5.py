import random

def histogram(t):
    result = dict()
    i = 0
    while i < len(t):
        a = random.choice(t)
        if a not in result:
            result[a] = 1
        else:
            result[a] += 1
        i += 1
    return result

t = ['a', 'a', 'b']
print(histogram(t))