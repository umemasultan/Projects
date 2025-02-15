
# counttimer//
import time

mytime=int(input("enter the time in seconds:"))


for x in range(mytime, 0, -1):
    seconds= x % 60
    minutes = int(x/60)% 60
    hours= int(x/3600)
    print(f"{hours:02}:{minutes:02},{seconds:02}")
    time.sleep(1)

print("TIME'S UP")

import time
def timer(seconds):
    for x in range(seconds, 0, -1):
        print("time left", i, "seconds")
        time.sleep(2)
try:
    user_seconds=int(input("enter the time in seconds:"))
    timer(user_seconds)
except:
    print("enter a valid integer for countdown time")

                     