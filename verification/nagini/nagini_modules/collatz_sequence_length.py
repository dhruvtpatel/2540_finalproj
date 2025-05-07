from nagini_contracts.contracts import *

@Pure
def collatz_step(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1

@Pure
def is_special_number(n: int) -> bool:
    """Check if n is in the special list [10, 26, 27, 17, 54, 55, 112, 113]"""
    return n == 10 or n == 26 or n == 27 or n == 17 or n == 54 or n == 55 or n == 112 or n == 113

@Pure
def calculate_collatz_length(n: int) -> int:
    """Calculate the length of the Collatz sequence starting from n"""
    Requires(n > 0)
    if n == 1:
        return 1
    else:
        return 1 + calculate_collatz_length(collatz_step(n))

def collatz_sequence_length_transformed(n: int) -> int:
    Requires(n > 0)
    Ensures(Result() == calculate_collatz_length(n) % 20)
    
    b_early = is_special_number(n)
    length = calculate_collatz_length(n)
    adjusted = length % 20
    
    return adjusted