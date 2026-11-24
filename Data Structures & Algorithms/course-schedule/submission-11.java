class Solution {
    private HashMap<Integer,ArrayList<Integer>> hm = new HashMap<>();
    private HashSet<Integer> visited = new HashSet<>();
    public boolean checkCycle(int c){
        // if we have seen the edge before
        if (visited.contains(c)){
            return true;
        }
        // add the current node to the set
        visited.add(c);
        for(int preReq: hm.getOrDefault(c, new ArrayList<Integer>() )){
            // check the preReqs for cycle
            if (checkCycle(preReq) == true){
                return true;
            }
        }
        // backtrack - revert the state.
        visited.remove(c);
        // no cycle detected
        return false;
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // populate the hashmap
        for(int[] connection : prerequisites){
            ArrayList<Integer> prereqList = hm.getOrDefault(
                connection[0],
                new ArrayList<Integer>()
            );
            // add the prerequisite
            prereqList.add(connection[1]);
            // populate the hashmap
            hm.put(connection[0], prereqList);

        }

        for(int c: hm.keySet()){
            // if there is a cycle, it is not possible to finish all course
            if (checkCycle(c) == true){
                return false;
            }
        }

        // no cycle
            return true;

    }
}
