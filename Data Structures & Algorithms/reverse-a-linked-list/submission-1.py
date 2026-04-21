# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head

        while(curr is not None):
            # save reference to next
            next = curr.next
            # reverse link
            curr.next = prev
            # update prev
            prev = curr
            # update curr
            curr = next
        return prev