#!/usr/bin/python3
from sys import argv
class Queens:
	def __init__(self, position):
		self.position = position
	def moves(self, position, places):
		row, column = self.position
		moves = []
		for i in range(places):
			li = row, i
			moves.append(li)
		for j in range(places):
			li = j, column
			moves.append(li)
		r, c = row, column
		while r >= 0 and c >= 0:
			if r == 0 or c == 0:
				break
			r -= 1
			c -= 1
			li = r, c
			moves.append(li)
		r, c = row, column
		while r < places and c >= 0:
			if r + 1 == places or c == 0:
				break
			r += 1
			c -= 1
			li = r, c
			moves.append(li)
		r, c = row, column
		while c < places and r >= 0:
			if r == 0 or c + 1 == places:
				break
			r -= 1
			c += 1
			li = r, c
			moves.append(li)
		r, c = row, column
		while c < places and r < places:
			if r + 1 == places or c + 1 == places:
				break
			r += 1
			c += 1
			li = r, c
			moves.append(li)
		return set(moves)

def check(j, i, n):
	alen = []
	x = j.copy()
	q = Queens(i)
	x += q.moves(i, n)
	z = i[0] + 1
	for d in range(n):
		jiji = z, d
		alen.append(jiji)
	for jij in alen:
		if jij not in x:
			return True
	return False
def comparequeens(mov, n):
	res = []
	j = []
	for i in mov:
		if i not in j and check(j, i, n):
			q = Queens(i)
			j += q.moves(i, n)
			res.append(i)
	return res
		
	

def passpositions(movelist, places):
	it = 0
	result = []
	while it < places * places:
		it += 1
		result = comparequeens(movelist, places)
		movelist = movelist[1:]
		if (len(result) == places):
			print(result)
		
def getpositions(places):
	firstop = []
	for i in range(places):
		for j in range(places):
			li = i, j
			firstop.append(li)
	return firstop
if len(argv) > 2:
	print("Usage: nqueens N")
	exit(1)
places = int(argv[1])
if not isinstance(places, int):
	print("N must be a number")
	exit(1)
if places < 4:
	print("N must be at least 4")
	exit(1)
firstop = getpositions(places)
moves = passpositions(firstop, places)

	



	
	
