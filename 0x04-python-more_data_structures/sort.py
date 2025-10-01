#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
	idict = list(a_dictionary.keys())
	idict.sort()
	for i in idict:
		print (i, " : ", a_dictionary.get(i))

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
