#!/usr/bin/python3
def weight_average(my_list=[]):
	result = 0
	divi = 0
	for i in my_list:
		result += i[0] * i[1]
		divi += i[1]
	return result / divi


my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))