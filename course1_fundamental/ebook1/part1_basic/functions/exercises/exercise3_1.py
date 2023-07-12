def right_justify(s):
    text = (70 - (len(s))) * " "
    print(text + s)

right_justify("monty")