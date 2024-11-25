#!/usr/bin/python3
def common_elements(set_1, set_2):
	set_3 = []
	for i in set_1:
		for x in set_2:
			if x == i:
				set_3.append(x)
	
	return set_3

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))