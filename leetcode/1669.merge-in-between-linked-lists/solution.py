# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        index = 0
        curNode = list1
        prevNode = None
        afterNode = None

        while index < a - 1:
            curNode = curNode.next
            index += 1
        prevNode = curNode
        while index <= b:
            curNode = curNode.next
            index += 1
        afterNode = curNode

        # print(prevNode.val, afterNode.val)

        prevNode.next = list2
        newCurNode = list2
        finalPrevNode = None
        while newCurNode is not None:
            finalPrevNode = newCurNode
            newCurNode = newCurNode.next

        finalPrevNode.next = afterNode
        return list1