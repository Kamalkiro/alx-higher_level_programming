#!/usr/bin/python3
def divisible_by_2(my_list = []):
	list_result = my_list.copy()
	x = 0
	for i in my_list:
		if i % 2 == 0:
			list_result[x] = True
		else:
			list_result[x] = False
		x += 1
	return list_result

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1