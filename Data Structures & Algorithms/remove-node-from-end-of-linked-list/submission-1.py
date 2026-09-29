# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow_idx = 0
        fast_idx = 0
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            slow_idx += 1
            fast = fast.next.next
            fast_idx += 2
        length = fast_idx
        if fast != None:
            length += 1
        rem_idx = length - n
        p = head
        prev = None
        tracker = 0
        if rem_idx > slow_idx:
            p = slow
            tracker = slow_idx
        while tracker < rem_idx:
            prev = p
            p = p.next
            tracker += 1
        if prev:
            prev.next = p.next
        else:
            head = p.next
        return head
        