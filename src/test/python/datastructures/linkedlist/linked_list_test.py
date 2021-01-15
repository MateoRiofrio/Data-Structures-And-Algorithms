import unittest
from linked_list import LinkedList
import random

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.lst = LinkedList()
        self.MAX_RAND_NUM = 250
        self.TEST_SZ = 50
        self.rand_elem = random.randrange(self.MAX_RAND_NUM)
        
    def test_size(self):
        # test empty linked list size method.
        self.assertEqual(self.lst.size(), 0)

        for i in range(self.TEST_SZ):
            self.lst.add(i)
        self.assertEqual(self.lst.size(), self.TEST_SZ)
    
    def test_is_empty(self):
        self.assertTrue(self.lst.is_empty())
        self.lst.add(random.randrange(self.MAX_RAND_NUM))
        self.assertFalse(self.lst.is_empty())

    def test_contains(self):
        # check false for empty list, true once element is added.
        self.assertFalse(self.lst.contains(self.rand_elem))
        self.lst.add(self.rand_elem)
        self.assertTrue(self.lst.contains(self.rand_elem))

    def test_peek(self):
        # assert None on empty list.
        self.assertIsNone(self.lst.peek())

        # assert correct item after adding multiple items.
        rand_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        last_item_added = rand_list[len(rand_list) - 1]
        for elem in rand_list:
            self.lst.add(elem)
        self.assertEqual(self.lst.peek(), last_item_added)

    def test_add(self):
        # add on empty list:
        self.lst.add(self.rand_elem)
        self.assertEqual(self.lst.peek(), self.rand_elem)
        self.assertEqual(self.lst.size(), 1)

        # add many items on non-empty list:
        rand_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        last_item_added = rand_list[len(rand_list) - 1]
        for elem in rand_list:
            self.lst.add(elem)
        self.assertEqual(self.lst.peek(), last_item_added)
        self.assertEqual(self.lst.size(), self.TEST_SZ + 1)

    def test_add_last(self):
        # add on empty list.
        self.lst.add_last(self.rand_elem)
        self.assertEqual(self.lst.peek(), self.rand_elem)

        # add many items non-empty list:
        rand_list = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        for elem in rand_list:
            self.lst.add_last(elem)
        self.assertEqual(self.lst.size(), self.TEST_SZ + 1)
        
    def test_remove(self):
        self.lst.add_last(self.rand_elem)
        self.lst.remove(self.rand_elem)
        self.assertFalse(self.lst.contains(self.rand_elem))
    
    def test_pop(self):
        self.lst.add(self.rand_elem)
        self.assertEqual(self.lst.pop(), self.rand_elem)
        self.assertEqual(self.lst.size(), 0 )
         
if __name__ == '__main__':
    unittest.main()