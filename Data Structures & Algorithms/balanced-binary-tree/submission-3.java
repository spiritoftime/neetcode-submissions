class Solution {
    // returns an array of 2 values: [isBalanced, height]
    // isBalanced: 0 if unbalanced, 1 if balanced
    // height: height of the current subtree
    public int[] getIsBalancedAndHeight(TreeNode root) {
        if (root == null) {
            return new int[]{1, 0}; // Tree is balanced, height is 0
        }
        
        int[] left = getIsBalancedAndHeight(root.left);  // Left subtree
        int[] right = getIsBalancedAndHeight(root.right); // Right subtree
        
        // If any subtree is unbalanced, propagate the unbalanced status
        if (left[0] == 0 || right[0] == 0) {
            return new int[]{0, 0};
        }
        
        // Check if the current node's subtree is balanced
        if (Math.abs(left[1] - right[1]) > 1) {
            return new int[]{0, 0}; // Unbalanced
        }
        
        // Current node is balanced; return balanced status and height
        int height = Math.max(left[1], right[1]) + 1;
        return new int[]{1, height};
    }

    public boolean isBalanced(TreeNode root) {
        int[] isBalancedAndHeight = getIsBalancedAndHeight(root);
        return isBalancedAndHeight[0] == 1; // Return true if balanced
    }
}
