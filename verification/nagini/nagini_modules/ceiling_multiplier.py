from nagini_contracts.contracts import *

@Pure
def custom_ceiling(value: float) -> int:
    """Implement a custom ceiling function without using math.ceil"""
    int_value = int(value)
    if int_value < value:
        return int_value + 1
    return int_value

@Pure
def ceiling_multiplier_transformed(x: int) -> int:
    """Transform x by multiplying by 1.5, taking ceiling, and adding 4"""
    Requires(x == 34)  # Precondition matching the original early assertion
    Ensures(Result() == 55)  # Matches the final assertion
    
    val = x * 1.5  # This is 51.0 when x is 34
    rounded = custom_ceiling(val)  # This is 51 when val is 51.0
    result = rounded + 4  # This is 55 when rounded is 51
    
    return result
