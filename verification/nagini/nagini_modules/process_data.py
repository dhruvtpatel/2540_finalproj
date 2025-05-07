from nagini_contracts.contracts import *

@Pure
def abs_value(x: int) -> int:
    """Compute the absolute value of x"""
    if x >= 0:
        return x
    else:
        return -x

@Pure
def process_data_transformed(x: int) -> int:
    """Process data with absolute value handling"""
    Requires(x >= -50)
    Requires(x <= 50)
    
    # Multiply by 2
    y = x * 2
    
    # Get absolute value
    z = abs_value(y)
    
    return z