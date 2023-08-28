#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    try:
        i = 0
        result = []
        while i < list_length:
            try:
                if my_list_2[i] == 0:
                    raise ZeroDivisionError
                    continue
                elif isinstance(my_list_1[i], int) and\
                isinstance(my_list_2[i], int):
                    result.append(my_list_1[i] / my_list_2[i])
                else:
                    raise TypeError

            except TypeError:
                print("wrong type")
                result.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            i += 1
    except IndexError:
        print("out of range")
        result.append(0)
    finally:
        return result
