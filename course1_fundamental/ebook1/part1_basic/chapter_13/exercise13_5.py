import random

def histogram(t):
    result = dict()
    for i in range(len(t)):
        a = random.choice(t)
        if a not in result:
            result[a] = 1
        else:
            result[a] += 1
    return result


if __name__ == "__main__":
    t = ['a', 'a', 'b']
    print(histogram(t))
