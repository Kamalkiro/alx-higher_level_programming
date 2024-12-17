#!/usr/bin/python3
from sys import argv

class Queens:
	def __init__(self, position):
		self.position = position

	def moves(self, position, places):
		row, column = self.position
		moves = set()

		for i in range(places):
			moves.add((row, i))  
			moves.add((i, column)) 
		r, c = row, column
		while r >= 0 and c >= 0:
			moves.add((r, c))
			r -= 1
			c -= 1

		r, c = row, column
		while r < places and c >= 0: 
			moves.add((r, c))
			r += 1
			c -= 1

		r, c = row, column
		while r >= 0 and c < places:
			moves.add((r, c))
			r -= 1
			c += 1

		r, c = row, column
		while r < places and c < places:  
			moves.add((r, c))
			r += 1
			c += 1

		return moves

def solve_nqueens(n):
	
	column_set = set()
	diag1_set = set()  
	diag2_set = set()  

	result = []

	def backtrack(row, current_board):
		if row == n:
			result.append(current_board[:])
			return
	
		for col in range(n):
			if col in column_set or (row - col) in diag1_set or (row + col) in diag2_set:
				continue 
			queen = Queens((row, col))
			attacked_positions = queen.moves((row, col),n)

			if all((r, c) not in attacked_positions for r, c in current_board):
				column_set.add(col)
				diag1_set.add(row - col)
				diag2_set.add(row + col)

				current_board.append((row, col))

				backtrack(row + 1, current_board)

				current_board.pop()
				column_set.remove(col)
				diag1_set.remove(row - col)
				diag2_set.remove(row + col)

	backtrack(0, [])
	return result

def print_solutions(solutions):
	for solution in solutions:
		solution = [list(res) for res in solution]
		print(solution)

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

solutions = solve_nqueens(places)
print_solutions(solutions)



	
	
