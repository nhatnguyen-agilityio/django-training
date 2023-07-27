class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
time = Time()
time.hour = 11
time.minute = 35
time.second = 59
end_time = time.increment(500)
# end_time.print_time()
print(time.is_after(end_time))
# time.print_time()
# print(time.time_to_int())