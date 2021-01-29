import unittest
from src.main.python.datastructures.heap.min_heap import MinHeap
import random

class TestMinHeap(unittest.TestCase):

    def setUp(self):
        self.heap = MinHeap()
        self.TEST_SZ = 50
        self.MAX_RAND_NUM = 250
    
    def tearDown(self):
        self.heap.clear()
    
    def test_is_empty(self):
        self.assertTrue(self.heap.is_empty())

        self.heap.insert(4)
        self.assertFalse(self.heap.is_empty())
        
        for elem in range(self.TEST_SZ):
            self.heap.insert(elem)
        self.assertFalse(self.heap.is_empty())
        
    def test_size(self):
        self.assertEqual(self.heap.size(), 0)

        self.heap.insert(1)
        self.assertEqual(self.heap.size(), 1)

        for elem in range(self.TEST_SZ):
            self.heap.insert(elem)
        self.assertEqual(self.heap.size(), self.TEST_SZ + 1)
    
    def test_clear(self):
        for elem in range(self.TEST_SZ):
            self.heap.insert(elem)
        
        self.heap.clear()
        self.assertTrue(self.heap.is_empty())
    
    def test_insert(self):
        self.heap.insert(4)
        self.assertEqual(self.heap.size(), 1)
    
    def test_find_min_smoke_cases(self):
        # assert None on empty heap
        self.assertIsNone(self.heap.find_min())

        # assert equal on smallest non-empty heap
        self.heap.insert(-10)
        self.assertEqual(self.heap.find_min(), -10)

    def test_find_min_first_middle_last(self):
        test_first = [12 , 43, 54 , 29, 13]
        test_middle = [87 , 34, 0 , 27, 88]
        test_last = [76, 23, 54, 72, 2, 1]

        for elem in test_first:
            self.heap.insert(elem)
        self.assertEqual(self.heap.find_min(), 12)
        self.heap.clear()

        for elem in test_middle:
            self.heap.insert(elem)
        self.assertEqual(self.heap.find_min(), 0)
        self.heap.clear()

        for elem in test_last:
            self.heap.insert(elem)
        self.assertEqual(self.heap.find_min(), 1)
        
    def test_find_min_rand(self):
        # test on random list of 50 items.
        rand_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        for elem in rand_list:
            self.heap.insert(elem)
        
        min_item = min(rand_list)
        self.assertEqual(self.heap.find_min(), min_item)

if __name__ == '__main__':
    unittest.main()