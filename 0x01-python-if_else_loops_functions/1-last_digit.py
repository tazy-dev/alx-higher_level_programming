#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digi = abs(number) % 10
if number < 0:
    digi = -digi
if digi > 5:
    print(f"Last digit of {number:d} is {digi:d} and is greater than 5")
elif digi == 0:
    print(f"Last digit of {number:d} is {digi:d} and is 0")
else:
    print(f"Last digit of {number:d} is {digi:d} and is less than 6 and not 0")
