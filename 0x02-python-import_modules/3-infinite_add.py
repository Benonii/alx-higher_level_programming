#!/usr/bin/python3
import sys
if __name__ == "__main__":
    av = sys.argv
    ac = len(av)
    result = 0
    for i in range(1, ac):
        result += int(av[i])
    print(result)
