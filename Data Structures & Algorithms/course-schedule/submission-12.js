class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses, prerequisites) {
 

        const preMap = new Map()
        const visited = new Set()
        function dfs(c){
            if(visited.has(c)) return false
            if(!preMap.has(c) || preMap.get(c).length == 0)return true
            visited.add(c)
            for(const pre of preMap.get(c)){
                if(!dfs(pre)) return false
            }
            visited.delete(c)
            preMap.set(c,[])
            return true
        }
        for(const [c, pre] of prerequisites){
            if(!preMap.has(c)){
                preMap.set(c,[pre])
            }else{
                preMap.get(c).push(pre)
            }
        }
        for(let i =0; i < numCourses; i++){
            if(!dfs(i)) return false
        }
        return true

    }
}
