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
        const q = [root]
        const res = []
        while(q.length > 0){
                    let rightMostNode = null;

            const iterations = q.length;
            for(let i=0; i < iterations; i ++){
                const curr = q.shift()
                if(curr){
                    rightMostNode = curr
                    q.push(curr.left)
                    q.push(curr.right)
                }


            }
            if(rightMostNode)
            res.push(rightMostNode.val)
        }
        return res
    }
}
