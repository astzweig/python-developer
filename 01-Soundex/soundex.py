def soundex(word: str) -> str:
    word = _contract_consecutive_consonants(word)
    word = _replace_consonants_with_digit(word)
    word = _zero_pad(word)
    return word

def _contract_consecutive_consonants(word: str) -> str:
    remaining_chars = ['']
    for char in word:
        last_added_char = remaining_chars[-1]
        if last_added_char != char:
            remaining_chars.append(char)
    return ''.join(remaining_chars)

def _replace_consonants_with_digit(word: str) -> str:
    soundex_mapping = str.maketrans('bfpvcgjkqsxzdtlmnr', '111122222222334556')
    return word.translate(soundex_mapping)

def _zero_pad(word: str) -> str:
    return word.ljust(4, '0')
