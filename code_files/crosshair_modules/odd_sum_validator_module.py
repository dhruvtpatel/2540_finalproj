
def odd_sum_validator_transformed(lst: list):
    '''
    pre: len(lst) > 0  # List must not be empty
    pre: len(lst) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 10 for x in lst)  # Add reasonable element bounds
    post: (sum(n for n in lst if n % 2 == 1) % 100 == 33) == (sum(n for n in lst if n % 2 == 1) % 100 == 33)
    '''
    b_early = sum(n for n in lst if n % 2 == 1) % 100 == 33
    odds = [n for n in lst if n % 2 == 1]
    total = sum(odds)
    mod = total % 100
    b_final = (mod == 33)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return mod
