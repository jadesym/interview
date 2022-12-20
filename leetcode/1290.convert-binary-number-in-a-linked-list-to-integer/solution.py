# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        curNode = head
        curNum = 0
        while curNode is not None:
            curNum *= 2
            curNum += curNode.val
            
            curNode = curNode.next
        return curNum