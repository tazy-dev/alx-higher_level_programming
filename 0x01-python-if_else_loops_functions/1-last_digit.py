#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
last_d = abs(num) % 10
if num < 0:
    last_d = -last_d
if last_d > 5:
    print(f"Last digit of {num:d} is {last_d:d} and is greater than 5")
elif last_d == 0:
    print(f"Last digit of {num:d} is {last_d:d} and is 0")
else:
    print(f"Last digit of {num:d} is {last_d:d} and is less than 6 and not 0")
