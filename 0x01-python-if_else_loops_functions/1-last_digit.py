#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
lastCpy = str(last)
if number < 0:
    lastCpy = "-" + lastCpy
lastCpy = int(lastCpy)
print(f"Last digit of {number:d} is {lastCpy:d}", end=" ")
if lastCpy > 5:
    print("and is greater than 5")
elif lastCpy == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
