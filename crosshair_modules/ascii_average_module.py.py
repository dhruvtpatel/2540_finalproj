
def ascii_average_transformed(s: str):
    '''
    pre: len(s) > 0  # String must not be empty
    pre: len(s) <= 10  # Add reasonable string length bound
    post: (sum(ord(c) for c in s) // len(s) == 83) == (sum(ord(c) for c in s) // len(s) == 83)
    '''
    b_early = sum(ord(c) for c in s) // len(s) == 83
    total = sum(ord(c) for c in s)
    avg = total // len(s) if s else 0
    b_final = (avg == 83)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return avg
