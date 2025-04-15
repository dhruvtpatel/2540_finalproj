
def temperature_offset_transformed(c: float):
    '''
    pre: 0 <= c <= 100  # Add reasonable temperature bounds
    post: (round((c * 9/5) + 32) - int(c) == 68) == (round((c * 9/5) + 32) - int(c) == 68)
    '''
    b_early = round((c * 9/5) + 32) - int(c) == 68
    f = (c * 9/5) + 32
    rounded = round(f)
    adjusted = rounded - int(c)
    b_final = (adjusted == 68)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adjusted
