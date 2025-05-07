# from nagini_contracts.contracts import *

# @Pure
# def abs_value(x: int) -> int:
#     """Compute the absolute value of x"""
#     if x >= 0:
#         return x
#     else:
#         return -x

# @Pure
# def process_data_transformed(x: int) -> int:
#     """Process data with absolute value handling"""
#     Requires(x >= -50)
#     Requires(x <= 50)
    
#     # Multiply by 2
#     y = x * 2
    
#     # Get absolute value
#     z = abs_value(y)
    
#     return z

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
    Requires(x >= -1000)
    Requires(x <= 1000)
    Ensures(Result() == abs_value(x * 2))
    # The key property we want to verify:
    Ensures((x == 50) == (abs_value(x * 2) == 100))
    
    # Early assertion's boolean value (would be an assert in normal Python)
    early_check = (x == 50)
    
    # Multiply by 2
    y = x * 2
    
    # Get absolute value
    z = abs_value(y)
    
    # Final assertion's boolean value (would be an assert in normal Python)
    final_check = (z == 100)
    
    # In Nagini, we use the Ensures clause above instead of this assert
    # The Ensures clause states the property that early_check == final_check
    
    return z