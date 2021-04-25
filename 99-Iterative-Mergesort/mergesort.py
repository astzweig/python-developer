def iterative_mergesort(lst: list[int]) -> list[int]:
    if len(lst) > 1:
        a, b = tuple(lst)
        if (a > b):
            return [b, a]
    return lst
