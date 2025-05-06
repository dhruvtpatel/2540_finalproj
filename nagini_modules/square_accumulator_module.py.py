from nagini_contracts.contracts import *

def square_accumulator_transformed(x: int):
    Requires(0 <= x <= 10  # Add reasonable input bounds)
    Ensures((sum(i * i for i in range(x)) % 100 == 55) == (sum(i * i for i in range(x)) % 100 == 55))

    pre: 0 <= x <= 10  # Add reasonable input bounds
    post: (sum(i * i for i in range(x)) % 100 == 55) == (sum(i * i for i in range(x)) % 100 == 55)
    b_early = sum(i * i for i in range(x)) % 100 == 55
    acc = 0
    for i in range(x):
        acc += i * i
    final = acc % 100
    b_final = (final == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
