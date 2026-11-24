class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
    countComponents(n, edges) {
        const adjList = {}
        for(let i = 0 ; i < n; i ++){
            adjList[i] = []
        }
        for (const [e1,e2] of edges){
            adjList[e1].push(e2)
            adjList[e2].push(e1)
        }
        const visited = Array(n).fill(false)
        const dfs = (node)=>{
            for(const n of adjList[node]){
                if(!visited[n]){
                    visited[n] = true
                    dfs(n)
                }
            }
        }
        let res  = 0
        for(let i = 0; i <n ; i++){
            if(!visited[i] && i in adjList){
                visited[i] = true
                dfs(i)
                res++
            }
        }
        return res      

    }
}
