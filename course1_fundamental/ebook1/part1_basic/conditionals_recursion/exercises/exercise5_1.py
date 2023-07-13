import time

time_now = int(time.time())
total_days = time_now // 3600 // 24

time_remaining = time_now - (total_days * 24 * 3600)

hours = time_remaining // 3600

minutes = (time_remaining - (hours * 3600)) // 60

seconds = time_remaining - (hours * 3600) - (minutes *60)

print("Time now: {0}:{1}:{2} on {3} days since epoch".format(hours, minutes, seconds, total_days))

