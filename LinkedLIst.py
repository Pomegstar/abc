class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self,New_item):
        node = Node(New_item)
        node.next = self.head
        self.head = node
        return self.head
    
    def __str__(self):
         output = []
         curr = self.head
         while curr:
             output.append(curr.data)
             curr = curr.next
         return str(output)
    
    def delete(self,item):
        if self.head.data == item:
            self.head = self.head.next
            return self.head
        
        prev = None
        curr = self.head
        while curr and curr.data != item:
            prev = curr
            curr = curr.next
        if curr != None:
            prev.next = curr.next       
        return self.head
list = LinkedList()
list.add(2)
list.add(63)
list.add(65)
list.add(4)
list.delete(63)
print(list)
    