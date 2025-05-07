import math
import datetime


def rolling_maximum_transformed(values: list):
    '''
    pre: len(values) > 0 # Must not be empty
    pre: len(values) <= 20
    pre: all(-1000 <= x <= 1000 for x in values)
    post: (max(values) == 89 if values else False) == ((max(values) if values else -float('inf')) + 10 == 99)
    '''
    b_early = (max(values) == 89 if values else False) # Added if values else False for safety
    
    max_val = -float('inf') # Ensure proper init for max
    if values: # Check if list is not empty
        for v_val in values:
            if v_val > max_val:
                max_val = v_val
    final = max_val + 10 if values else -float('inf') + 10 # Handle empty list for final calc
    b_final = (final == 99)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
