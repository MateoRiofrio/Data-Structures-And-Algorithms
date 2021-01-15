class Node:
    """Linked List Node that contains data and next node."""
    def __init__(self, data = None, next_ = None):
        self.data = data
        self.next = next_

    def __str__(self):
        return str(self.data)

class LinkedList:
    """Single linked list using nodes.
    
    __init__ method creates a sentinel node and initializes the length of the list to 0.
    
    Attributes:
        top_sentinel (Node): empty node that is always at the beginning of the linked list.
        length (int): size of the linked list. 
    """

    def __init__(self):
        self.top_sentinel = Node()
        self.length = 0

        
    def __iter__(self):
        node = self.top_sentinel.next
        while node is not None:
            yield node.data
            node = node.next
        
    def __str__(self):
        return str(list(self))
    
    def is_empty(self):
        """Return true if the list is empty, false otherwise."""
        return self.length == 0
        
    def size(self):
        """Return the size of the linked list."""
        return self.length
    
    def add_first(self, data):
        """Add a node to the top of the linked list."""
        if self.is_empty() == True:
            # if the list is empty then have the top sentinel point to the given node.
            self.top_sentinel.next = Node(data)
        else:
            # if the list is not empty, create a new node and have it point to the old top node.
            new_node = Node(data, self.top_sentinel.next)
            self.top_sentinel.next = new_node
    
        self.length += 1
        
    # add has same functionality as add_first.
    add = add_first
    
    
    

    
    
    