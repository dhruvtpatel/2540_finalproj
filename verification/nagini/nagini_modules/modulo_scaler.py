from nagini_contracts.contracts import *

float_encoding = False

@Pure
def calculate_operation(x: int) -> int:
    """Calculate (x % 6) * 7 + 3"""
    # Only use integer operations 
    return (x % 6) * 7 + 3

@Pure
def verify_operation(x: int) -> bool:
    """Verify that (x % 6) * 7 + 3 == 30"""
    return calculate_operation(x) == 30

def modulo_scaler_transformed(x: int) -> int:
    """Transform x using a modulo-based calculation if it meets a specific condition.
    
    If (x % 6) * 7 + 3 == 30, the function multiplies x by 3 and adds 5.
    Otherwise, it returns x directly.
    """
    # Check if x satisfies the required condition: (x % 6) * 7 + 3 == 30
    Requires(verify_operation(x))
    
    # Calculate the result using integer operations only
    result = x * 3 + 5
    
    return result