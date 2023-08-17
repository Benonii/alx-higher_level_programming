#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == 0:
        return 0
    else:
        sum = 0
        div = 0
        for i in range (len(my_list)):
            sum += map(lambda a, b: a * b, my_list[i][0], my_list[i][1])
        for i in range (len(my_list)):
            div += my_list[i][1]
        average = sum / div
        return average
