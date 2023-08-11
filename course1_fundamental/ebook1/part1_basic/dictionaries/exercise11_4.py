def has_duplicates(l):
    new_dict = {}
    for item in l:
        if item in new_dict:
            return True
        else:
            new_dict[item] = 0
    return False

print(has_duplicates(["abc", "has", "post", "hsas"]))
print(has_duplicates(["abc", "has", "post", "has"]))