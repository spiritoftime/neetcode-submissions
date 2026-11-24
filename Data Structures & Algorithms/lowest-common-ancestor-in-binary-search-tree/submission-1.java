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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || p == null || q == null){
            return null;
        }
        // is root less than p and q? if yes, travel to the right where everything is greater
        if(root.val < p.val && root.val < q.val ){
            return lowestCommonAncestor(root.right,  p,  q);
        }
        // is root more than p and q?
        if(root.val > p.val && root.val > q.val ){
            return lowestCommonAncestor(root.left, p,  q);
        }
        // else, return root
        return root;
        
    }
}
