from typing import List


def fibonacci_sequence(n: int) -> List[int]:
    """Get the first n Fibonacci numbers."""
    result: List[int] = []
    a: int = 0
    b: int = 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def fibonacci_counter_transformed(n: int) -> int:
    """
    pre: 1 <= n <= 20  # Add reasonable bounds
    post: __return__ == mod_sum
    """
    # Calculate the Fibonacci sequence
    sequence: List[int] = fibonacci_sequence(n)
    fib_sum_early: int = sum(sequence)
    b_early: bool = fib_sum_early % 100 == 89

    # Now do the actual calculation
    a: int = 0
    b: int = 1
    fib_sum: int = 0

    for _ in range(n):
        fib_sum += a
        temp: int = a
        a = b
        b = temp + b

    mod_sum: int = fib_sum % 100
    b_final: bool = mod_sum == 89
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return mod_sum
