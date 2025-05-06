def character_counter_transformed(text: str) -> int:
    '''
    pre: len(text) > 0  # String must not be empty
    pre: len(text) <= 10  # Add reasonable string length bound
    post: __return__ == result
    post: result == vowel_count * 3
    '''
    # Calculate early condition without generator expression
    vowels: str = 'aeiouAEIOU'
    early_count: int = 0
    for ch in text:
        if ch in vowels:
            early_count += 1
    
    b_early: bool = early_count * 3 == 27
    
    # Now do the actual calculation
    vowel_count: int = 0
    for ch in text:
        if ch in vowels:
            vowel_count += 1
            
    result: int = vowel_count * 3
    b_final: bool = (result == 27)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result 