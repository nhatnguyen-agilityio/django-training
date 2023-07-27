class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """


def mul_time(time, n):
    time1 = Time()
    seconds = time_to_int(time) * n
    time1 = int_to_time(seconds)
    return time1


def print_time(time):
    if time.hour > 24:
        print(
            "%.2d days %.2d:%.2d:%.2d"
            % (time.hour / 24, time.hour % 24, time.minute, time.second)
        )
    else:
        print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))


def time_to_int(time):
    minute = time.minute + (time.hour * 60)
    second = time.second + (minute * 60)
    return second


def int_to_time(second):
    time = Time()
    minute, time.second = divmod(second, 60)
    time.hour, time.minute = divmod(minute, 60)
    return time


time = Time()
time.hour = 6
time.second = 43
time.minute = 45
done = mul_time(time, 4)
print_time(done)
