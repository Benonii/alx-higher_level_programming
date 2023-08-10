#!/usr/bin/python3
import hidden_4 as hidden
if __name__ == "__main__":
    names = dir(hidden)
    for i in range(0, len(names)):
        if names[i][0] == '_':
            continue
        else:
            print(f"{names[i]}")
