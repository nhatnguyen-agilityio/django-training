from random import randint

def random_birthday(n):
    i = 0
    list_birthday = []
    while i < n:
        list_birthday.append(randint(1, 365))
        i += 1
    return list_birthday

def has_duplicates(l):
    for item in l:
        new_list = l[:]
        new_list.remove(item)
        if item in new_list:
            return True
    return False

students = 23
simulation = 1000
count = 0
for i in range(simulation):
    list_birthday = random_birthday(students)
    if has_duplicates(list_birthday):
        count += 1
print(count)
