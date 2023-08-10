#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    av = sys.argv
    ac = len(av)
    result = 0
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, operator, b = int(av[1]), av[2], int(av[3])
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{a} {operator} {b} = {result}")
