
def square_accumulator_transformed(x: int):
    '''
    pre: 0 <= x <= 20  # Add reasonable bounds
    post: (sum(i * i for i in range(x)) % 100 == 55) == (sum(i * i for i in range(x)) % 100 == 55)
    '''
    b_early = sum(i * i for i in range(x)) % 100 == 55
    acc = 0
    for i in range(x):
        acc += i * i
    final = acc % 100
    b_final = (final == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
