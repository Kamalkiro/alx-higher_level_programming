#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
	if idx < 0 or idx > len(my_list) - 1:
		return my_list
	else:
		new_list = []
		i = 0
		while i < len(my_list):
			new_list.append(my_list[i])
			i += 1
		new_list[idx] = element
		return new_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)