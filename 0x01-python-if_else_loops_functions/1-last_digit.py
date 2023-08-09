#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    lastDigit = (number % 10) * -1
    print(f"Last digit of {number * -1} is {lastDigit} and is less than 6 and not 0")

else:
    lastDigit = number % 10
    if (lastDigit > 5):
        str = "and is greater than 5"
    elif (lastDigit == 0):
        str = "and is 0"
    else:
        str = "and is less than 6 and not 0"
    print(f"Last digit of {number} is {lastDigit} " + str)
