def edit_distance(word_a: str, word_b: str) -> int:
    if (len(word_b) == 0): return len(word_a)
    if (word_a != word_b): return 1
    return 0
