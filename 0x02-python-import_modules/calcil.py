#!/usr/bin/python3
if __name__ == '__main__':
	from sys import argv
	i = 1
	print(len(argv) - 1, "arguments" + '.' if len(argv) == 1 else "arguments" + ':')
	while i < len(argv):
		print(i, ":", argv[i])
		i += 1