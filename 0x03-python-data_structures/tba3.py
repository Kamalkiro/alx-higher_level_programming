#!/usr/bin/python3
def print_list_integer(list=[]):
	for i in list:
		print("{:d}".format(i))

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)