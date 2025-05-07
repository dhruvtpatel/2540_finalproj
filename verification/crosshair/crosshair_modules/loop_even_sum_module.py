import math
import datetime


def loop_even_sum_transformed(start: int, end: int):
    '''
    pre: -50 <= start <= 50 # Wider range
    pre: -50 <= end <= 50
    pre: start <= end # Ensure start is not greater than end
    post: (sum(i for i in range(start, end + 1) if i % 2 == 0) == 220) == (sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110)
    '''
    b_early = sum(i_early for i_early in range(start, end + 1) if i_early % 2 == 0) == 220
    
    total = 0
    for i_final in range(start, end + 1):
        if i_final % 2 == 0:
            total += i_final
    final = total // 2
    b_final = (final == 110)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
