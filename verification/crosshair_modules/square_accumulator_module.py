import math
import datetime


def square_accumulator_transformed(x: int):
    '''
    pre: 0 <= x <= 50 # Increased range for x
    post: (sum(i * i for i in range(x)) % 100 == 55) == (sum(i * i for i in range(x)) % 100 == 55)
    '''
    b_early = sum(i_early * i_early for i_early in range(x)) % 100 == 55
    
    acc = 0
    for i_final in range(x):
        acc += i_final * i_final
    final = acc % 100
    b_final = (final == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
