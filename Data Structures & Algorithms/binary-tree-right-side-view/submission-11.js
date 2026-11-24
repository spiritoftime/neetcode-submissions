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
     * @return {number[]}
     */
    rightSideView(root) {
        if(!root) return []
        const q = [root]
        const res = []
        let rightMostNode = null;
        while(q.length > 0){
            const iterations = q.length;
            for(let i=0; i < iterations; i ++){
                const curr = q.shift()
                if(curr){
                    rightMostNode = curr
                }
                if(curr.left) q.push(curr.left)
                if(curr.right) q.push(curr.right)

            }
            res.push(rightMostNode.val)
        }
        return res
    }
}
