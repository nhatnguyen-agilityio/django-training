def eval_loop():
    result = 0
    while True:
        value = input("Input value: ")
        if value == "done":
            return result
        print(eval(value))
        result = value

print(eval_loop())