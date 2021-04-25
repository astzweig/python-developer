import unittest
from mergesort import iterative_mergesort as mergesort, merge_list

class TestIterativeMergeSort(unittest.TestCase):
    @unittest.skip("Implement merge_list first.")
    def test_returnsEmptyListWhenGivenEmptyList(self):
        empty_list = []
        self.assertEqual(empty_list, mergesort(empty_list))

    @unittest.skip("Implement merge_list first.")
    def test_returnsUnchangedListWhenGivenSingleElementList(self):
        list_with_one_element = [1]
        self.assertEqual(list_with_one_element, mergesort(list_with_one_element))

    @unittest.skip("Implement merge_list first.")
    def test_sortsListWithTwoElements(self):
        list_to_sort = [4, 1]
        sorted_list = [1, 4]
        self.assertEqual(sorted_list, mergesort(list_to_sort))

    @unittest.skip("Implement merge_list first.")
    def test_sortsListWithFourElements(self):
        list_to_sort = [4, 1, -2, 3]
        sorted_list = [-2, 1, 3, 4]
        self.assertEqual(sorted_list, mergesort(list_to_sort))


class TestMergeList(unittest.TestCase):
    def test_returnsEmptyListWhenGivenEmptyList(self):
        self.assertEqual([], merge_list([], 0, 0))
