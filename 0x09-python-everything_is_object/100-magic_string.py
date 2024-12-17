#!/usr/bin/python3
def magic_string():
	magic_string.i = getattr(magic_string, 'i', 0) +1
	return ("Best School, " * (magic_string.i - 1) + "Best School")

for i in range(10):
    print(magic_string())