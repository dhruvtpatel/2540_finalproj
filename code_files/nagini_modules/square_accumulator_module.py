def square_accumulator_transformed(x: int) -> int:
    '''
    pre: 0 <= x <= 20  # Add reasonable bounds
    post: __return__ == acc % 100
    post: (acc % 100 == 55) == b_early
    '''
    b_early: bool = False
    acc: int = 0
    
    # Calculate the sum manually instead of using generator expression
    temp_sum: int = 0
    for i in range(x):
        temp_sum += i * i
    
    b_early = temp_sum % 100 == 55
    
    # Now do the actual calculation
    acc = 0
    for i in range(x):
        acc += i * i
    
    final: int = acc % 100
    b_final: bool = (final == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final 