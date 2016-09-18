from collections import deque

class Node:
    def __init__(self, val, left = None, right = None, mid = None):
        self.val = val
        self.left = left
        self.right = right
        self.mid = mid

class SearchTreeMod:
    def __init__(self, values, root = None):
        self.root = root
        for value in values:
            self.insert(value)
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
    def delete_multiple(self, values):
        for value in values:
            self.delete(value)
    # Deletes a Node from the tree by its value
    def delete(self, value):
        if self.root is None:
            return
        else:
            self.delete_recurse(self.root, value, None, None)
    # Deletes a Node from a subtree by its value
    def delete_recurse(self, node, value, parent, parentleftOrRight):
        if node.val == value:
            if node.mid is not None: self.delete_lowest_mid(node)
            else: self.replace(node, parent, parentleftOrRight)
        elif node.val > value:
            if node.left is not None: self.delete_recurse(node.left, value, node, True)
        else:
            if node.right is not None: self.delete_recurse(node.right, value, node, False)
    # Deletes the lowest mid node that exists
    def delete_lowest_mid(self, node):
        if node.mid.mid is None: node.mid = None
        else: self.delete_lowest_mid(node.mid)
    # Finds the replacement node
    def replace(self, node, parent, parentLeftOrRight):
        left = self.find_replacement(True, node.left, parent)
        if left is not None:
            if parent is not None:
                if parentLeftOrRight: parent.left = left
                else: parent.right = left
            else: self.root = left
            left.right = node.right
            return
        right = self.find_replacement(False, node.right, parent)
        if right is not None:
            if parent is not None:
                if parentLeftOrRight: parent.left = right
                else: parent.right = right
            else: self.root = right
            right.left = node.left
        else:
            if parent is None:
                self.root = None
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
            if prevNode is not None: prevNode.right = None
        else:
            while curNode.left is not None:
                prevNode = curNode
                curNode = curNode.left
            if prevNode is not None: prevNode.left = None
        return curNode
    # Printing for Debugging Purposes
    def display(self):
        queue = deque([(0, self.root)])
        prevLevel = -1
        beginning = True
        print("Starting SMT")
        while len(queue) > 0:
            level, node = queue.popleft()
            if node is None: continue
            if level > prevLevel:
                if not beginning:
                    print()
                else:
                    beginning = False
                print(str(level) + ":", end="")
                prevLevel = level
            print(str(node.val), ":", end = "")
            children = []
            if node.left is not None:
                queue.append((level + 1, node.left))
                children.append(node.left.val)
            else:
                children.append("_")
            if node.mid is not None:
                queue.append((level + 1, node.mid))
                children.append(node.mid.val)
            else:
                children.append("_")
            if node.right is not None:
                queue.append((level + 1, node.right))
                children.append(node.right.val)
            else:
                children.append("_")
            print(str(children) + " ", " ", end = "")
        print("\nDone...")
