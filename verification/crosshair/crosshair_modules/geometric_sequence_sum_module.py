import math
import datetime


def geometric_sequence_sum_transformed(a: float, r: float, n: int):
    '''
    pre: -100 <= a <= 100
    pre: -2 <= r <= 2 # Ratio around 1 can be tricky
    pre: 0 <= n <= 10 # Sequence length
    post: (round(a * (1 - r**n) / (1 - r) if abs(r) < 1 and r != 1 else sum(a * r**i for i in range(n))) == 80) == (round( (a * (1 - r**n) / (1 - r) if abs(r) < 1 and r != 1 else sum(a * r**i for i in range(n))) ) == 80)
    '''
    sum_formula = a * (1 - r**n) / (1 - r) if abs(r) < 1 and r != 1 else sum(a * r**i for i in range(n))
    b_early = (round(sum_formula) == 80)
    
    if abs(r) < 1 and r != 1:
        total = a * (1 - r**n) / (1 - r)
    else:
        total = sum(a * r**i for i in range(n))
    
    rounded = round(total)
    b_final = (rounded == 80)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded
