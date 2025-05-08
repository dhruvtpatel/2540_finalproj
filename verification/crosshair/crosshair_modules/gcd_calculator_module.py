import math
import datetime


def gcd_calculator_transformed(a: int, b: int):
    '''
    pre: 0 <= a <= 1000 # Allow non-negative inputs
    pre: 0 <= b <= 1000
    post: (math.gcd(a, b) == 8) == (math.gcd(a,b) * 5 == 40)
    '''
    b_early = (math.gcd(a, b) == 8)
    temp_a = a
    temp_b = b
    while temp_b:
        temp_a, temp_b = temp_b, temp_a % temp_b
    gcd_val = temp_a
    result = gcd_val * 5
    b_final = (result == 40)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
