from typing import List


def list_balance_transformed(nums: List[int]) -> int:
    """
    pre: len(nums) >= 2  # List must have at least 2 elements
    pre: len(nums) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 10 for x in nums)  # Add reasonable element bounds
    post: __return__ == balance
    post: balance == abs(left - right)
    """
    half: int = len(nums) // 2

    # Calculate left sum manually
    left_early: int = 0
    for i in range(half):
        left_early += nums[i]

    # Calculate right sum manually
    right_early: int = 0
    for i in range(half, len(nums)):
        right_early += nums[i]

    b_early: bool = abs(left_early - right_early) == 5

    # Now do the actual calculation
    half = len(nums) // 2

    left: int = 0
    for i in range(half):
        left += nums[i]

    right: int = 0
    for i in range(half, len(nums)):
        right += nums[i]

    balance: int = abs(left - right)
    b_final: bool = balance == 5
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return balance
