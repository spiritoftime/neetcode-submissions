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
    private int goodNodes = 0;
    public void dfs(TreeNode root, int largestPrev){
        if(root == null) return;
        if(root.val >= largestPrev){
            largestPrev = root.val;
            goodNodes +=1;
        }
         dfs(root.left, largestPrev);
         dfs(root.right,largestPrev);
    }
    public int goodNodes(TreeNode root) {
         dfs(root,-101);
         return goodNodes;
    }
}
