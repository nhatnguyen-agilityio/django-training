def chop(l):
    del l[0]
    del l[-1]

t = [1, 2, 3, 4]
chop(t)
print(t)