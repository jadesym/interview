# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        previousNode = None
        curNode = head
        while curNode is not None:
            nextNode = curNode.next
            curNode.next = previousNode
            previousNode = curNode
            curNode = nextNode
        return previousNode