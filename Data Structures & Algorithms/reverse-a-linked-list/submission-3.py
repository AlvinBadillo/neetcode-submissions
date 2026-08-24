# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # so we need an extra node here, to store the data before moving the pointers
        prev = None

        curr_n = head

        if not head:
            return None

        while curr_n.next:
            print(curr_n.val)
            # we need now to first save the details of the next node on temp
            # this is what we will update as curr at the very end
            next_node = curr_n.next
            
            # now make curr look back
            curr_n.next = prev
            # now update prev for next call
            prev = curr_n
            curr_n = next_node
        # Finally update the last unprocecesed node
        curr_n.next = prev
        return curr_n

        