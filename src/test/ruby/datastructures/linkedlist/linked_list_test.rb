require "./src/main/ruby/datastructures/linkedlist/linked_list"
require "test/unit"

class TestLinkedList < Test::Unit::TestCase

    def setup
        @list = LinkedList.new
        @TEST_SZ = 50
    end

    def test_new_sllist_size
        # test empty sllist
        assert_equal(0, @list.size)

        # test smallest non-empty sllist
        @list.push(3)
        assert_equal(1, @list.size)

        # test a higher bound 
        for i in 1..@TEST_SZ
            @list.push(i)
        end
        assert_equal(51, @list.size)
    end

    def test_is_empty
        assert(@list.is_empty)

        @list.push(3)
        assert(!@list.is_empty)
    end

    def test_contains_one_item
        assert(!@list.contains(3))
        @list.push(3)
        assert(@list.contains(3))
    end

    def test_contains_multiple_items
        for i in 1..@TEST_SZ
            @list.push(i)
        end
        
        for i in 1..@TEST_SZ
            assert(@list.contains(i))

        end
    end
    def test_push_one_item
        @list.push(5)
        assert_equal(1, @list.size)
        assert(!@list.contains(2)) # check it does not contain a different number
        assert(@list.contains(5))
    end

    def test_push_multiple_items
        lst_one = [1,3,5,7,9]
        lst_two = [2,4,6,8,10]
        for num in lst_one
            @list.push(num)
        end
        assert_equal(5, @list.size)
        
        # check list contains items pushed
        for num in lst_one
            assert(@list.contains(num))
        end
        # check no incorrect numbers were added
        for num in lst_two
            assert(!@list.contains(num))
        end
    end

    def test_pop_one_item
        assert_raise(IndexError){
            @list.pop
        }
        @list.push(1)
        assert_equal(1, @list.pop)
        assert_equal(0, @list.size)
    end

    def test_pop_multiple_items
        for i in 1..@TEST_SZ
            @list.push(i)
        end
        assert_equal(@TEST_SZ, @list.pop)
    end
end