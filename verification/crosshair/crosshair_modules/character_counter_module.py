import math
import datetime


def character_counter_transformed(text: str):
    '''
    pre: len(text) <= 100
    post: (sum(1 for ch in text if ch in "aeiouAEIOU") == 9) == (sum(1 for ch in text if ch in "aeiouAEIOU") * 3 == 27)
    '''
    b_early = sum(1 for ch_early in text if ch_early in "aeiouAEIOU") == 9
    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for ch_final in text:
        if ch_final in vowels:
            vowel_count += 1
    result = vowel_count * 3
    b_final = (result == 27)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
