/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.Set;
import java.util.HashSet;

class Solution {
    boolean b = false;
    public boolean findTarget(TreeNode root, int k) {
        HashSet<Integer> set = new HashSet<Integer>();
        this.traverseTree(root, k, set);
        return b;
    }

    public void traverseTree(TreeNode node, int k, HashSet<Integer> set) {
        if (node == null) {
            return;
        }

        this.traverseTree(node.left, k, set);

        int complement = k - node.val;
        if (set.contains(complement)) {
            this.b = true;
            return;
        }
        set.add(node.val);

        this.traverseTree(node.right, k, set);
    }
}