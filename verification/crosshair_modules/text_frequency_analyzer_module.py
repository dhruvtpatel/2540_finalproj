import math
import datetime


def text_frequency_analyzer_transformed(text: str):
    '''
    pre: len(text) <= 100 # Allow longer texts
    post: (any(text.lower().count(c) == 6 for c in set(text.lower()) if text)) == (max([text.lower().count(c) for c in set(text.lower()) if c.isalpha()] or [0]) * 2 == 12 if text else 0 == 12)
    '''
    b_early = any(text.lower().count(c) == 6 for c in set(text.lower()))
    if not text:
        return 0
    char_freq: dict[str, int] = {}
    for char in text:
        if char.isalpha():
            char_freq[char.lower()] = char_freq.get(char.lower(), 0) + 1
    most_common = max(char_freq.values()) if char_freq else 0
    result = most_common * 2
    b_final = (result == 12)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
