def loop_even_sum_transformed(start: int, end: int) -> int:
    '''
    pre: 0 <= start <= 100  # Add reasonable bounds
    pre: 0 <= end <= 100
    post: __return__ == final
    post: final == total // 2
    '''
    # Calculate early condition without generator expression
    early_total: int = 0
    for i in range(start, end + 1):
        if i % 2 == 0:  # Check if even
            early_total += i
    
    b_early: bool = early_total // 2 == 110
    
    # Now do the actual calculation
    total: int = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
            
    final: int = total // 2
    b_final: bool = (final == 110)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final 