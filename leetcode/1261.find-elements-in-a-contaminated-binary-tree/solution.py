# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.valSet = set()
        self.recover(root, 0)
        
    
    def recover(self, node: Optional[TreeNode], expectedVal: int) -> None:
        if node is None: return
        node.val = expectedVal
        self.valSet.add(expectedVal)
        # print("Setting node to {}".format(expectedVal))
        self.recover(node.left, expectedVal * 2 + 1)
        self.recover(node.right, expectedVal * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.valSet    

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)