#!/usr/bin/python3
if __name__ == '__main__':
	from sys import argv
	from calculator_1 import add, sub, mul, div
	if len(argv) != 4:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>")
		exit(1)
	elif argv[2] not in ['+', '-', '*', '/']:
		print("Unknown operator. Available operators: +, -, * and /")
		exit(1)
	else:
		a, b = int(argv[1]), int(argv[3])
		if argv[2] == '+':
			print(f"{a} {argv[2]} {b} = {add(a, b)}")
		elif argv[2] == '-':
			print(f"{a} {argv[2]} {b} = {sub(a, b)}")
		elif argv[2] == '*':
			print(f"{a} {argv[2]} {b} = {mul(a, b)}")
		elif argv[2] == '/':
			print(f"{a} {argv[2]} {b} = {div(a, b)}")