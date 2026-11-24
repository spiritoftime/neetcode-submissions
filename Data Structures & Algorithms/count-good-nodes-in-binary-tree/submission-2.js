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

    goodNodes(root) {
        let res = 0
        function dfs(root,greatestEncountered){
            if(!root) return
            if(root.val >= greatestEncountered){
                res += 1
            }
            greatestEncountered = Math.max(
                greatestEncountered,
                root.val
            )
            dfs(root.left, greatestEncountered)
            dfs(root.right, greatestEncountered)
        }
        dfs(root, root.val - 1)
        return res
    }
}
