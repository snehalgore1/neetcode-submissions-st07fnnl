# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        dummy = ListNode(0)
        # print(dummy.val)
        tail = dummy
        for val in reversed(values):
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next
