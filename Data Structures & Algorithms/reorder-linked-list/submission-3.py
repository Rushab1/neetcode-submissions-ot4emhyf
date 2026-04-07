# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        if slow is None or slow.next is None:
            # list has length 1 or 2
            return 

        # reverse everything after slow
        prev = slow.next
        it = prev.next
        slow.next = None
        prev.next = None

        while it:
            tmp = it.next
            it.next = prev
            prev = it
            it = tmp

        head2 = prev

        it = head
        while it and head2:
            itnext = it.next
            head2next = head2.next

            it.next = head2
            head2.next = itnext
            head2 = head2next
            it = itnext

