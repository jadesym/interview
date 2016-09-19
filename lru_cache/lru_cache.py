"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1. set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""

class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity):
        # key -> (value, node)
        self.lookup = {}
        # oldest
        self.head = None
        # newest
        self.tail = None
        self.capacity = capacity
        self.numElem = 0
    # removes a node from the linkedlist
    def remove_node(self, node):
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            newHead = self.head.next
            newHead.prev = None
            self.head = newHead
        elif node is self.tail:
            newTail = self.tail.prev
            newTail.next = None
            self.tail = newTail
        else:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
        node.prev = None
        node.next = None
    # Appends a node to the end of the linkedlist
    def append_node(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            oldTail = self.tail
            oldTail.next = node
            node.prev = oldTail
            self.tail = node
    # Gets a value for a specific key
    def get(self, key):
        if key not in self.lookup: return -1
        value, node = self.lookup[key]
        self.remove_node(node)
        self.append_node(node)
        return value
    # Sets a value for a specific key
    def set(self, key, value):
        # If currently does not exist
        if key in self.lookup:
            _, node = self.lookup[key]
            self.remove_node(node)
            del self.lookup[key]
        # If reaches the current capacity
        elif self.numElem == self.capacity:
            headKey = self.head.key
            self.remove_node(self.head)
            del self.lookup[headKey]
        # If doesnt exist and has not reached the capacity
        else:
            self.numElem += 1
        newNode = Node(key)
        self.lookup[key] = (value, newNode)
        self.append_node(newNode)
    def getVal(self, node):
        return self.lookup[node.key][0]
    # Displays for debugging purposes
    def display(self):
        print("Dictionary: " + str(self.lookup))
        if self.head is not None: print("Head: " + str(self.getVal(self.head)))
        if self.tail is not None: print("Tail: " + str(self.getVal(self.tail)))
        print("Num Elements: " + str(self.numElem) + "/" + str(self.capacity))
        print("LinkedList:")
        curNode = self.head
        if curNode is None: print("Empty")
        while curNode is not None:
            if curNode.prev is not None: print(self.getVal(curNode.prev), "", end=" ")
            else: print("_", "", end=" ")
            print(self.getVal(curNode), "", end=" ")
            if curNode.next is not None: print(self.getVal(curNode.next))
            else: print("_")
            curNode = curNode.next
        print("----------------------")
