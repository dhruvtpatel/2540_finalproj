import math

def vector_norm_transformed(x: float, y: float) -> int:
    '''
    pre: -10 <= x <= 10  # Add reasonable vector component bounds
    pre: -10 <= y <= 10
    post: (int(math.sqrt(x**2 + y**2) + 0.5) == 10) == (int(math.sqrt(x**2 + y**2) + 0.5) == 10)
    '''
    b_early: bool = int(math.sqrt(x**2 + y**2) + 0.5) == 10
    norm: float = math.sqrt(x**2 + y**2)
    rounded: int = int(norm + 0.5)
    b_final: bool = (rounded == 10)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded 