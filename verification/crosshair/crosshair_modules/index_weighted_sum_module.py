import math
import datetime


def index_weighted_sum_transformed(lst: list):
    '''
    pre: len(lst) <= 20
    pre: all(-100 <= x <= 100 for x in lst)
    post: (sum(i * val for i, val in enumerate(lst)) % 100 == 35) == (sum(i * val for i, val in enumerate(lst)) % 100 == 35)
    '''
    b_early = sum(i_early * val_early for i_early, val_early in enumerate(lst)) % 100 == 35
    
    weighted = 0
    for i_final, val_final in enumerate(lst):
        weighted += val_final * i_final
    result = weighted % 100
    b_final = (result == 35)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
