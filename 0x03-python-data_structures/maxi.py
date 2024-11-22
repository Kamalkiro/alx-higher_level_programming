#!/usr/bin/python3
def max_integer(my_list=[]):
	i = my_list[0]
	for x in my_list:
		if x > i:
			i = x
	return i

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))