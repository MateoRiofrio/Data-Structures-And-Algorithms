class BinarySearch:
    """Binary Search that returns either the position of the target, or the number of iterations.
    
    Attributes:
        arr (list): array of elements.
        target: element to search.
        count (bool): default to False, if true return number of iterations instead.
    """
    def search(self, arr, target, count = False):
        low = 0
        high = len(arr) - 1
        cnt = 0

        while(low <= high):
            cnt += 1
            mid = (low + high) // 2
            mid_val = arr[mid]

            if (mid_val < target):
                low = mid + 1
            
            elif (mid_val > target):
                high = mid - 1
            
            else:
                if count == False: return mid 
                else: return cnt
        
        if count == False: return -1
        else: return cnt
