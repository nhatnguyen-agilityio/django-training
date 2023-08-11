def nested_sum(l):
    total = 0
    for item in l:
        total += sum(item)
    return total

print(nested_sum([[1, 2], [3], [4, 5, 6]]))