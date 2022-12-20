# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rootResult = None
        result = None
        carry = 0
        firstNode = l1
        secondNode = l2
        while firstNode is not None or secondNode is not None:
            first = firstNode.val if firstNode is not None else 0
            second = secondNode.val if secondNode is not None else 0

            remainder = (first + second + carry) % 10

            if first + second + carry >= 10:
                carry = 1
            else:
                carry = 0
            
            newNode = ListNode(remainder)

            if result is None:
                result = newNode
            else:
                result.next = newNode
                result = newNode
            if  rootResult is None:
                rootResult = newNode
            
            if firstNode is not None:
                firstNode = firstNode.next
            if secondNode is not None:
                secondNode = secondNode.next

        if carry == 1:
            result.next = ListNode(1)

        return rootResult
        