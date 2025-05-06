import math
import datetime


def vector_norm_transformed(x: float, y: float):
    '''
    pre: -100 <= x <= 100 # Increased bounds for wider testing range
    pre: -100 <= y <= 100
    post: (round(math.sqrt(x**2 + y**2)) == 10) == (round(math.sqrt(x**2 + y**2)) == 10)
    '''
    b_early = round(math.sqrt(x**2 + y**2)) == 10
    norm = math.sqrt(x**2 + y**2)
    rounded = round(norm)
    b_final = (rounded == 10)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded
