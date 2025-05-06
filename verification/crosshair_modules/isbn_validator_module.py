import math
import datetime


def isbn_validator_transformed(isbn: str):
    '''
    pre: len(isbn) >= 10 and len(isbn) <= 17 # ISBN-10 or ISBN-13 with/without hyphens
    pre: all(c in "0123456789" for c in [char for char in isbn if char.isdigit()]) # Ensure characters that pass isdigit() are actual ASCII digits
    post: ( (lambda digits: len(digits) == 10 and sum((10 - i) * digit for i, digit in enumerate(digits)) % 11 == 0)([int(c) for c in isbn if c.isdigit()]) ) == ( (lambda d: 90 if (len(d) == 10 and sum((10 - i) * val for i, val in enumerate(d)) % 11 == 0) else 0)([int(c) for c in isbn if c.isdigit()]) == 90)
    '''
    digits_early = [int(c_early) for c_early in isbn if c_early.isdigit()]
    b_early = (len(digits_early) == 10 and sum((10 - i_early) * digit_early for i_early, digit_early in enumerate(digits_early)) % 11 == 0)
    
    digits_final = [int(c_final) for c_final in isbn if c_final.isdigit()]
    
    if len(digits_final) == 10:
        check_sum_final = sum((10 - i_final) * digit_final for i_final, digit_final in enumerate(digits_final))
        is_valid_final = check_sum_final % 11 == 0
    else:
        is_valid_final = False
        
    result = 90 if is_valid_final else 0
    b_final = (result == 90)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
