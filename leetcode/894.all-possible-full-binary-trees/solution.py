from copy import deepcopy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.n_cache = {}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0: return []

        if n in self.n_cache:
            return self.n_cache[n]

        if n == 1:
            self.n_cache[n] = [TreeNode(0)]
            return self.n_cache[n]

        print("Running on {}".format(n))
        tree_size_pairs = []
        # 3: [(1, 1)]
        # 5: [(1, 3), (3, 1)]
        for i in range(1, n, 2):
            tree_size_pairs.append((i, n - i - 1))

        left_tree_combos = []
        right_tree_combos = []
        for tree_size_pair in tree_size_pairs:
            left_size, right_size = tree_size_pair
            left_tree_combos.append(deepcopy(self.allPossibleFBT(left_size)))
            right_tree_combos.append(deepcopy(self.allPossibleFBT(right_size)))

        result_trees = []
        for i in range(len(left_tree_combos)):
            left_tree_combo = left_tree_combos[i]
            right_tree_combo = right_tree_combos[i]
            for left_tree in left_tree_combo:
                for right_tree in right_tree_combo:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    result_trees.append(root)
        self.n_cache[n] = result_trees
        return result_trees


