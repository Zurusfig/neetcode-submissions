# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = None
        end = None
        if list1 == None:
            if list2 == None:
                return None
            else:
                return list2
        if list2 == None:
            return list1
        
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                if list3 == None:
                    list3 = list1
                    list1 = list1.next
                    end = list3
                else:
                    end.next = list1
                    end = end.next
                    list1 = end.next
            else:
                if list3 == None:
                    list3 = list2
                    list2 = list2.next
                    end = list3
                else:
                    end.next = list2
                    end = end.next
                    list2 = end.next
        if list1 != None:
            end.next = list1
        if list2 != None:
            end.next = list2
        return list3