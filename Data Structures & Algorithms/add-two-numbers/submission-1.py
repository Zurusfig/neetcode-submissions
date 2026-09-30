# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 != None and l2 != None:
            added = l1.val + l2.val + carry
            digit = added % 10
            carry = added // 10
            tail.next = ListNode()
            tail.next.val = digit
            tail = tail.next
            if l1.next == None and l2.next != None:
                l1.next = ListNode()
                l1.next.val = 0
            if l1.next != None and l2.next == None:
                l2.next = ListNode()
                l2.next.val = 0
            l1 = l1.next
            l2 = l2.next
                
        if carry == 1:
            tail.next = ListNode()
            tail.next.val = 1
            tail = tail.next
        return dummy.next

        