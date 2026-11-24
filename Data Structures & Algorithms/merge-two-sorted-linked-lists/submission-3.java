/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode l1Node = list1;
        ListNode l2Node = list2;
        // initialize a listNode - dont set as null
        ListNode newHead = new ListNode(-1);
        ListNode returnHead = newHead;
        while (true){
            if(l1Node == null || l2Node == null){
                break;
            }
            if(l1Node.val < l2Node.val){
                newHead.next = l1Node;
                l1Node = l1Node.next;
            } else{
                newHead.next = l2Node;
                l2Node = l2Node.next;
            }
            newHead = newHead.next;
        }
        if (l1Node != null){
            newHead.next = l1Node;
        }
                if (l2Node != null){
            newHead.next = l2Node;
        }
        return returnHead.next;
    }
}