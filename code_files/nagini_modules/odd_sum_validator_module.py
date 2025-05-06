from typing import List

def odd_sum_validator_transformed(lst: List[int]) -> int:
    '''
    pre: len(lst) > 0  # List must not be empty
    pre: len(lst) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 10 for x in lst)  # Add reasonable element bounds
    post: __return__ == mod
    post: mod == total % 100
    '''
    # Calculate early condition without generator expression
    early_sum: int = 0
    for n in lst:
        if n % 2 == 1:  # Check if odd
            early_sum += n
    
    b_early: bool = early_sum % 100 == 33
    
    # Calculate the actual result without list comprehension
    total: int = 0
    for n in lst:
        if n % 2 == 1:  # Check if odd
            total += n
    
    mod: int = total % 100
    b_final: bool = (mod == 33)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return mod 