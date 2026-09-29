# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow, fast = head, head.next
        if fast == None:
            return False
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast == None or fast.next == None:
                return False
            fast = fast.next
        return True
