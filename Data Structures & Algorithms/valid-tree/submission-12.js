class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {boolean}
     */
    validTree(n, edges) {
        const adjList = {}
        for(let i = 0; i < n;i++){
            adjList[i] = []
        }
        for(const [e1,e2] of edges){
            adjList[e1].push(e2)
            adjList[e2].push(e1)
        }
        const visited = new Set()
        function dfs(node, parent){
            
            if(visited.has(node)) return false
            visited.add(node)
            for(const n of adjList[node]){
                if(n === parent) continue
                if(!dfs(n, node)) return false
            }
            return true
        }
        return dfs(0,-1) && visited.size === n
    }   
}
