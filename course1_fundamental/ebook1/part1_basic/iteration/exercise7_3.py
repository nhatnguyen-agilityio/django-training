import math

def factorial(k):
  if k == 0:
    return 1
  else:
    a = factorial(k-1)
    result = k * a
    return result

def estimate_pi():
  k = 0
  total = 0
  a = 2*math.sqrt(2)/9801
  while True:
    b = factorial(4*k) * (1103 + 26390*k)
    d = factorial(k)**4*396**(4*k)
    term = a* (b/d)
    total += term

    if abs(term) < 1e-15:
      break
    k += 1

  return 1/total

print(estimate_pi())