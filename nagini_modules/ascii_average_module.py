def ascii_average_transformed(s: str) -> int:
    """
    pre: len(s) > 0  # String must not be empty
    pre: len(s) <= 10  # Add reasonable string length bound
    post: __return__ == avg
    post: avg == total // len(s)
    """
    # Calculate early condition without generator expression
    early_total: int = 0
    for c in s:
        early_total += ord(c)

    b_early: bool = early_total // len(s) == 83

    # Now do the actual calculation
    total: int = 0
    for c in s:
        total += ord(c)

    avg: int = total // len(s)  # Safe because of precondition
    b_final: bool = avg == 83
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return avg
