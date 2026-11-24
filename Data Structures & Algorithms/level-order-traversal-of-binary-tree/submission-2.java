/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        List<List<Integer>> output = new ArrayList<>();
        while (!q.isEmpty()){
            int levelLength = q.size();
            ArrayList<Integer> level = new ArrayList<>();

            for(int i = 0; i < levelLength; i ++){
                // remove head of queue, if null return empty
                TreeNode curr = q.poll();
                
                // check for null to prevent NullPointerException
                if(curr != null){
                level.add(curr.val);
  
                q.add(curr.left);

                q.add(curr.right);
                }


                
            }

            // if there is nothing in the level, dont add
            if(level.size() > 0){
            output.add(level);

            }
        }
        return output;
    }
}
