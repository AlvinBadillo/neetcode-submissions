# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Verify there are at least two nodes
        if head.next is None:
            return False
        # Set up pointers
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            # Check if we have a loop
            if fast == slow:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        # If we exit the loop it means there is no loop
        return False