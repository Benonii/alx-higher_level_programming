#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if i >= j:
            continue
        else:
            if i == 8 and j == 9:
                end = "\n"
            else:
                end = ", "
            print("{0}{1}".format(i, j), end=end)
