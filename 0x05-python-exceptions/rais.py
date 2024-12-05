#!/usr/bin/python3
def raise_exception():
	raise TypeError

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
def raise_exception_msg(message=""):
		raise NameError(message)
try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)