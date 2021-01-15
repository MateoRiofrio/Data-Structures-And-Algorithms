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