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
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isValid(root,l,r){
        if(!root) return true
        if(!(root.val > l && root.val < r)) return false
        return this.isValid(root.left, l, root.val) &&
        this.isValid(root.right,root.val, r)
    }
    isValidBST(root) {
        return this.isValid(root,-Infinity, Infinity)
    }
}
