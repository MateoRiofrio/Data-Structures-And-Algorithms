# Sentinel Linked list representation using nodes. 
# insert/delete at beginning: O(1), insert/delete at end: O(n)

class Node
    attr_accessor :data, :next

    def initialize(data = nil, next_ = nil)
        @data = data
        @next = next_
    end

    def to_s
        "#{data}"
    end
end

class LinkedList
    def initialize
        @top_sentinel = Node.new
        @length = 0
    end

    def size
        @length
    end

    def is_empty
        @length == 0
    end 

    def push(data)
        if is_empty
            @top_sentinel.next = Node.new(data)
            
        else
            new_node = Node.new(data, @top_sentinel.next)
            @top_sentinel.next = new_node
        end
        @length += 1
    end

    def pop
        if is_empty
            raise IndexError.new "pop from empty list"
        elsif size == 1
            top_node = @top_sentinel.next
            @top_sentinel.next = nil
            return top_node.data
        else
            top_node = @top_sentinel.next
            @top_sentinel.next = top_node.next
            return top_node.data
        end
    end 
        
    def contains(target)
        return false if is_empty

        # return top node if the target 
        node = @top_sentinel.next
        return true if node.data == target
        
        #loop through list and return target if found
        while (node.next != nil)
            node = node.next
            return true if node.data == target
        end 
        
        #otherwise, not in list
        return false
    end
end
