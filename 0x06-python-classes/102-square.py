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
	def __eq__(self, other):
		return self.area() == other.area()
	def __ne__(self, other):
		return self.area() != other.area()
	def __lt__(self, other):
		return self.area() < other.area()
	def __le__(self, other):
		return self.area() <= other.area()
	def __gt__(self, other):
		return self.area() > other.area()
	def __ge__(self, other):
		return self.area() >= other.area()

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")