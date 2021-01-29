from linked_list import LinkedList

class Stack:
    """Stack representation using Linked List created previously (in repo)."""
    def __init__(self):
        self.lst = LinkedList()
    
    def is_empty(self):
        return self.lst.is_empty()

    def size(self):
        """Return the size of the stack."""
        return self.lst.size()
    
    def push(self, data):
        """Add an element to front of the linked list representing the stack."""
        self.lst.add_first(data)

    def pop(self):
        """Remove the top element from the linked list representing the stack."""
        return self.lst.pop()        
    
    def reverse_array(self, arr):
        """Reversing an array using the stack."""
        
        # push items into stack.
        for i in arr:
            self.push(i)

        # return reveresed items array. 
        return [self.pop() for _ in arr]