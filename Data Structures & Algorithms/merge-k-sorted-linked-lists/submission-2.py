# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None

        for i in range(len(lists)):
            p1 = result
            p2 = lists[i]

            dummy = ListNode(0, None)
            tail = dummy

            while p1 and p2:
                if p1.val <= p2.val:
                    tail.next = p1
                    p1 = p1.next
                else:
                    tail.next = p2
                    p2 = p2.next

                tail = tail.next

            if p1:
                tail.next = p1
            elif p2:
                tail.next = p2

            result = dummy.next

        return result
