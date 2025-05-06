from nagini_contracts.contracts import *

def index_weighted_sum_transformed(lst: list):
    Requires(len(lst) > 0  # List must not be empty)
    Requires(len(lst) <= 10  # Add reasonable list length bound)
    Requires(all(0 <= x <= 10 for x in lst)  # Add reasonable element bounds)
    Ensures((sum(val * i for i, val in enumerate(lst)) % 100 == 35) == (sum(val * i for i, val in enumerate(lst)) % 100 == 35))

    pre: len(lst) > 0  # List must not be empty
    pre: len(lst) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 10 for x in lst)  # Add reasonable element bounds
    post: (sum(val * i for i, val in enumerate(lst)) % 100 == 35) == (sum(val * i for i, val in enumerate(lst)) % 100 == 35)
    b_early = sum(val * i for i, val in enumerate(lst)) % 100 == 35
    weighted = 0
    for i, val in enumerate(lst):
        weighted += val * i
    result = weighted % 100
    b_final = (result == 35)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
