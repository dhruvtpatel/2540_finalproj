import math
import datetime


def hexadecimal_converter_transformed(num: int):
    '''
    pre: 0 <= num <= 10000 # Non-negative numbers
    post: (sum(int(c, 16) for c in hex(num)[2:]) + len(hex(num)[2:]) == 24) == (sum(int(c, 16) for c in hex(num)[2:]) + len(hex(num)[2:]) == 24)
    '''
    hex_digits_sum_early = 0
    for c in hex(num)[2:]:
        hex_digits_sum_early += int(c, 16)
    b_early = (hex_digits_sum_early + len(hex(num)[2:]) == 24)
    hex_value = hex(num)[2:]
    digit_sum = sum(int(c, 16) for c in hex_value)
    result = digit_sum + len(hex_value)
    b_final = (result == 24)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
