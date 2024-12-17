#!/usr/bin/python3
class Node:
	def __init__(self, data, next_node=None):
		self.__data = data
		self.__next_node = next_node
	@property
	def data(self):
		return self.__data
	@data.setter
	def data(self, value):
		if not isinstance(value, int):
			raise TypeError("data must be an integer")
		else:
			self.__data = value
	@property
	def next_node(self):
		return self.__next_node
	@next_node.setter
	def next_node(self, value):
		if not isinstance(value, Node) and value is not None:
			raise TypeError("next_node must be a Node object")
		else:
			self.__next_node = value
class SinglyLinkedList:
	def __init__(self):
		self.head = None
	def sorted_insert(self, value):
		new = Node(int(value))
		if not self.head:
			self.head = new
		else:
			if self.head.data > value:
				new.next_node = self.head
				self.head = new
			else:
				tmp = self.head
				while (tmp.next_node and tmp.next_node.data < value):
					tmp = tmp.next_node
				new.next_node = tmp.next_node
				tmp.next_node = new
		return self.head

	def __str__(self):
		j = self.head
		while j.next_node:
			print(j.data)
			j = j.next_node
		return str(j.data)


sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)