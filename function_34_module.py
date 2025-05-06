
def function_34_transformed(x: int):
    '''
    pre: -1000 <= x <= 1000  # Add reasonable bounds
    post: math.ceil(x * 1.5) + 4 == 55
    '''
    import math
    b_early = math.ceil(x * 1.5) + 4 == 55
    val = x * 1.5
    rounded = math.ceil(val)
    adj = rounded + 4
    b_final = (adj == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adj
