#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("0{0}".format(i), end=", ")
    else:
        if i == 99:
            end = "\n"
        else:
            end = ", "
        print("{0}".format(i), end=end)
