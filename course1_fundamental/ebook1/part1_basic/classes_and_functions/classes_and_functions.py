class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

def print_time(time):
    print("{0}:{1}:{2}".format(time.hour, time.minute, time.second))

def is_after(t1, t2):
    if t1.hour > t2.hour:
        return True
    elif t1.hour == t2.hour:
        if t1.minute > t2.minute:
            return True
        elif t1.minute == t2.minute:
            if t1.second >= t2.second:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second = sum.second % 60

    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute = sum.minute % 60

    return sum

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def add_time_new_version(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    time1 = time_to_int(t1)
    time2 = time_to_int(t2)
    return int_to_time(time1+time2)
    

time = Time()
time.hour = 11
time.minute = 59
time.second = 20

time2 = Time()
time2.hour = 1
time2.minute = 52
time2.second = 29

print_time(add_time_new_version(time, time2))

# print(is_after(time, time2))
# print_time(time)
# print_time(time2)