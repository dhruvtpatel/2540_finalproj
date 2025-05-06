
def function_31_transformed(x: int):
    '''
    pre: -1000 <= x <= 1000  # Add reasonable bounds
    post: (((x + 15) % 90 * 2) % 100 == 46) == (((x + 15) % 90 * 2) % 100 == 46)
    '''
    b_early = (((x + 15) % 90 * 2) % 100 == 46)
    import random
    rand_val = random.randint(10, 20)
    calc = (x + rand_val) % 90
    final = (calc * 2) % 100
    b_final = (final == 46)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
