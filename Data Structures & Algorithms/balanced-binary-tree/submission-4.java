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
    // returns an array of 2 values - isBalanced and height.
    // if not balanced - 0. if balanced - 1
    public int[] getIsBalancedAndHeight(TreeNode root){
        if(root == null){
            return new int[]{1,0};
        }
        int[] left = getIsBalancedAndHeight(root.left);
        int[] right =  getIsBalancedAndHeight(root.right);

        // as long as both are inbalanced, immediately propogate upward
        if(left[0] == 0 || right[0] == 0) return new int[]{0,0};

        int maxHeight = Math.max(left[1],right[1]);
        if(Math.abs(left[1] - right[1] ) > 1){
            return new int[]{0,maxHeight + 1};
        }
        return new int[]{1,maxHeight + 1};


    }

    public boolean isBalanced(TreeNode root) {
        int[] isBalancedAndHeight = getIsBalancedAndHeight(root);
        return isBalancedAndHeight[0] == 1; 
    }
}
