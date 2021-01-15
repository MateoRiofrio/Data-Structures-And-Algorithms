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

    def add(self, node):
        """Add a node to the top of the linked list."""
        if self.is_empty() != True:
            # if the list is not empty, create a new node and have it point to the current top node.
            new_node = Node(node, self.top_sentinel.next)
            self.top_sentinel.next = new_node
        else:
            # if the list is empty then have the top sentinel point to the given node.
            self.top_sentinel.next = Node(node)
    
        self.length += 1
        
    # add_first has same functionality as add.
    add_first = add

    def add_last(self, node):
        """Add a node to the bottom of the linked list."""
        prev_node = self.top_sentinel
        top = self.top_sentinel.next
        
        while top is not None:
            prev_node = top
            top = top.next
        prev_node.next = Node(node)
        self.length += 1

    def remove(self, target):
        """Remove the first instance of a node."""
        prev_node = self.top_sentinel
        top = self.top_sentinel.next
        while top is not None:
            if(top.data == target):
                prev_node.next = top.next
                break
            prev_node = top
            top = top.next

        # update length after deletion accordingly.
        self.length -= 1

    def peek(self):
        """View the top element on the list."""
        if(self.length == 0):
            return None
            
        return self.top_sentinel.next.data

    def pop(self):
        """ Remove and then return the top element on the list."""
        if(self.length == 0):
            return None
        top = self.top_sentinel.next
        self.top_sentinel.next = top.next
        self.length -= 1

        return top.data

    def contains(self, target):
        """ Return true if the list contains the element passed."""
        if (target == None or self.length == 0):
            return False

        # check if top item is target node.
        top = self.top_sentinel.next
        if(top.data == target):
            return True
        
        # else traverse through the list until found. 
        while top.next is not None:
            if(top.data == target):
                return True
            top = top.next
    
        return False

    def is_empty(self):
        """Return true if the list is empty, false otherwise."""
        return self.length == 0
        
    def size(self):
        """Return the size of the linked list."""
        return self.length