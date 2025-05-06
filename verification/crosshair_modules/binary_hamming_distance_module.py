import math
import datetime


def binary_hamming_distance_transformed(a: int, b: int):
    '''
    pre: 0 <= a <= 1000 # Wider range for integers
    pre: 0 <= b <= 1000
    post: (bin(a ^ b).count('1') == 4) == ( (lambda val_a, val_b: sum(1 for bit_a, bit_b in zip(bin(val_a)[2:].zfill(max(len(bin(val_a)[2:]), len(bin(val_b)[2:]))), bin(val_b)[2:].zfill(max(len(bin(val_a)[2:]), len(bin(val_b)[2:])))) if bit_a != bit_b) * 8)(a,b) == 32)
    '''
    b_early = (bin(a ^ b).count('1') == 4)
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    
    max_len = max(len(bin_a), len(bin_b))
    bin_a = bin_a.zfill(max_len)
    bin_b = bin_b.zfill(max_len)
    
    distance = sum(1 for bit_a_val, bit_b_val in zip(bin_a, bin_b) if bit_a_val != bit_b_val)
    result = distance * 8
    b_final = (result == 32)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
