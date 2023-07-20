cache = {}
def ack(n ,m):
    if n == 0:
        return n + 1
    if m == 0:
        return ack(n-1, 1)
    if (n, m) in cache:
        return cache[n, m]
    else:
        cache[n, m] = ack(n-1, ack(n, m-1))
        return cache[n, m]
    
print(ack(5,7))