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
			return (str(self.print_symbol)*self.__width + "\n") * self.__height
	def __repr__(self):
		return (f"Rectangle({self.__width}, {self.__height})")
	def __del__(self):
		Rectangle.number_of_instances -= 1
		print("Bye rectangle...")
	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		if not isinstance(rect_1, Rectangle) or not isinstance(rect_2, Rectangle):
			raise TypeError("rect_1 and rect_2 must be an instance of Rectangle")
		elif (rect_1.area() >= rect_2.area()):
			return rect_1
		else :
			return rect_2
my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")