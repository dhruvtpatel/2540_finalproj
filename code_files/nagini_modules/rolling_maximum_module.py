from typing import List

def rolling_maximum_transformed(values: List[int]) -> int:
    '''
    pre: len(values) > 0  # List must not be empty
    pre: len(values) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 100 for x in values)  # Add reasonable element bounds
    post: __return__ == final
    post: final == max_val + 10
    '''
    # Manual implementation of max without using the built-in max
    early_max: int = values[0]
    for val in values:
        if val > early_max:
            early_max = val
    
    b_early: bool = early_max + 10 == 99
    
    # Now do the actual calculation
    max_val: int = values[0]  # Initialize with first element instead of -infinity
    for v in values:
        if v > max_val:
            max_val = v
            
    final: int = max_val + 10
    b_final: bool = (final == 99)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final 