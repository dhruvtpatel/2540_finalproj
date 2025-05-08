import math
import datetime


def digit_sum_processor_transformed(x: int):
    '''
    pre: -10000 <= x <= 10000
    post: (x == 199) == ((sum(int(d) for d in str(abs(x))) + len(str(abs(x)))) * 2 == 44)
    '''
    b_early = (x == 199)
    digits = [int(d) for d in str(abs(x))]
    total = sum(digits)
    adjusted = total + len(digits)
    result = adjusted * 2
    b_final = (result == 44)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
