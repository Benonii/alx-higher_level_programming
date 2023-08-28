#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x = 0):
	i = 0
	j = 0
	try:
		while j < x:
			if isinstance(my_list[j], int):
				print("{:d}".format(my_list[j]), end="")
				i += 1
			j += 1

		print("")
		return i
	except TypeError:
		return j
