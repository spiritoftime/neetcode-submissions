/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    private HashMap<Node,Node> oldToNew = new HashMap<>();

    public void dfs(Node node){
        //  node has already been cloned
        if(oldToNew.containsKey(node)){
            return;
        }
        Node clone = new Node(node.val);
        oldToNew.put(node, clone);
        for(Node n: node.neighbors){
            dfs(n);
            oldToNew.get(node).neighbors.add(oldToNew.get(n));
        }
    }
    public Node cloneGraph(Node node) {
        if(node == null) return null;
        dfs(node);
        return oldToNew.get(node);
    }
}