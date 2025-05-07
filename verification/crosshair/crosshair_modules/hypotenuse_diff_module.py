import math
import datetime


def hypotenuse_diff_transformed(a: float, b: float):
    '''
    pre: 0 <= a <= 100 # Increased bounds for wider testing range
    pre: 0 <= b <= 100
    post: (abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3) == (abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3)
    '''
    b_early = abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3
    hyp = math.hypot(a, b)
    rounded = round(hyp)
    diff = abs(rounded - int(a) - int(b))
    b_final = (diff == 3)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return diff
