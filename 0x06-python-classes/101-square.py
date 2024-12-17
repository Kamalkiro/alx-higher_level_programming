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
	def __str__(self):
		ret = ""
		if not self.__size:
			print()
		elif not self.__position:
			for i in range(self.size):
				for j in range(self.size):
					ret += '#'
				ret += '\n'
		else:
			for i in range(self.__size):
				for n in range(self.__position[0]):
						ret += ' '
				for j in range(self.__size):
					ret += '#'
				ret += "\n"
		return str(ret[:-1])

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)