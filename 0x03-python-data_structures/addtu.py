#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
	x, y = tuple_a
	if len(tuple_b) == 2:
		a, b = tuple_b
	elif len(tuple_b) == 1:
		a = tuple_b[0]
		b = 0
	else:
		a, b = 0, 0
	new_tuple = (a + x, b + y)
	return new_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))