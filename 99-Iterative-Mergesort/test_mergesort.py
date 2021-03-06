import unittest
from mergesort import iterative_mergesort as mergesort, merge_list

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

    def test_sortsListWithThreeElements(self):
        list_to_sort = [5, -1, 3]
        sorted_list = [-1, 3, 5]
        self.assertEqual(sorted_list, mergesort(list_to_sort))

    def test_sortsListWithFourElements(self):
        list_to_sort = [4, 1, -2, 3]
        sorted_list = [-2, 1, 3, 4]
        self.assertEqual(sorted_list, mergesort(list_to_sort))

    def test_sortsListWithFiveElements(self):
        list_to_sort = [5, -2, 4, 9, 16]
        sorted_list = [-2, 4, 5, 9, 16]
        self.assertEqual(sorted_list, mergesort(list_to_sort))


class TestMergeList(unittest.TestCase):
    def test_returnsEmptyListWhenGivenEmptyList(self):
        self.assertEqual([], merge_list([], 0, 0))

    def test_returnsUnchangedListWhenGivenSingleElementList(self):
        self.assertEqual([1], merge_list([1], 0, 1))

    def test_sortsListWithTwoPresortedListsOfLengthOne(self):
        list_to_sort = [4, 1]
        sorted_list = [1, 4]
        self.assertEqual(sorted_list, merge_list(list_to_sort, 0, 2))

    def test_sortsListWithTwoPresortedListsOfLengthTwo(self):
        list_to_sort = [1, 6] + [0, 7]
        sorted_list = [0, 1, 6, 7]
        self.assertEqual(sorted_list, merge_list(list_to_sort, 0, 4))

    def test_sortsListWithTwoPresortedListsOfLengthTwoAndOne(self):
        list_to_sort = [1, 6] + [0]
        sorted_list = [0, 1, 6]
        self.assertEqual(sorted_list, merge_list(list_to_sort, 0, 3))

    def test_sortsListWithTwoPresortedListsOfLengthThreeAndTwo(self):
        list_to_sort = [0, 1, 3] + [-1, 2]
        sorted_list = [-1 , 0, 1, 2, 3]
        self.assertEqual(sorted_list, merge_list(list_to_sort, 0, 5))

    def test_sortsListsWithSameLengthAndSameValues(self):
        list_to_sort = [0, 1, 3] + [-1, 0]
        sorted_list = [-1 , 0, 0, 1, 3]
        self.assertEqual(sorted_list, merge_list(list_to_sort, 0, 5))
