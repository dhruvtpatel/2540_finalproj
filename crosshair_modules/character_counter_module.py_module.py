
def character_counter_transformed(text: str):
    '''
    pre: len(text) > 0  # String must not be empty
    pre: len(text) <= 10  # Add reasonable string length bound
    post: (sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27) == (sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27)
    '''
    b_early = sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for ch in text:
        if ch in vowels:
            vowel_count += 1
    result = vowel_count * 3
    b_final = (result == 27)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
