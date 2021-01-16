import unittest
from src.main.python.datastructures.queue.queue import Queue
import random

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.TEST_SZ = 50
        self.MAX_RAND_NUM = 250
    
    def test_is_empty(self):
        # empty queue
        self.assertTrue(self.queue.is_empty())

        # smallest non-empty queue
        self.queue.enqueue(3)
        self.assertFalse(self.queue.is_empty())

    def test_size(self):
        # empty and smallest non-empty queue
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.size(), 1)
        
        # higher bound size 
        for elem in range(self.TEST_SZ):
            self.queue.enqueue(elem)
        self.assertEqual(self.queue.size(), self.TEST_SZ + 1)
    
    def test_dequeue(self):
        # test empty list
        self.assertIsNone(self.queue.dequeue())
        
        # smallest non empty list
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 2)

        # insert 50 random elements and test dequeue correctness
        rand_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        target_elem = rand_list[0]
        for elem in rand_list:
            self.queue.enqueue(elem)
        self.assertEqual(self.queue.dequeue(), target_elem)

    def test_enqueue(self):
        self.queue.enqueue(4)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.dequeue(), 4)  

        # insert 50 random elements and test pop correctness
        rand_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        for elem in rand_list:
            self.queue.enqueue(elem)
        self.assertEqual(self.queue.size(), self.TEST_SZ) 

if __name__ == '__main__':
    unittest.main()

