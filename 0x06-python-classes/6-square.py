#!/usr/bin/python3
class Square:
	def __init__(self, size=0, position=(0,0)):
		self.__size = size
		self.__position = position
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
	@property
	def position(self):
		return self.__position
	@position.setter
	def position(self, value):
		if not isinstance(value, tuple) or not len(value) == 2 or not value[0] >= 0 or not value[1] >=0:
			raise TypeError("position must be a tuple of 2 positive integers")
		else:
			self.__position = value
	def my_print(self):
		if not self.__size:
			print()
		elif not self.__position:
			for i in range(self.size):
				for j in range(self.size):
					print('#', end = '')
				print()
		else:
			for i in range(self.__size):
				for n in range(self.__position[0]):
						print(' ', end = '')
				for j in range(self.__size):
					print('#', end = '')
				print()
my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")