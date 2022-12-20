# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l2 is None: return l1
        elif l1 is None: return l2
        elif l1 is None and l2 is None: return None
        curL1 = l1
        curL2 = l2
        
        root = None
        if curL1.val < curL2.val: 
            root = curL1
            curL1 = curL1.next
        else: 
            root = curL2
            curL2 = curL2.next
        curNode = root
        while curL1 is not None or curL2 is not None:
            if curL1 is None: 
                curNode.next = curL2
                curL2 = curL2.next
            elif curL2 is None:
                curNode.next = curL1
                curL1 = curL1.next
            elif curL1.val < curL2.val: 
                curNode.next = curL1
                curL1 = curL1.next
            else: 
                curNode.next = curL2
                curL2 = curL2.next
            curNode = curNode.next
        return root