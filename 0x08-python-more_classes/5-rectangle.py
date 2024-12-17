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
	def __str__(self):
		if not self.__height or not self.__width:
			return ""
		else:
			return ("#"*self.__width + "\n") * self.__height
	def __repr__(self):
		return (f"Rectangle({self.__width}, {self.__height})")
	def __del__(self):
		print("Bye rectangle...")
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))