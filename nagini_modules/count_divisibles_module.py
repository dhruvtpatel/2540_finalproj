from typing import List


def count_divisibles_transformed(nums: List[int]) -> int:
    """
    pre: len(nums) > 0  # List must not be empty
    pre: len(nums) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 10 for x in nums)  # Add reasonable element bounds
    post: __return__ == score
    post: score == count * 10
    """
    # Calculate early condition without generator expression
    early_count: int = 0
    for n in nums:
        if n % 4 == 0:
            early_count += 1

    b_early: bool = early_count * 10 == 40

    # Now do the actual calculation
    count: int = 0
    for n in nums:
        if n % 4 == 0:
            count += 1

    score: int = count * 10
    b_final: bool = score == 40
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return score
