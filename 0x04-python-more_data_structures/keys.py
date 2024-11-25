#!/usr/bin/python3
def number_keys(a_dictionary):
	ret = 0
	for i in a_dictionary:
		ret += 1
	return ret


a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))