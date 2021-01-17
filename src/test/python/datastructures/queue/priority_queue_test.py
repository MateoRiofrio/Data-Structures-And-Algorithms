import unittest
from src.main.python.datastructures.queue.priority_queue import MinPriorityQueue
import random

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = MinPriorityQueue()
        self.TEST_SZ = 50
        self.MAX_RAND_NUM = 250
    
    def tearDown(self):
        self.pq.clear()
    
    def test_is_empty(self):
        self.assertTrue(self.pq.is_empty())
        self.pq.insert(5)
        self.assertFalse(self.pq.is_empty())

    def test_size(self):
        self.assertEqual(self.pq.size(), 0)
        self.pq.insert(3)
        self.assertEqual(self.pq.size(), 1)

        for elem in range(self.TEST_SZ):
            self.pq.insert(elem)
        
        self.assertEqual(self.pq.size(), self.TEST_SZ + 1)
    
    def test_insert(self):
        self.pq.insert(3)
        self.assertEqual(self.pq.size(), 1)
    
    def test_min(self):
        lst = [3, 2, 64, 73, 1, 54]
        for elem in lst:
            self.pq.insert(elem)

        self.assertEqual(self.pq.min(), 1)
    
    def test_min_rand(self):
        rand_lst = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        for elem in rand_lst:
            self.pq.insert(elem)
        min_elem = min(rand_lst)

        self.assertEqual(self.pq.min(), min_elem)

if __name__ == '__main__':
    unittest.main()
