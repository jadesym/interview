# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curNode = head
        result = []
        while curNode is not None:
            result.append(curNode.val)
            curNode = curNode.next
        maxSum = 0
        for i in range(0, len(result), 2):
            maxSum = max(maxSum, result[i] + result[len(result)-i - 1])
        return maxSum
            