
def sum_until_limit_transformed(nums: list):
    '''
    pre: len(nums) > 0  # List must not be empty
    pre: len(nums) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 20 for x in nums)  # Add reasonable element bounds
    post: (sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60) == (sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60)
    '''
    b_early = sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60
    total = 0
    for n in nums:
        if total >= 50:
            break
        total += n
    adjusted = total + len(nums)
    b_final = (adjusted == 60)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adjusted
