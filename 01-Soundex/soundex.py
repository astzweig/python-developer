def soundex(word: str) -> str:
    word = _remove_h_and_w(word)
    word = _contract_consecutive_consonants(word)
    word = _replace_consonants_with_digit(word)
    word = _remove_vowels(word)
    word = _zero_pad(word)
    return word

def _remove_h_and_w(word: str) -> str:
    return word.replace('h', '').replace('w', '')

def _remove_vowels(word: str) -> str:
    remaining_chars = ['']
    for char in word:
        if not _is_vowel(char):
            remaining_chars.append(char)
    return ''.join(remaining_chars)

def _is_vowel(char: str) -> bool:
    return char in 'aeiouy'

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
