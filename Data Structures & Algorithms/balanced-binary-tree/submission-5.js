/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {


    isBalanced(root){
       function dfs(root){
            if(!root) return [true,0]   
            const l = dfs(root.left)
            const r = dfs(root.right)
            const balanced = l[0] && r[0] && Math.abs(l[1] - r[1]) <=1
            return [balanced, Math.max(l[1],r[1]) +1]
        }
        return dfs(root)[0]
        
    }
}
