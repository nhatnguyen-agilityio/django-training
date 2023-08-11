def most_frequent(s):
    hist = make_histogram(s)
    t = []
    for x, freq in hist.items():
        t.append((freq, x))
    t.sort(reverse=True)
    res = []
    for freq, x in t:
        res.append(x)
    print(res)
    return res

def make_histogram(s):
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist

letter_seq = most_frequent("Sorts the letters in s in reverse order of frequency")
print(letter_seq)