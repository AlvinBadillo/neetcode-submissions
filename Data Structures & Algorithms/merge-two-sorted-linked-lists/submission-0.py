# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Declacre starting node of new list
        dummy = ListNode()
        tail = dummy
        # Loop through both lists until we reach the end of the smallest one
        while list1 is not None and list2 is not None:
            # Search for smaller node and add that one to the list
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # After this we have to append the remaining of the list that has not been fully iterated
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
        # Return stating node
        return dummy.next