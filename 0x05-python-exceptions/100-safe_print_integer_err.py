#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
	try:
		print("{:d}".format(value))
	except Exception as i:
		stderr.write("Exception: {}\n".format(i))
		return (False)
	else:
		return (True)
