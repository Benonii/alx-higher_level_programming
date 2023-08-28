#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for element in my_list:
                if i < x:
                        print(element, end="")
                        i += 1
                else:
                       continue
        print("")
        return i
    except Exception:
        print("An Error Occured")
