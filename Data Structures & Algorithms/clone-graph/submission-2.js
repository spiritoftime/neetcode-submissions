/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    /**
     * @param {Node} node
     * @return {Node}
     */
    cloneGraph(node) {
        const oldToNew = new Map()
        function dfs(node){
            if(node == null) return null
            if(oldToNew.has(node)) return oldToNew.get(node)
            // create new node
            const newNode = new Node(node.val)
            oldToNew.set(node,newNode)
            for(const n of node.neighbors){
                oldToNew.get(node).neighbors.push(dfs(n))
            }
            return oldToNew.get(node)
        }
        return dfs(node)
    }
}
