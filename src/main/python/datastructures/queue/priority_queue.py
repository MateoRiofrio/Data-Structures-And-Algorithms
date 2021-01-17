from min_heap import MinHeap

class MinPriorityQueue:
    """Priority Queue following natural ordering using a minimum heap."""
    def __init__(self):
        self.heap = MinHeap()
        self.length = 0

    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def clear(self):
        self.heap.clear()
    
    def insert(self, data):
        self.heap.insert(data)
        self.length += 1
    
    def min(self):
        """Remove and return the minimum element from the queue."""
        self.length -= 1
        return self.heap.find_min()