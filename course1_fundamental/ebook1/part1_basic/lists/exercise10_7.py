def has_duplicates(l):
    for item in l:
        new_list = l[:]
        new_list.remove(item)
        if item in new_list:
            return True
    return False

print(has_duplicates(["abc", "has", "post", "hsas"]))
print(has_duplicates(["abc", "has", "post", "has"]))
