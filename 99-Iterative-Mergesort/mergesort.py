from math import ceil

def iterative_mergesort(lst: list[int]) -> list[int]:
    for step_size in get_doubled_number_up_to(2 * len(lst), starting_at = 2):
        partials = []
        for start, end in walk_list_in_steps(len(lst), step_size):
            sorted_partial_list = merge_list(lst, start, end)
            partials.extend(sorted_partial_list)
        lst = partials
    return lst

def merge_list(lst: list[int], left: int, right: int):
    result = []
    mid = ceil((right - left) / 2) + left
    indices = [left, mid]
    indices_max = [mid, right]

    while True:
        if is_any_indice_maxed(indices, indices_max):
            break
        append_lower_number_and_advance_index(result, lst, indices)

    append_remaining_elements(result, lst, indices, indices_max)
    return result

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

def append_lower_number_and_advance_index(result: list[int], lst: list[int], indices: list[int]):
    lowest_number = None
    index_to_advance = 0
    for idx_num, idx in enumerate(indices):
        if lowest_number is None or lst[idx] < lowest_number:
            lowest_number = lst[idx]
            index_to_advance = idx_num

    indices[index_to_advance] += 1
    result.append(lowest_number)

def append_remaining_elements(result: list[int], lst: list[int], indices: list[int], maxed: list[int]):
    assert len(indices) == len(maxed)
    for idx, max_value in zip(indices, maxed):
        while idx < max_value:
            result.append(lst[idx])
            idx += 1

def is_any_indice_maxed(indices: list[int], maxed: list[int]) -> bool:
    assert len(indices) == len(maxed)
    for idx, maxed in zip(indices, maxed):
        if idx >= maxed:
            return True
    return False
