def cumsum(l):
    cumulative_sum = []
    if len(l) <= 1:
        return l
    else:
        privious_item = 0
        for index, item in enumerate(l):
            if index == 0:
                privious_item = item
                cumulative_sum.append(item)
            else:
                sum_items = item + privious_item
                cumulative_sum.append(sum_items)
                privious_item = sum_items
        return cumulative_sum

print(cumsum([1, 2, 3]))
