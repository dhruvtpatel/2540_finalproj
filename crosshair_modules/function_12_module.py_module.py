
def function_12_transformed(x: int):
    '''
    pre: -1000 <= x <= 1000  # Add reasonable bounds
    post: (sum(int(d) for d in str(abs(x))) + len(str(abs(x)))) * 2 == 44
    '''
    b_early = (sum(int(d) for d in str(abs(x))) + len(str(abs(x)))) * 2 == 44
    digits = [int(d) for d in str(abs(x))]
    total = sum(digits)
    adjusted = total + len(digits)
    result = adjusted * 2
    b_final = (result == 44)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
