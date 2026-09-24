# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        dummy = ListNode()
        tail = dummy
        while(c1!=None and c2!=None):
            if c1.val<c2.val:
                tail.next = c1
                tail = c1
                c1 = c1.next
            else:
                tail.next = c2
                tail = c2
                c2 = c2.next

        if c1!=None:
            tail.next = c1
        else:
            tail.next = c2

        return dummy.next