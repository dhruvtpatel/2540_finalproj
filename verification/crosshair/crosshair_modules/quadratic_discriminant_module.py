import math
import datetime


def quadratic_discriminant_transformed(a: int, b: int, c: int):
    '''
    pre: -100 <= a <= 100 # Increased bounds for wider testing range
    pre: -100 <= b <= 100
    pre: -100 <= c <= 100
    post: (abs(b**2 - 4*a*c) % 100 == 25) == (abs(b**2 - 4*a*c) % 100 == 25)
    '''
    b_early = abs(b**2 - 4*a*c) % 100 == 25
    disc = b**2 - 4*a*c
    normalized = abs(disc) % 100
    b_final = (normalized == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return normalized
