a = {"a": 1, "b": 2, "c": 1, "d": 4, "e": 1}

def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

print(invert_dict(a))