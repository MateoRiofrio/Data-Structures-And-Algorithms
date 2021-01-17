class MaxHeap:
    """Min Heap representation using a list."""
    def __init__(self):
        self.lst = []
        self.length = 0

    def __swap(self, index1, index2):
        temp = self.lst[index1]
        self.lst[index1] = self.lst[index2]
        self.lst[index2] = temp

    def __parent(self, index):
        return (index - 1) // 2
    
    def __left(self, index):
        return (index * 2) + 1
    
    def __right(self, index):
        return (index * 2) + 2
    
    def __greater(self, index1, index2):
        return self.lst[index1] > self.lst[index2]
    
    def __less(self, index1, index2):
        return self.lst[index1] < self.lst[index2]

    def __siftup(self):
        index = self.length - 1
        while(self.__less(self.__parent(index), index) and index > 0):
            self.__swap(index, self.__parent(index))
            index = self.__parent(index)          

    def __siftdown(self):
        """Move node up down if its children are greater."""
        index = 0

        # while node at idex has a leftt child
        while(self.__left(index) < self.length):
            smaller_child = self.__left(index)
            
            # if node's right child is greater than the left child
            if (self.__right(index) < self.length and self.__greater(self.__right(index), smaller_child)):
                smaller_child += 1 # this is now the right child

            # break if node is in correct position (greater than its children)
            if (self.__greater(index, smaller_child)):
                break
            
            else:
                self.__swap(index, smaller_child)
                index = smaller_child

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length
    
    def clear(self):
        self.lst.clear()
        self.length = 0

    def insert(self, data):
        self.lst.append(data)
        self.length += 1
        self.__siftup()
        

    def find_max(self):
        """Remove and return the minimum value in the list representing the heap."""
        if(self.is_empty() == True):
            return None

        item = self.lst[0]
        # move last node up. 
        self.lst[0] = self.lst[self.length - 1]
        self.lst[self.length - 1] = None 

        self.length -= 1
        self.__siftdown()

        return item 