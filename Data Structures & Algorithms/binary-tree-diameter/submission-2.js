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
    constructor(){
        this.diameter = 0
    }
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    dfs(root){
        if(root === null) return 0;
        const left = this.dfs(root.left)
        const right = this.dfs(root.right)
        this.diameter = Math.max(left+right, 
        this.diameter
        )
        return Math.max(left,right) + 1
    }
    diameterOfBinaryTree(root) {
        this.dfs(root)
        return this.diameter
    }
}
