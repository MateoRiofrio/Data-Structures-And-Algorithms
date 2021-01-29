import unittest
from binary_search import BinarySearch
import random, math

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.bs = BinarySearch()
        self.MAX_RAND_NUM = 50000
        self.TEST_SZ = 50
        self.PERF_TEST_SZ = 10000
    
    def test_search_on_empty(self):
        empty_arr = []
        self.assertEqual(self.bs.search(empty_arr, 51), -1)
    
    def test_with_a_chosen_number(self):
        arr_with_22 = [2, 33, 45, 51, 888, 1003]
        self.assertEqual(self.bs.search(arr_with_22, 51), 3)
        self.assertEqual(self.bs.search(arr_with_22, 52), -1)
    
    def test_smallest_non_empty(self):
        smallest_non_empty_arr = [51]
        self.assertEqual(self.bs.search(smallest_non_empty_arr, 51), 0)
        self.assertEqual(self.bs.search(smallest_non_empty_arr, 52), -1)

    def test_boundary_locations(self):
        test_arr = [11, 21, 42, 51, 68, 100]
        self.assertEqual(self.bs.search(test_arr, 11), 0)
        self.assertEqual(self.bs.search(test_arr, 51), 3)
        self.assertEqual(self.bs.search(test_arr, 100), 5)
    
    def test_rand_arr_no_duplicates(self):
        rand_arr = random.sample(range(self.MAX_RAND_NUM), self.TEST_SZ)
        rand_arr.sort()
        rand_index = random.randrange(self.TEST_SZ)
        target = rand_arr[rand_index]
        self.assertEqual(self.bs.search(rand_arr, target), rand_index)
    
    def test_performance_with_count_of_iterations(self):
        rand_arr2 = random.sample(range(self.MAX_RAND_NUM), self.PERF_TEST_SZ)
        rand_arr2.sort()
        rand_index = random.randrange(self.PERF_TEST_SZ)
        target = rand_arr2[rand_index]

        performance = self.bs.search(rand_arr2, target, True)
        self.assertTrue(performance <= (1 + math.log2(len(rand_arr2))))
    
if __name__ == '__main__':
    unittest.main()