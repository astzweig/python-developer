def edit_distance(word_a: str, word_b: str) -> int:
    if (len(word_b) == 0): return len(word_a)
    return _return_amount_of_different_chars(word_a, word_b)

def _return_amount_of_different_chars(word_a: str, word_b: str) -> int:
    distance = len(word_b) - len(word_a)
    for char_a, char_b in zip(word_a, word_b):
        if char_a != char_b:
            distance += 1
    return distance
