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

class Solution {
    private int maxDiameter = 0;
    public int calculateHeight(TreeNode root){
        if(root == null) return 0;
        int left = calculateHeight(root.left);
        int right = calculateHeight(root.right);

        this.maxDiameter = Math.max(left+right,this.maxDiameter);
        return Math.max(left,right) + 1;
    }
    public int diameterOfBinaryTree(TreeNode root) {
        calculateHeight(root);
        return this.maxDiameter;

    }
}
