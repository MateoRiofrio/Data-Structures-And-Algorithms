import unittest
from src.main.python.datastructures.queue.deque import Deque

class TestDeque(unittest.TestCase):
    
    def setUp(self):
        self.deque = Deque()
        self.TEST_SZ = 50
        
    def test_is_empty(self):
        # empty deque
        self.assertTrue(self.deque.is_empty())

        # smallest non-empty deque
        self.deque.add_first(3)
        self.assertFalse(self.deque.is_empty())

    def test_size(self):
        # empty and smallest non-empty dedque
        self.assertEqual(self.deque.size(), 0)
        self.deque.add_first(5)
        self.assertEqual(self.deque.size(), 1)
        
        # higher bound size 
        for elem in range(self.TEST_SZ):
            self.deque.add_first(elem)
        self.assertEqual(self.deque.size(), self.TEST_SZ + 1)

    def test_add_first(self):
        # test smallest non-empty deque
        self.deque.add_first(3)
        self.assertEqual(self.deque.size(), 1)

        # test on deque of size 51
        for elem in range(self.TEST_SZ):
            self.deque.add_first(elem)
        self.assertEqual(self.deque.size(), self.TEST_SZ + 1)

        # test element is added on top
        self.assertEqual(self.deque.pop(), self.TEST_SZ - 1)

    def test_add_last(self):
        # test smallest non-empty deque
        self.deque.add_last(3)
        self.assertEqual(self.deque.size(), 1)

        # test on deque of size 51
        for elem in range(self.TEST_SZ):
            self.deque.add_last(elem)
        self.assertEqual(self.deque.size(), self.TEST_SZ + 1)

        # test last element added correctness
        self.assertEqual(self.deque.remove_last(), self.TEST_SZ - 1)
    
    def test_remove_last(self):
        # empty deque returns None
        self.assertIsNone(self.deque.remove_last())

        # smallest non-empty deque should return only item
        self.deque.add_first(2)
        self.assertEqual(self.deque.remove_last(), 2)
    
        # test on deque of 50 elements
        for elem in range(self.TEST_SZ):
            self.deque.add_first(elem)
        self.assertEqual(self.deque.remove_last(), 0)

    def test_pop(self):
        # empty deque returns None
        self.assertIsNone(self.deque.pop())
    
        # smallest non-empty deque should return only item
        self.deque.add_first(1)
        self.assertEqual(self.deque.pop(), 1)

        # test on deque of 50 elements
        for elem in range(self.TEST_SZ):
            self.deque.add_first(elem)
        self.assertEqual(self.deque.pop(), self.TEST_SZ - 1)

if __name__ == '__main__':
    unittest.main()    
    


