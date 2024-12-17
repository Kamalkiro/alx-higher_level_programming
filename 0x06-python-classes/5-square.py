#!/usr/bin/python3
class Square:
	def __init__(self, size=0):
		self.__size = size
	def area(self):
		ret = self.__size * self.__size
		return ret
	@property
	def size(self):
		return self.__size
	@size.setter
	def size(self, value):
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = value
	def my_print(self):
		if not self.size:
			print()
		else:
			for i in range(self.size):
				for j in range(self.size):
					print('#', end = '')
				print()
my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")