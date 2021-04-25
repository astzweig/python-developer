from math import ceil

def iterative_mergesort(lst: list[int]) -> list[int]:
    step_size = 2
    while step_size <= len(lst):
        result = []
        for index in range(0, len(lst), step_size):
            second_index = index + step_size
            if second_index > len(lst):
                second_index = len(lst)
            result.extend(merge_list(lst, index, second_index))
        lst = result
        step_size *= 2
    return lst

def merge_list(lst: list[int], left: int, right: int):
    mid = ceil((right - left) / 2) + left
    left_idx = left
    right_idx = mid
    result = []

    while True:
        if left_idx >= mid or right_idx >= right:
            break
        if lst[left_idx] > lst[right_idx]:
            result.append(lst[right_idx])
            right_idx += 1
        else:
            result.append(lst[left_idx])
            left_idx += 1

    while left_idx < mid:
        result.append(lst[left_idx])
        left_idx += 1

    while right_idx < right:
        result.append(lst[right_idx])
        right_idx += 1
    return result
