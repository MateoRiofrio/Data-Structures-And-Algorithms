import unittest
from doubly_linked_list import DoublyLinkedList
import random

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.lst = DoublyLinkedList()
        self.MAX_RAND_NUM = 250
        self.TEST_SZ = 50
        
    def test_size(self):
        # test empty and of size 1 
        self.assertEqual(self.lst.size(), 0)
        self.lst.add(2)
        self.assertEqual(self.lst.size(), 1)

        # random size 
        for i in range(self.TEST_SZ):
            self.lst.add(i)
        self.assertEqual(self.lst.size(), self.TEST_SZ)
    
    def test_is_empty(self):
        self.assertTrue(self.lst.is_empty())
        self.lst.add(3)
        self.assertFalse(self.lst.is_empty())
    
    def test_add_first(self):
        self.lst.add_first(5)
        self.assertTrue(self.lst.size(), 1)
    
    def test_add_last(self):
        self.lst.add_last(3)
        self.assertTrue(self.lst.size(), 1)
    
    def test_pop(self):
        # test empty list
        self.assertIsNone(self.lst.pop())

        # test smallest non empty list
        self.lst.add(3)
        self.assertEqual(self.lst.pop(), 3)

        # test random size array
        rand_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        first_elem = rand_list[0]
        self.assertEqual(self.lst.pop(), first_elem)
    
    def test_poll(self):
        self.assertIsNone(self.lst.poll())

        self.lst.add(5)
        self.assertEqual(self.lst.poll(), 5)

        rand_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        last_elem = rand_list[self.TEST_SZ - 1]
        self.assertEqual(self.lst.pop(), last_elem)
        
        
if __name__ == '__main__':
    unittest.main()