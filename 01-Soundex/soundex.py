def soundex(word: str) -> str:
    word = _replace_consonants_with_digit(word)
    word = _zero_pad(word)
    return word

def _replace_consonants_with_digit(word: str) -> str:
    soundex_mapping = str.maketrans('bfpvcgjkqsxzdtlmnr', '111122222222334556')
    return word.translate(soundex_mapping)

def _zero_pad(word: str) -> str:
    return word.ljust(4, '0')
