import math
import datetime


def nested_loop_checker_transformed(limit: int):
    '''
    pre: 0 <= limit <= 50 # Increased limit
    post: ((limit * (limit - 1) // 2) % 200 == 36) == (( (lambda l: sum(1 for i in range(l) for j in range(i)))(limit) ) % 200 == 36)
    '''
    b_early = (limit * (limit - 1) // 2) % 200 == 36
    
    counter = 0
    for i in range(limit):
        for j in range(i):
            counter += 1
    final = counter % 200
    b_final = (final == 36)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
