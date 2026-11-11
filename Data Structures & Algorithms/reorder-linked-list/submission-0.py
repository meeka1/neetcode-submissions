# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        li = []
        node = head

        while node:
            li.append(node)
            node = node.next

        n = len(li)
        p1, p2 = 1, n
        new_li = []

        while len(new_li) < len(li):
            new_li.append(li[n-p2])

            if len(new_li) < len(li):
                new_li.append(li[n-p1])
            p2 -= 1
            p1 += 1
    
        for i in range(len(new_li)-1):
            new_li[i].next = new_li[i+1]
        
        if new_li:
            new_li[-1].next = None
