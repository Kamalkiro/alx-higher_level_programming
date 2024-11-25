#!/usr/bin/python3
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary
def multiply_by_2(a_dictionary):
	jiji = {}
	for i in a_dictionary:
		jiji[i] = a_dictionary.get(i) * 2
	return jiji

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)