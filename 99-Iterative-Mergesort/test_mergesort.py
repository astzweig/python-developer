import unittest
from mergesort import iterative_mergesort as mergesort

class TestIterativeMergeSort(unittest.TestCase):
    def test_returnsEmptyListWhenGivenEmptyList(self):
        empty_list = []
        self.assertEqual(empty_list, mergesort(empty_list))

    def test_returnsUnchangedListWhenGivenSingleElementList(self):
        list_with_one_element = [1]
        self.assertEqual(list_with_one_element, mergesort(list_with_one_element))

    def test_sortsListWithTwoElements(self):
        list_to_sort = [4, 1]
        sorted_list = [1, 4]
        self.assertEqual(sorted_list, mergesort(list_to_sort))
