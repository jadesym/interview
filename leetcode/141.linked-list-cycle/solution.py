# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        slow = head
        fast = head
        while fast is not None:
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                return False
            if slow is fast:
                return True
        return False
                
