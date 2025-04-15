
def process_data_transformed(x: int):
    '''
    pre: -1000 <= x <= 1000  # Add reasonable bounds
    post: (x == 50) == (x * 2 if x + 2 > 0 else -x * 2 == 100)
    '''
    b_early = (x == 50)
    y = x * 2
    z = y if y > 0 else -y
    b_final = (z == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return z
