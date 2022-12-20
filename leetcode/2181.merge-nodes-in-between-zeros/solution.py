# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addNode(self, val: int, resultListNode: Optional[ListNode]) -> ListNode:
        if resultListNode is None: return ListNode(val)
        else:
            resultListNode.next = ListNode(val)
            return resultListNode.next

    def print(self, resultListNode: Optional[ListNode]):
        if resultListNode is None: print("None")
        else:
            result = []
            curNode = resultListNode
            while curNode is not None:
                result.append(curNode.val)
                curNode = curNode.next
            print(result)

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        currentSum = 0
        result = None
        tail = None

        curNode = head
        while curNode is not None:
            if curNode.val == 0:
                if currentSum > 0:
                    newNode = self.addNode(currentSum, tail)
                    tail = newNode
                    if result is None: result = newNode
                    currentSum = 0
            else:
                currentSum += curNode.val
            curNode = curNode.next

        if currentSum > 0:
            newNode = self.addNode(currentSum, tail)
            tail = newNode
            if result is None: result = newNode
        return result