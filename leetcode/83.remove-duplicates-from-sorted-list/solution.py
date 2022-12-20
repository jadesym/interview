# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        curNode = head
        orig = head
        while curNode is not None:
            if curNode.next is None: break
            if curNode.next.val == curNode.val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return orig