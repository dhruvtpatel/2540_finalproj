import math
import datetime


def string_reversal_checker_transformed(text: str):
    '''
    pre: len(text) <= 50 # Allow longer strings
    post: (text == text[::-1]) == ((75 if text == text[::-1] else 75 - abs(len(text) - len(text[::-1].strip()))) == 75)
    '''
    b_early = (text == text[::-1])
    reversed_text = text[::-1]
    length_diff = abs(len(text) - len(reversed_text.strip()))
    code = 75 if text == reversed_text else 75 - length_diff
    b_final = (code == 75)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return code
