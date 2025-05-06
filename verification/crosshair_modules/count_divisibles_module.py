import math
import datetime


def count_divisibles_transformed(nums: list):
    '''
    pre: len(nums) <= 20
    pre: all(-100 <= x <= 100 for x in nums)
    post: (len([n for n in nums if n % 4 == 0]) == 4) == (sum(1 for n in nums if n % 4 == 0) * 10 == 40)
    '''
    b_early = len([n for n in nums if n % 4 == 0]) == 4
    
    count = 0
    for n_val in nums:
        if n_val % 4 == 0:
            count += 1
    score = count * 10
    b_final = (score == 40)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return score
