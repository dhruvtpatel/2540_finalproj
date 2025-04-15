
def count_divisibles_transformed(nums: list):
    '''
    pre: len(nums) > 0  # List must not be empty
    pre: len(nums) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 10 for x in nums)  # Add reasonable element bounds
    post: (sum(1 for n in nums if n % 4 == 0) * 10 == 40) == (sum(1 for n in nums if n % 4 == 0) * 10 == 40)
    '''
    b_early = sum(1 for n in nums if n % 4 == 0) * 10 == 40
    count = 0
    for n in nums:
        if n % 4 == 0:
            count += 1
    score = count * 10
    b_final = (score == 40)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return score
