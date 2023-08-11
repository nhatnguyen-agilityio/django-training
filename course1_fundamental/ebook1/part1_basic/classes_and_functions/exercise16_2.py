from datetime import datetime

time = datetime.now()
print(time)
print(time.strftime("%A"))
birth_day = "10/27/1999"
bday = datetime.strptime(birth_day, "%m/%d/%Y")
print(bday)
next_bday = bday.replace(year=time.year)
print(next_bday)

until_next_bday = next_bday - time
print(until_next_bday)

print("For people born on these dates:")
bday1 = datetime(day=11, month=5, year=1967)
bday2 = datetime(day=11, month=10, year=2003)
print(bday1)
print(bday2)

print("Double Day is")
d1 = min(bday1, bday2)
print(d1)
d2 = max(bday1, bday2)
print(d2)
dd = d2 + (d2 - d1)
print(dd)
