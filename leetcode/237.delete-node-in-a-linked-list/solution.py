# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            pass
        elif node.next is None:
            node = None
        else:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
            else:
                node.next = node.next.next