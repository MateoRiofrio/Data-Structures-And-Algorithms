import unittest
from doubly_linked_list import DoublyLinkedList
import random

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.lst = DoublyLinkedList()
        self.MAX_RAND_NUM = 250
        self.TEST_SZ = 50
        self.rand_elem = random.randrange(self.MAX_RAND_NUM)
        
    def test_size(self):
        # test empty linked list size method
        self.assertEqual(self.lst.size(), 0)

        for i in range(self.TEST_SZ):
            self.lst.add(i)
        self.assertEqual(self.lst.size(), self.TEST_SZ)
    
    def test_is_empty(self):
        self.assertTrue(self.lst.is_empty())
        self.lst.add(random.randrange(self.MAX_RAND_NUM))
        self.assertFalse(self.lst.is_empty())
        
if __name__ == '__main__':
    unittest.main()