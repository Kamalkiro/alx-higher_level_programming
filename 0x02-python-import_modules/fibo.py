#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    i = 1
    x = 0
    while (i < len(argv)):
        x += int(argv[i])
        i += 1
    print(x)