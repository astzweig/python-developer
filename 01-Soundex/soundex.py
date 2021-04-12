def soundex(word: str) -> str:
    return _zero_pad(word)

def _zero_pad(word: str) -> str:
    return word + '000'
