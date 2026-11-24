class Solution {

    private int[] unionArr;
    private int find(int e1) {
        int par = unionArr[e1];
        int currEdge = e1;
        // it is parent of itself
        if(par < 0) return e1;
        // optimise the path to improve time complexity

        // find the root first. the root is when unionArr[currEdge] is negative.
        while(unionArr[currEdge] >= 0){
            currEdge = unionArr[currEdge];
        }
        // keep pointer to the root
        int root = currEdge;

        // reset pointer of currEdge to e1
        currEdge = root;

        // for all child nodes, point them to root
        while(unionArr[currEdge] >= 0){
            // save current parent as temporary variable
            int p = unionArr[currEdge];

            unionArr[currEdge] = root;
            // change pointer to parent so loop can continue
            currEdge = p;

        }
        // par found
        return root;
    }




    // union find: negative number means it is parent of itself
    // magnitude of negative number means the number of nodes connected to
    // it (including itself)
    // positive number means that it has a parent that is not itself.
    private void union(int e1,int e2){
        int p1 = find(e1);
        int p2 = find(e2);
        if(p1 == p2) return;
        // check the rank/ number of nodes connected to it
        int rank1 = unionArr[p1];
        int rank2 = unionArr[p2];
        // if p1 has more nodes connected to it, should set p2 to have 
        // parent of p1.
        if(Math.abs(rank1) > Math.abs(rank2)){
            // increase rank of p1
            unionArr[p1] += unionArr[p2];
            // assign p1 to be parent of p2
            unionArr[p2] = p1;
        }
        else{
            unionArr[p2] += unionArr[p1];
            unionArr[p1] = p2;
        }
    }

    public int countComponents(int n, int[][] edges) {
        if(edges.length ==0) return n;
        // initialise the rank and weight array list
         unionArr = new int [n];

        // assign -1 to indicate that each of them are parents to its own
        for(int i = 0; i < n; i ++ ){
            unionArr[i] = -1;
        }
        // union all the edges
        for(int[] connection: edges){
            union(connection[0], connection[1]);
        }

        int numConnected = 0;
        // for loop to find the number of connected edges.
        for(int i : unionArr){

            // it is the parent
            if( i < 0){
                numConnected += 1;
            }
        }
        return numConnected;
    }
}
