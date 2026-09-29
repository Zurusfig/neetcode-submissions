# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow
        half = slow.next
        tmp.next = None

        # reverse second list half
        prev = None
        while half != None:
            tmp = half
            half = half.next
            tmp.next = prev
            prev = tmp
        head2 = prev

        # merge 
        head1 = head
        while head2 != None:
            tmp1 = head1.next
            head1.next = head2
            tmp2 = head2.next
            head2.next = tmp1
            head1 = tmp1
            head2 = tmp2
        
        
        


            
