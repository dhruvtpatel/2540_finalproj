
import math
def vector_norm_transformed(x: float, y: float):
    '''
    pre: -10 <= x <= 10  # Add reasonable vector component bounds
    pre: -10 <= y <= 10
    post: (round(math.sqrt(x**2 + y**2)) == 10) == (round(math.sqrt(x**2 + y**2)) == 10)
    '''
    b_early = round(math.sqrt(x**2 + y**2)) == 10
    norm = math.sqrt(x**2 + y**2)
    rounded = round(norm)
    b_final = (rounded == 10)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded
