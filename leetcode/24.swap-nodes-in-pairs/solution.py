# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        elif head.next is None: return head
        newHead = head.next
        cur = head
        prev = None
        while cur is not None:
            if cur.next is None: break
            nextNextNode = cur.next.next
            nextNode = cur.next
            if prev is not None:
                prev.next = cur.next
            cur.next, nextNode.next = nextNextNode, cur
            prev = cur
            cur = nextNextNode
        return newHead        