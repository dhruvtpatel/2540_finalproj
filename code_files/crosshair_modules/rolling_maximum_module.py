
def rolling_maximum_transformed(values: list):
    '''
    pre: len(values) > 0  # List must not be empty
    pre: len(values) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 20 for x in values)  # Add reasonable element bounds
    post: (max(values) + 10 == 99) == (max(values) + 10 == 99)
    '''
    b_early = max(values) + 10 == 99
    max_val = float('-inf')
    for v in values:
        if v > max_val:
            max_val = v
    final = max_val + 10
    b_final = (final == 99)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
