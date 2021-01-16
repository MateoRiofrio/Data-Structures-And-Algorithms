class Node:
    "Doubly Linked List Node that holds data, next node, and previous, node."
    def __init__(self, data = None, foward = None, prev = None):
        self.data = data
        self.next = foward
        self.prev = prev

    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    """Doubly linked list using nodes.
    
    __init__ method creates a sentinel node and initializes the length of the list to 0.
    
    Attributes:
        top_sentinel (Node): empty node that is always at the beginning of the linked list.
        bottom_sentinel (Node): empty node that is always at the beginning of the linked list.
        length (int): size of the linked list. 
    """

    def __init__(self):
        self.top_sentinel = Node() 
        self.bottom_sentinel = Node() 
        self.length = 0