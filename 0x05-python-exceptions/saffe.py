#!/usr/bin/python3
def safe_print_integer_err(value):
	from sys import exc_info, stderr
	try:
		print("{:d}".format(value))
		return True
	except (ValueError, TypeError) as e:
		print("Exception: {}".format(exc_info()[1]), file=stderr)
		return False

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
