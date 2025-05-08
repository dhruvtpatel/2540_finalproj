import math
import datetime


def string_pattern_score_transformed(s: str):
    '''
    pre: len(s) > 0
    pre: len(s) <= 20 # Increased bounds for wider testing range
    post: (sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25) == (sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25)
    '''
    b_early = sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25
    score = sum(1 for c in s if c in 'aeiouAEIOU')
    result = score * 5
    b_final = (result == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
