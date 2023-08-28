#!/usr/bin/python3

import sys

def safe_function(fct, *args):
	try:
		return(fct(*args))
	except:
		sys.perror("exception: ")
