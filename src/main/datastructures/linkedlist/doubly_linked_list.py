class Node:
    "Doubly Linked List Node that holds data, previous node, and next node."
    def __init__(self, data = None, prev = None, next_= None):
        self.data = data
        self.next = next_
        self.prev = prev

    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    """Doubly linked list using nodes.
    
    __init__ takes creates a top and bottom sentinel and initializes the length of the list to 0.
    
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

    # 'add' has same functionality as 'add_first'
    add = add_first

    def add_last(self, node):
        """Add node to the bottom of the doubly linked list."""
        if(self.is_empty() == True):
            # node points to top and bottom sentinel
            new_last_node = Node(self.top_sentinel, self.bottom_sentinel)
            self.top_sentinel = new_last_node
            self.bottom_sentinel.prev = new_last_node
        else:
            # node points to old bottom node and bottom sentinel
            new_node = Node(node, self.bottom_sentinel.prev, self.bottom_sentinel)
            self.bottom_sentinel.prev.next = new_node
            self.bottom_sentinel.prev = new_node
        
        self.length += 1
    
    def pop(self):
        """Remove the item at the top of the list."""
        if(self.is_empty() == True):
            return None

        # assign variables to the target node and the new top node
        target_node = self.top_sentinel.next
        new_top_node = target_node.next

        # point the new top node
        self.top_sentinel.next = new_top_node
        new_top_node.prev = self.top_sentinel
        self.length -= 1

        return target_node.data
    
    def poll(self):
        """Remove the item at the bottom of the list."""
        if(self.is_empty() == True):
            return None

        # assign variables to the target node and the node before the target node. 
        target_node = self.bottom_sentinel.prev
        new_bottom_node = target_node.prev

        # point to new bottom node
        self.bottom_sentinel.prev = new_bottom_node
        new_bottom_node.next = self.bottom_sentinel
        self.length -= 1

        return target_node.data