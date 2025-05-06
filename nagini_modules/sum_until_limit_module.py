from typing import List


def sum_until_limit_transformed(nums: List[int]) -> int:
    """
    pre: len(nums) > 0  # List must not be empty
    pre: len(nums) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 20 for x in nums)  # Add reasonable element bounds
    post: __return__ == adjusted
    post: adjusted == total + len(nums)
    """
    # Calculate early condition explicitly without comprehensions
    b_early: bool = False

    # Calculate the value of b_early manually
    valid_sum: int = 0
    for i in range(len(nums)):
        # Check if sum up to this point is < 50
        prefix_sum: int = 0
        for j in range(i + 1):
            prefix_sum += nums[j]

        if prefix_sum < 50:
            valid_sum += nums[i]

    b_early = valid_sum + len(nums) == 60

    # Now do the actual calculation
    total: int = 0
    for n in nums:
        if total >= 50:
            break
        total += n

    adjusted: int = total + len(nums)
    b_final: bool = adjusted == 60
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adjusted
