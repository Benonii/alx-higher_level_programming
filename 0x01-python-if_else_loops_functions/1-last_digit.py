#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    print((number % 10) * -1)

else:
    print(number % 10)
