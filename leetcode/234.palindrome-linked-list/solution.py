# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return True
        if head.next is None: return True
        count = 0
        cur = head
        while cur.next is not None:
            cur = cur.next
            count += 1
        second = head
        prevSecond = None
        newCount = 0
        while newCount < (count) // 2:
            prevSecond = second
            second = second.next
            newCount += 1
        cur = second
        first = True
        while cur is not None:
            past = prevSecond
            prevSecond = cur
            cur = cur.next
            prevSecond.next = past
        rightNow = head
        curCount = 0
        while curCount < (count // 2) + 1:
            if rightNow.val != prevSecond.val: return False
            rightNow = rightNow.next
            prevSecond = prevSecond.next
            curCount += 1
        return True
            
        
            
        
        