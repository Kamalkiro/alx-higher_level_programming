#!/usr/bin/env python3
def no_c(string):
	newstr = ''
	for i in string:
		if i not in ['c', 'C']:
			newstr += i
	return newstr


print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))