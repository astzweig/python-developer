from typing import Callable

def soundex(word: str) -> str:
    first_char = word[0]
    word = _remove_h_and_w(word)
    word = _replace_consonants_with_digit(word)
    word = _contract_consecutive_consonants(word)
    word = _remove_vowels(word)
    word = _add_or_replace_first_char(word, first_char)
    word = _zero_pad(word)
    word = _cut_after_four_chars(word)
    return word

def _cut_after_four_chars(word: str) -> str:
    return word[0:4]

def _add_or_replace_first_char(word: str, first_char: str) -> str:
    if _is_consonant(first_char):
        return first_char + word[1:]
    return first_char + word

def _remove_h_and_w(word: str) -> str:
    for char in 'hHwW':
        word = word.replace(char, '')
    return word

def _remove_vowels(word: str) -> str:
    def is_no_vowel(char, retained_chars):
        return not _is_vowel(char)
    return _filter_chars(word, is_no_vowel)

def _is_consonant(char: str) -> bool:
    is_no_vowel = not _is_vowel(char)
    is_no_h_or_w = char.lower() not in 'hw'
    return is_no_vowel and is_no_h_or_w

def _is_vowel(char: str) -> bool:
    return char.lower() in 'aeiouy'

def _contract_consecutive_consonants(word: str) -> str:
    def is_not_consecutive_char(char, retained_chars):
        return char != retained_chars[-1]
    return _filter_chars(word, is_not_consecutive_char)

def _filter_chars(word: str, callback: Callable[[str, str], bool]) -> str:
    retained_chars = ['']
    for char in word:
        if callback(char, retained_chars):
            retained_chars.append(char)
    return ''.join(retained_chars)

def _replace_consonants_with_digit(word: str) -> str:
    soundex_mapping = str.maketrans('bfpvcgjkqsxzdtlmnr', '111122222222334556')
    return word.lower().translate(soundex_mapping)

def _zero_pad(word: str) -> str:
    return word.ljust(4, '0')
