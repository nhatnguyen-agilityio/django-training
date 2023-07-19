def middle(l):
    new_list = l[:]
    del new_list[0]
    del new_list[-1]
    return new_list

l = [1, 2, 3, 4]
print(middle(l))
print(l)