import math
import datetime


def ceiling_multiplier_transformed(x: int):
    '''
    pre: -1000 <= x <= 1000
    post: (x == 34) == (math.ceil(x * 1.5) + 4 == 55)
    '''
    b_early = (x == 34)
    import math
    val = x * 1.5
    rounded = math.ceil(val)
    adj = rounded + 4
    b_final = (adj == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adj
