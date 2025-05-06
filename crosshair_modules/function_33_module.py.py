
def function_33_transformed(x: int):
    '''
    pre: -1000 <= x <= 1000  # Add reasonable bounds
    post: ((x % 6) * 7 + 3) * 2 == 60
    '''
    b_early = ((x % 6) * 7 + 3) * 2 == 60
    val = (x % 6) * 7 + 3
    scaled = val * 2
    b_final = (scaled == 60)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return scaled
