from nagini_contracts.contracts import *
from typing import List

def sum_list_portion(nums: List[int], start: int, end: int) -> int:
    """Compute the sum of elements in nums[start:end]"""
    Requires(Acc(list_pred(nums)))
    Requires(start >= 0)
    Requires(end >= start)
    Requires(end <= len(nums))
    
    result = 0
    i = start
    while i < end:
        result += nums[i]
        i += 1
    return result

def list_balance_transformed(nums: List[int]) -> int:
    """Calculate the absolute difference between sum of left and right halves"""
    Requires(Acc(list_pred(nums)))
    
    half = len(nums) // 2
    left = sum_list_portion(nums, 0, half)
    right = sum_list_portion(nums, half, len(nums))
    
    # Calculate absolute difference
    diff = left - right
    if diff < 0:
        diff = -diff
    
    return diff