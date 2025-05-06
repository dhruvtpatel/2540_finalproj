def string_pattern_score_transformed(s: str) -> int:
    '''
    pre: len(s) > 0  # String must not be empty
    pre: len(s) <= 10  # Add reasonable string length bound
    post: __return__ == count * 5
    post: (count * 5 == 25) == b_early
    '''
    # Calculate vowel count manually instead of using generator expression
    vowels: str = 'aeiouAEIOU'
    count_early: int = 0
    for c in s:
        if c in vowels:
            count_early += 1
    
    b_early: bool = count_early * 5 == 25
    
    # Do the actual calculation
    count: int = 0
    for c in s:
        if c in vowels:
            count += 1
            
    result: int = count * 5
    b_final: bool = (result == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result 