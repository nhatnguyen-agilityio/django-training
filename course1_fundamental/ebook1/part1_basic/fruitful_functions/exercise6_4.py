def is_power(a, b):
    if a == 0 or b == 0:
        return "a and b must be different from 0"
    elif a % b == 0:
        return True
    else:
        return False
    
print(is_power(0, 0))
print(is_power(10, 15))
print(is_power(10, 5))