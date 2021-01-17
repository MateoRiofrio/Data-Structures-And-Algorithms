from doubly_linked_list import DoublyLinkedList

class Queue:
    """Queue representation using a Doubly Linked List."""
    def __init__(self):
        self.lst = DoublyLinkedList()
        self.length = 0
    
    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def enqueue(self, data):
        self.lst.add(data)
        self.length += 1
    
    def dequeue(self):
        self.length -=1
        return self.lst.poll()
             
