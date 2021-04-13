from functools import cache

@cache
def edit_distance(word_a: str, word_b: str) -> int:
    word_a, word_b = _swap_values_if_word_b_is_longer(word_a, word_b)
    if _is_empty_word(word_b): return len(word_a)

    delete_char = _get_distance_if_char_is_deleted(word_a, word_b)
    retain_char = _get_distance_if_char_is_retained(word_a, word_b)
    add_char = _get_distance_if_char_is_added(word_a, word_b)
    return min(delete_char, retain_char, add_char)

def _get_distance_if_char_is_deleted(word_a: str, word_b: str) -> int:
    cost_of_deleting_one_char = 1
    remaining_costs = edit_distance(word_a[:-1], word_b)
    return cost_of_deleting_one_char + remaining_costs

def _get_distance_if_char_is_retained(word_a: str, word_b: str) -> int:
    is_same_character = word_a[-1] == word_b[-1]
    cost_of_retaining_one_char = 0 if is_same_character else 1
    remaining_costs = edit_distance(word_a[:-1], word_b[:-1])
    return cost_of_retaining_one_char + remaining_costs

def _get_distance_if_char_is_added(word_a: str, word_b: str) -> int:
    cost_of_adding_one_char = 1
    remaining_costs = edit_distance(word_a, word_b[:-1])
    return cost_of_adding_one_char + remaining_costs

def _is_empty_word(word: str) -> bool:
    return len(word) == 0

def _swap_values_if_word_b_is_longer(word_a: str, word_b: str) -> (str, str):
    if len(word_a) < len(word_b):
        return word_b, word_a
    return word_a, word_b
