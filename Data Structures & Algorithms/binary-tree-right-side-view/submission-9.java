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
    private List<Integer> rs = new ArrayList<>();
    public void levelOrderTraversal(TreeNode root){
        if(root == null) return;

        TreeNode rightNode = null;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
         while(q.size() > 0){
            int levelSize = q.size();
            for (int i =0; i < levelSize; i ++){
                TreeNode r = q.poll();
                rightNode = r;
                if(r.left != null){
                    q.add(r.left);

                }
                if(r.right!=null){
                    q.add(r.right);
                }
            }
            rs.add(rightNode.val);

         }
        
    }
    public List<Integer> rightSideView(TreeNode root) {
        levelOrderTraversal(root);
        return rs;

    }
}
