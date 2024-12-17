#!/usr/bin/python3
class Rectangle:
	number_of_instances = 0
	print_symbol = '#'
	def __init__(self, width=0, height=0):
		self.width = width
		self.height = height
		Rectangle.number_of_instances += 1
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
			return (print_symbol*self.__width + "\n") * self.__height
	def __repr__(self):
		return (f"Rectangle({self.__width}, {self.__height})")
	def __del__(self):
		Rectangle.number_of_instances -= 1
		print("Bye rectangle...")
my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))