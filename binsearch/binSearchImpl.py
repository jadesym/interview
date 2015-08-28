class Node:
	def __init__(self, val):
		self.leftChild = None
		self.rightChild = None
		self.data = val

def binary_insert(root, node):
	if root is None:
		root = node
	else:
		if root.data > node.data:
			if root.leftChild is None:
				root.leftChild = node
			else:
				binary_insert(root.leftChild, node)
		else:
			if root.rightChild is None:
				root.rightChild = node
			else:
				binary_insert(root.rightChild, node)

def print_ascending(root):
	if not root:
		return
	print_ascending(root.leftChild)
	print(root.data)
	print_ascending(root.rightChild)

def print_pre_order(root):
	if not root:
		return
	print(root.data)
	print_pre_order(root.leftChild)
	print_pre_order(root.rightChild)

def bin_search(root, val):
	if root.data == val:
		return root
	elif val > root.data:
		if root.rightChild is None:
			return None
		else:
			return bin_search(root.rightChild, val)
	else:
		if root.leftChild is None:
			return None
		else:
			return bin_search(root.leftChild, val)

def insert_array_into_tree(root, valArray):
	for val in valArray:
		binary_insert(root, Node(val))

def exists(root, val):
	if bin_search(root, val):
		return "Exists"
	else:
		return "Does Not Exist"

import random
def randomArray(low, high, numNums):
	array = []
	for num in range(numNums):
		array.append(random.randint(low, high))
	return array

root = Node(3)
numArray = randomArray(1, 1000, 30)
print("Unsorted: ", numArray)
insert_array_into_tree(root, numArray)
print("Ascending Order:")
print_ascending(root)
print("Pre Order:")
print_pre_order(root)
print("Searching for values:")
print("1:" + exists(root, 1))
print("2:" + exists(root, 2))
print("3:" + exists(root, 3))
print("4:" + exists(root, 4))
print("5:" + exists(root, 5))
print("6:" + exists(root, 6))
print("7:" + exists(root, 7))
print("8:" + exists(root, 8))
print("9:" + exists(root, 9))
print("10:" + exists(root, 10))

