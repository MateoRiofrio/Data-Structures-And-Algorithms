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
    
    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length
    
    def add_first(self, node):
        """Add node to the top of the doubly linked list."""
        if(self.is_empty() == True):
            # node points 'prev' to the top sentinel and 'next_' to the bottom sentinel
            new_node = Node(node, self.top_sentinel, self.bottom_sentinel)
            self.top_sentinel.next = new_node
            self.bottom_sentinel.prev = new_node
        else:
            # node points 'prev' to top sentinel and 'next_' to the old top node  
            new_node = Node(node, self.top_sentinel, self.top_sentinel.next)
            self.top_sentinel.next.prev = new_node
            self.top_sentinel.next = new_node
    
        self.length += 1

    # 'add' has same functionality as add_first
    add = add_first