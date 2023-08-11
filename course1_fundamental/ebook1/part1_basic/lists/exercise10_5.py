def is_sorted(l):
    new_list = sorted(l)
    if l == new_list:
        return True
    return False

print(is_sorted([1, 1, 2]))
print(is_sorted([1, 10, 2]))