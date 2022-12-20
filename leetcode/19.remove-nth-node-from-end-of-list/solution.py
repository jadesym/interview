# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None: return head
        if head.next is None and n == 1: return None
        count = 0
        prev = None
        cur = head
        while count < n - 1:
            cur = cur.next
            count += 1
        if cur.next is None: return head.next
        while cur.next is not None:
            if prev is None: prev = head
            else: prev = prev.next
            cur = cur.next
        prev.next = prev.next.next
        return head
        
        
            