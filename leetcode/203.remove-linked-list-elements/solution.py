# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None: return None
        newHead = head
        prev = None
        cur = head
        while cur is not None:
            if newHead.val == val:
                newHead = newHead.next
            if prev is None:
                prev = cur
            else:
                if cur.val == val:
                    prev.next = cur.next
                else:
                    prev = prev.next
            cur = cur.next
        return newHead
                