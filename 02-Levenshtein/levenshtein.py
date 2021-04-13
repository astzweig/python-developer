def edit_distance(word_a: str, word_b: str) -> int:
    word_a, word_b = _swap_values_if_word_a_is_longer(word_a, word_b)
    if (len(word_b) == 0): return len(word_a)
    return _return_amount_of_different_chars(word_a, word_b)

def _swap_values_if_word_a_is_longer(word_a: str, word_b: str) -> (str, str):
    if len(word_a) > len(word_b):
        return word_b, word_a
    return word_a, word_b

def _return_amount_of_different_chars(word_a: str, word_b: str) -> int:
    distance = len(word_b) - len(word_a)
    for char_a, char_b in zip(word_a, word_b):
        if char_a != char_b:
            distance += 1
    return distance
