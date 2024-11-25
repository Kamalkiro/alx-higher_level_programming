#!/usr/bin/python3
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary
def complex_delete(a_dictionary, value):
	i = 0
	for v in a_dictionary.values():
		if v == value:
			i += 1
	while i > 0:
		for k, v in a_dictionary.items():
			if v == value:
				del a_dictionary[k]
				break
		i -= 1
	return a_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
