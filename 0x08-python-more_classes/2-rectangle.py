#!/usr/bin/python3
class Rectangle:
	def __init__(self, width=0, height=0):
		self.width = width
		self.height = height
	@property
	def width(self):
		return self.__width
	@property
	def height(self):
		return self.__height
	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		elif value < 0:
			raise ValueError("width must be >= 0")
		else:
			self.__width = value
	@height.setter
	def height(self, value):
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		elif value < 0:
			raise ValueError("height must be >= 0")
		else:
			self.__height = value
	def area(self):
		return self.__height * self.__width
	def perimeter(self):
		if not self.__height or not self.__width:
			return 0
		else:
			return self.__height * 2 + self.__width *2

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))