import unittest
from mergesort import iterative_mergesort as mergesort

class TestIterativeMergeSort(unittest.TestCase):
    def test_returnsEmptyListWhenGivenEmptyList(self):
        empty_list = []
        self.assertEqual(empty_list, mergesort(empty_list))

    def test_returnsUnchangedListWhenGivenSingleElementList(self):
        list_with_one_element = [1]
        self.assertEqual(list_with_one_element, mergesort(list_with_one_element))
