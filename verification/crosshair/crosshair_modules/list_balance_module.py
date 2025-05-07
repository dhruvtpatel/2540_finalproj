import math
import datetime


def list_balance_transformed(nums: list):
    '''
    pre: len(nums) >= 2
    pre: len(nums) <= 20 # Increased bounds for wider testing range
    pre: all(-100 <= x <= 100 for x in nums)  # Wider element bounds
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
