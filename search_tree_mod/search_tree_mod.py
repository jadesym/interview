from collections import deque

class Node:
    def __init__(self, val, left = None, right = None, mid = None):
        self.val = val
        self.left = left
        self.right = right
        self.mid = mid

class SearchTreeMod:
    def __init__(self, root = None):
        self.root = root
    # Inserts a new Node into the tree
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recurse(self.root, value)
    # Recursive function for inserting a node into a subtree
    def insert_recurse(self, node, value):
        if node.val == value:
            if node.mid is None:
                node.mid = Node(value)
            else:
                self.insert_recurse(node.mid, value)
        elif node.val > value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recurse(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recurse(node.right, value)
    # Deletes a Node from the tree by its value
    def delete(self, value):
        if self.root is None:
            return
        else:
            self.delete_recurse(self.root, value, None)
    # Deletes a Node from a subtree by its value
    def delete_recurse(self, node, value):
        if node.val == value:
            if node.mid is not None:
                self.delete_lowest_mid(node)
            else:
                # replace Call
        elif node.val > value:
            if node.left is not None:
                self.delete_recurse(node.left, value, parent)
        else:
            if node.right is not None:
                self.delete_recurse(node.right, value, parent)
    # Deletes the lowest mid node that exists
    def delete_lowest_mid(self, node):
        if node.mid.mid is None:
            node.mid is None
        else:
            self.delete_lowest_mid(node.mid)
    # Finds the replacement node
    def replace(self, node, parent):
        left = self.find_replacement(True, node.left, parent)
        if left is not None:
            node.val = left.val
            return
        right = self.find_replacement(False, node.right, parent)
        if right is not None: node.val = right.val
        else:
            if parent is None:
                self.root is None:
            else:
                if parent.left is node: parent.left = None
                elif parent.right is node: parent.right = None
    # Replaces
    def find_replacement(self, leftOrRight, node, parent):
        if node is None: return None
        curNode = node
        prevNode = parent
        if leftOrRight:
            while curNode.right is not None:
                prevNode = curNode
                curNode = curNode.right
            prevNode.right = None
        else:
            while curNode.left is not None:
                prevNode = curNode
                curNode = curNode.left
            prevNode.left = None
        return curNode
    # Printing for Debugging Purposes
    def display(self):
        queue = deque([(0, self.root)])
        prevLevel = 0
        while len(queue) > 0:
            level, node = level, queue.popleft()
            if level > prevLevel:
                print()
            print(node.val, end = "")
            if node.left is not None: queue.append(node.left)
            if node.mid is not None: queue.append(node.mid)
            if node.right is not None: queue.append(node.right)
