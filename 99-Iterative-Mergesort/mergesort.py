from math import ceil

def iterative_mergesort(lst: list[int]) -> list[int]:
    for step_size in get_doubled_number_up_to(2 * len(lst), starting_at = 2):
        partials = []
        for start, end in walk_list_in_steps(len(lst), step_size):
            sorted_partial_list = merge_list(lst, start, end)
            partials.extend(sorted_partial_list)
        lst = partials
    return lst

def get_doubled_number_up_to(n, starting_at):
    step_size = starting_at
    while step_size <= n:
        yield step_size
        step_size *= 2

def walk_list_in_steps(n: int, step_size):
    for start in range(0, n, step_size):
        end = start + step_size
        if end > n:
            end = n
        yield start, end


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
