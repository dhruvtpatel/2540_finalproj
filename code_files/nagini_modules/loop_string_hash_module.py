def loop_string_hash_transformed(text: str) -> int:
    """
    pre: len(text) > 0  # String must not be empty
    pre: len(text) <= 10  # Add reasonable string length bound
    post: __return__ == final
    post: final == hash_val % 200
    """
    # Calculate the hash value without generator expression
    early_hash: int = 0
    for c in text:
        early_hash += ord(c) * 3

    b_early: bool = early_hash % 200 == 66

    hash_val: int = 0
    for c in text:
        hash_val += ord(c) * 3

    final: int = hash_val % 200
    b_final: bool = final == 66
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
