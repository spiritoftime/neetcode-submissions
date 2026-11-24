# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recurse(self,curr,list1,list2):
        if not list1 or not list2:
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2           
            return
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2  = list2.next
        curr = curr.next
        self.recurse(curr,list1,list2)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       dummy = curr = ListNode()
       self.recurse(curr,list1,list2)
       return dummy.next


       
       
       
        # dummynode = ListNode()
        # curr = dummynode
        # while list1 and list2:
        #     if list1.val < list2.val: # add list1 curr node first
        #         curr.next = list1
        #         list1 = list1.next
        #     else:
        #         curr.next = list2
        #         list2 = list2.next
        #     curr = curr.next

        # if list1:
        #     curr.next = list1
        # if list2:
        #     curr.next = list2
        # return dummynode.next

