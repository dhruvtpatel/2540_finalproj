
def function_25_transformed(x: int):
    '''
    pre: 0 <= x <= 10  # Add reasonable bounds for factorial
    post: (int(math.sqrt(math.factorial(x))) % 50 == 30)
    '''
    import math
    b_early = (int(math.sqrt(math.factorial(x))) % 50 == 30)
    fact = math.factorial(x)
    root = int(math.sqrt(fact))
    final = root % 50
    b_final = (final == 30)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
