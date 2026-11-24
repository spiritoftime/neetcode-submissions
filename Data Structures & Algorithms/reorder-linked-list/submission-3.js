class Solution {
    /**
     * @param {ListNode} head
     * @return {void}
     */
    reorderList(head) {

        // Step 1: Find the middle of the list
        let slow = head;
        let fast = head;
        while (fast && fast.next) {
            fast = fast.next.next;
            slow = slow.next;
        }

        // Step 2: Reverse the second half
        let before = null;
        let l2 = slow.next;
        slow.next = null; // Break the list into two halves
        while (l2) {
            let after = l2.next;
            l2.next = before;
            before = l2;
            l2 = after;
        }

        // Step 3: Merge the two halves
        let l1 = head;
        while (before) {
            const tmp1 = l1.next;
            const tmp2 = before.next;
            l1.next = before;
            before.next = tmp1;
            l1 = tmp1;
            before = tmp2;
        }
    }
}
