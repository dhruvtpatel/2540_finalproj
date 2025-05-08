import math
import datetime


def factorial_root_calculator_transformed(x: int):
    '''
    pre: 0 <= x <= 10 # Factorials grow fast
    post: (x == 5) == (int(math.sqrt(math.factorial(x))) % 50 == 30)
    '''
    b_early = (x == 5)
    import math
    fact = math.factorial(x)
    root = int(math.sqrt(fact))
    final = root % 50
    b_final = (final == 30)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
