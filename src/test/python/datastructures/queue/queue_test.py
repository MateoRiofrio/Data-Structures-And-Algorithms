import unittest
from queue import Queue
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
        self.queue.push(3)
        self.assertFalse(self.queue.is_empty())

    def test_size(self):
        # empty and smallest non-empty queue
        self.assertEqual(self.queue.size(), 0)
        self.queue.push(5)
        self.assertEqual(self.queue.size(), 1)
        
        # higher bound size 
        for elem in range(self.TEST_SZ):
            self.queue.push(elem)
        self.assertEqual(self.queue.size(), self.TEST_SZ + 1)
    
    def test_pop(self):
        # test empty list
        self.assertIsNone(self.queue.pop())
        
        # smallest non empty list
        self.queue.push(2)
        self.assertEqual(self.queue.pop(), 2)

        # insert 50 random elements and test pop correctness
        rand_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        target_elem = rand_list[self.TEST_SZ - 1]
        for elem in rand_list:
            self.queue.push(elem)
        self.assertEqual(self.queue.pop(), target_elem)
    
    def test_poll(self):
        # test empty list
        self.assertIsNone(self.queue.poll())
        
        # smallest non-empty list
        self.queue.push(2)
        self.assertEqual(self.queue.poll(), 2)

        # insert 50 random elements and test poll correctness
        rand_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        target_elem = rand_list[0]
        for elem in rand_list:
            self.queue.push(elem)
        self.assertEqual(self.queue.poll(), target_elem)

    def test_push(self):
        self.queue.push(4)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.pop(), 4)    

if __name__ == '__main__':
    unittest.main()

