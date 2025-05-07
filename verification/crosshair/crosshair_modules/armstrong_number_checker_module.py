import math
import datetime


def armstrong_number_checker_transformed(n: int):
    '''
    pre: 0 <= n <= 10000 # Check a range of numbers
    post: (sum(int(d) ** len(str(n)) for d in str(n)) == n if n >=0 else False) == ((81 if sum(int(d) ** len(str(n)) for d in str(n)) == n else 0) == 81 if n >= 0 else False)
    '''
    if n < 0: # Armstrong numbers are non-negative
        b_early = False
        b_final = False
        assert b_early == b_final
        return 0

    digits_early = [int(d_early) for d_early in str(n)]
    power_early = len(digits_early)
    b_early = (sum(digit_early ** power_early for digit_early in digits_early) == n)
    
    digits_final = [int(d_final) for d_final in str(n)]
    power_final = len(digits_final)
    total_final = sum(digit_final ** power_final for digit_final in digits_final)
    is_armstrong_final = total_final == n
    result = 81 if is_armstrong_final else 0
    b_final = (result == 81)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
