/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) {
            return null;
        }

        TreeNode mergedTree = new TreeNode(0);
        if (t1 == null) {
            mergedTree.left = mergeTrees(null, t2.left);
            mergedTree.right = mergeTrees(null, t2.right);
            mergedTree.val = t2.val;
        } else if (t2 == null) {
            mergedTree.left = mergeTrees(t1.left, null);
            mergedTree.right = mergeTrees(t1.right, null);
            mergedTree.val = t1.val;
        } else {
            mergedTree.left = mergeTrees(t1.left, t2.left);
            mergedTree.right = mergeTrees(t1.right, t2.right);
            mergedTree.val = t1.val + t2.val;
        }
        
        return mergedTree;
    }
}