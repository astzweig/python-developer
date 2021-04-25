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
    mid = (right - left) // 2
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
