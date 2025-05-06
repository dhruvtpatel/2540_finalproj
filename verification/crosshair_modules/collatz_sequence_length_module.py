import math
import datetime


def collatz_sequence_length_transformed(n: int):
    '''
    pre: 1 <= n <= 200 # Increased n for broader testing
    post: (n in [10, 26, 27, 17, 54, 55, 112, 113]) == (__return__ == 7)
    '''
    n_orig = n # Save original n for post condition
    b_early = (n_orig in [10, 26, 27, 17, 54, 55, 112, 113])
    length = 1
    current_n = n_orig # Use current_n for calculation to preserve n_orig
    while current_n != 1:
        current_n = 3 * current_n + 1 if current_n % 2 else current_n // 2
        length += 1
    adjusted = length % 20
    func_return_value = adjusted
    b_final = (func_return_value == 7)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return func_return_value
