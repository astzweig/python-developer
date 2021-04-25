from math import ceil

def iterative_mergesort(lst: list[int]) -> list[int]:
    for index in range(0, len(lst), 1):
        pass

    for index in range(0, len(lst), 2):
        length_list = 2
        merge_list(lst[index:index + length_list])

    for index in range(0, len(lst), 4):
        length_list = 4
        merge_list(lst[index:index + length_list])
    return lst

def merge_list(lst: list[int], left: int, right: int):
    return lst
