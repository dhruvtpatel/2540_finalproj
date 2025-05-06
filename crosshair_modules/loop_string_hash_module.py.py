
def loop_string_hash_transformed(text: str):
    '''
    pre: len(text) > 0  # String must not be empty
    pre: len(text) <= 10  # Add reasonable string length bound
    post: (sum(ord(c) * 3 for c in text) % 200 == 66) == (sum(ord(c) * 3 for c in text) % 200 == 66)
    '''
    b_early = sum(ord(c) * 3 for c in text) % 200 == 66
    hash_val = 0
    for c in text:
        hash_val += ord(c) * 3
    final = hash_val % 200
    b_final = (final == 66)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
