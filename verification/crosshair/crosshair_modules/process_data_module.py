import math
import datetime


def process_data_transformed(x: int):
    '''
    pre: -1000 <= x <= 1000
    post: (x == 50) == (abs(x * 2) == 100)
    '''
    b_early = (x == 50)
    y = x * 2
    z = abs(y)
    b_final = (z == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return z
