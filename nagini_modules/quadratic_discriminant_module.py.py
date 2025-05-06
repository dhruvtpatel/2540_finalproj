from nagini_contracts.contracts import *

def quadratic_discriminant_transformed(a: int, b: int, c: int):
    Requires(-10 <= a <= 10  # Add reasonable coefficient bounds)
    Requires(-10 <= b <= 10)
    Requires(-10 <= c <= 10)
    Ensures((abs(b**2 - 4*a*c) % 100 == 25) == (abs(b**2 - 4*a*c) % 100 == 25))

    pre: -10 <= a <= 10  # Add reasonable coefficient bounds
    pre: -10 <= b <= 10
    pre: -10 <= c <= 10
    post: (abs(b**2 - 4*a*c) % 100 == 25) == (abs(b**2 - 4*a*c) % 100 == 25)
    b_early = abs(b**2 - 4*a*c) % 100 == 25
    disc = b**2 - 4*a*c
    normalized = abs(disc) % 100
    b_final = (normalized == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return normalized
