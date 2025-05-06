
def list_balance_transformed(nums: list):
    '''
    pre: len(nums) >= 2  # List must have at least 2 elements
    pre: len(nums) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 10 for x in nums)  # Add reasonable element bounds
    post: (abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5) == (abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5)
    '''
    b_early = abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5
    half = len(nums) // 2
    left = sum(nums[:half])
    right = sum(nums[half:])
    balance = abs(left - right)
    b_final = (balance == 5)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return balance
