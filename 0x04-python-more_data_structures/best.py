#!/usr/bin/python3
def best_score(a_dictionary):
	if not a_dictionary:
		return 'None'
	else:
		i = 0
		for x, j in a_dictionary.items():
			if i < j:
				i = j
				best_key = x
	return best_key

a_dictionary = {'John': 20, 'Bob': 17, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))