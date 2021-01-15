import unittest
from stack import Stack
import random

class TestStacK(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.MAX_RAND_NUM = 250
        self.TEST_SZ = 50
    
    def tearDown(self):
        for _ in range(self.stack.size()):
            while self.stack.size() !=0:
                self.stack.pop()

    def test_size(self):
        # test empty stack size method
        self.assertEqual(self.stack.size(), 0)

        # test random size
        rand_range = random.randrange(self.TEST_SZ)
        for i in range(rand_range):
            self.stack.push(i)
        self.assertEqual(self.stack.size(), rand_range)
    
    def test_push(self):
        self.stack.push(random.randrange(self.MAX_RAND_NUM))
        self.assertEqual(self.stack.size(), 1)
    
    def test_pop(self):
        # add a random number
        elem = random.randrange(self.MAX_RAND_NUM)
        self.stack.push(elem)

        # test correct element returned and smaller size        
        self.assertEqual(elem, self.stack.pop())
        self.assertEqual(self.stack.size(), 0)
    
    def test_reverse_array(self):
        # use python's reversed method to check correctness 
        random_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        reversed_list = [i for i in reversed(random_list)]
        self.assertEqual(self.stack.reverse_array(random_list), reversed_list)

if __name__ == '__main__':
    unittest.main()