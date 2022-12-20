from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        curNode = head
        middleNode = curNode
        while curNode is not None:
            count += 1
            if count % 2 == 0:
                middleNode = middleNode.next
            curNode = curNode.next
        return middleNode
            