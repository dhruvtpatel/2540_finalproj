import math
import datetime


def random_mod_calculator_transformed(x: int):
    '''
    pre: -1000 <= x <= 1000
    # NOTE: For functions with random, the post condition checks against a fixed seed version
    post: (x == 23) == (((x + 15) % 90 * 2) % 100 == 46) # seed 42, randint(10,20) -> 15
    '''
    b_early = (x == 23)
    import random
    random.seed(42)
    rand_val = random.randint(10, 20)
    calc = (x + rand_val) % 90
    final = (calc * 2) % 100
    b_final = (final == 46)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
