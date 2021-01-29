from doubly_linked_list import DoublyLinkedList

class Deque:
    """Deque representation using a Doubly Linked List."""
    def __init__(self):
        self.lst = DoublyLinkedList()
        self.length = 0

    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def add_first(self, data):
        """Add to the top of the deque."""
        self.lst.add_first(data)
        self.length += 1
    
    def add_last(self, data):
        """Add to the bottom of the deque."""
        self.lst.add_last(data)
        self.length += 1
    
    def pop(self):
        """Remove and return the top element of the deque."""
        self.length -= 1
        return self.lst.pop()
    
    def remove_last(self):
        """Remove and return the bottom element of the deque."""
        self.length -=1
        return self.lst.poll()
    