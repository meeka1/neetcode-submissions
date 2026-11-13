# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in range(0, len(lists), 2):
            p1 = lists[i]
            p2 = lists[i+1] if i < len(lists)-1 else ListNode(0, None)

            p1_ind = p1
            p2_ind = p2
            dummy = ListNode(0, None)

            while p1.next and p2.next:
                if p1.val <= p2.val:
                    dummy.next = p1
                    p1 = p1.next
                else:
                    dummy.next = p2
                    p2 = p2.next
                
            if p1:
                dummy.next = p1
            elif p2:
                dummy.next = p2
        
        return dummy.next
