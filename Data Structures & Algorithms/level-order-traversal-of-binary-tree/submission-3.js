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
     * @return {number[][]}
     */
    levelOrder(root) {
    if(!root) return []
        const q = [root]
        const res=[]
        while(q.length > 0){
            const level = []
            const iterations = q.length
            for(let i = 0; i < iterations; i++){
                const curr = q.shift()
                level.push(curr.val)

                if(curr.left){
                    q.push(curr.left)

                }
                if(curr.right){
                    q.push(curr.right)
                }
            }
            if(level.length > 0) res.push(level)
        }
        return res
    }
}
