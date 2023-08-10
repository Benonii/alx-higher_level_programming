#!/usr/bin/python3
import sys
if __name__ == "__main__":
    av = sys.argv
    ac = len(av)
    if ac == 1:
        print("0 arguments.")
    else:
        if ac == 2:
            print("1 argument:")
            print(f"1: {av[1]}")
        else:
            print(f"{ac - 1} arguments:")
            for i in range(1, ac):
                print(f"{i} : {av[i]}")
