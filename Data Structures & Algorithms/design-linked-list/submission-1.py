class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0: 
            return -1

        curr = self.head
        ind = 0

        while curr is not None:
            if ind == index:
                return curr.val
            
            curr = curr.next
            ind += 1
            
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        curr = self.head
        ind = 0
        while curr.next is not None:
            curr = curr.next
            ind += 1

        new_node = ListNode(val)  # val -> None
        curr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return -1
        
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head
        ind = 0
        while curr is not None:
            if ind == index - 1:
                new_node = ListNode(val)
                temp = curr.next
                curr.next = new_node
                new_node.next = temp
                return
            
            curr = curr.next
            ind += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return -1
        
        curr = self.head
        ind = 0

        while curr is not None:
            if ind == index-1:
                if curr.next is not None:
                    curr.next = curr.next.next
                return
            
            curr = curr.next
            ind += 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)