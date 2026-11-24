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
     * @return {number}
     */

    diameterOfBinaryTree(root) {
        let diameter = 0
        function calculateDiameter(root){
            if(root == null) return 0;
            const l = calculateDiameter(root.left)
            const r = calculateDiameter(root.right)
            diameter = Math.max(diameter, l + r)
            return Math.max(l,r) +1
        }
        calculateDiameter(root)
        return diameter
    }
}
