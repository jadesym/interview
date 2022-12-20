class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        head = Node(1)
        curNode = head
        for i in range(1, n):
            newNode = Node(i + 1)
            curNode.next = newNode
            curNode = newNode
        curNode.next = head

        iterationNode = head
        prevNode = curNode

        while iterationNode.val != prevNode.val:
            for i in range(k-1):
                prevNode = iterationNode
                iterationNode = iterationNode.next
            prevNode.next = iterationNode.next
            iterationNode = iterationNode.next
        return iterationNode.val
            
            