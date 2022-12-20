# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None: return None
        first = headA
        second = headB
        while first is not None and second is not None and first is not second:
            first = first.next
            second = second.next
            if first == second: return first
            if first is None:
                first = headB
            if second is None:
                second = headA
        return first