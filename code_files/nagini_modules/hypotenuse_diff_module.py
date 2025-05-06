import math

def hypotenuse_diff_transformed(a: float, b: float) -> int:
    '''
    pre: 0 <= a <= 10  # Add reasonable side length bounds
    pre: 0 <= b <= 10
    post: (abs(int(math.sqrt(a**2 + b**2) + 0.5) - int(a) - int(b)) == 3) == b_early
    '''
    # Calculate using Pythagoras theorem and manual rounding
    b_early: bool = abs(int(math.sqrt(a**2 + b**2) + 0.5) - int(a) - int(b)) == 3
    
    # Calculate hypotenuse manually
    hyp: float = math.sqrt(a**2 + b**2)
    rounded: int = int(hyp + 0.5)  # Manual rounding
    diff: int = abs(rounded - int(a) - int(b))
    
    b_final: bool = (diff == 3)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return diff 