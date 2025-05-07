from nagini_contracts.contracts import *

@Pure
def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate the discriminant b^2 - 4ac"""
    return b * b - 4 * a * c

@Pure
def normalize_value(value: int) -> int:
    """Calculate abs(value) % 100"""
    if value >= 0:
        return value % 100
    else:
        return (-value) % 100

def quadratic_discriminant_transformed(a: int, b: int, c: int) -> int:
    """Calculate the normalized discriminant of a quadratic equation"""
    Requires(True)
    
    # Calculate the discriminant
    disc = calculate_discriminant(a, b, c)
    
    # Normalize the result
    normalized = normalize_value(disc)
    
    return normalized
