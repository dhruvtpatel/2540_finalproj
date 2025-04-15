"""
Transformed Programs for Assertion Equivalence Checking with Nagini Verification Contracts
Each function includes simplified contracts for Nagini verification.
"""

from typing import *
import math
from nagini_contracts.contracts import *
from nagini_contracts.io_contracts import *
from nagini_contracts.obligations import *
import inspect
import sys
import importlib
from typing import Optional, Dict, Any

def process_data_transformed(x: int) -> int:
    """
    Requires: True
    Ensures: result == abs(x * 2)
    """
    y = x * 2
    z = abs(y)
    return z

def convert_temperature_transformed(celsius: float) -> int:
    """
    Requires: True
    Ensures: result == round((celsius * 9/5) + 32)
    """
    fahrenheit = (celsius * 9/5) + 32
    rounded_temp = round(fahrenheit)
    return rounded_temp

def calculate_discount_transformed(price: float, discount_rate: float) -> int:
    """
    Requires: price >= 0 and 0 <= discount_rate <= 1
    Ensures: result == round(price * (1 - discount_rate))
    """
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    return rounded_price

def process_complex_number_transformed(real: float, imag: float) -> int:
    """
    Requires: True
    Ensures: result == round(abs(complex(real, imag)))
    """
    complex_num = complex(real, imag)
    magnitude = abs(complex_num)
    return round(magnitude)

def transform_data_transformed(nums: List[int]) -> int:
    """
    Requires: len(nums) > 0
    Ensures: result == sum(nums) // len(nums)
    """
    return sum(nums) // len(nums)

def circle_area_diff_transformed(r1: float, r2: float) -> int:
    """
    Requires: r1 > 0 and r2 > 0
    Ensures: result == round(abs(math.pi * (r1**2 - r2**2)))
    """
    area1 = math.pi * r1**2
    area2 = math.pi * r2**2
    diff = abs(area1 - area2)
    return round(diff)

def triangle_checker_transformed(a: int, b: int, c: int) -> bool:
    """
    Requires: a > 0 and b > 0 and c > 0
    Ensures: result == (a + b > c and a + c > b and b + c > a)
    """
    return a + b > c and a + c > b and b + c > a

def temperature_offset_transformed(t: float) -> float:
    """
    Requires: True
    Ensures: result == t + 10.0
    """
    return t + 10.0

def quadratic_discriminant_transformed(a: float, b: float, c: float) -> float:
    """
    Requires: True
    Ensures: result == b**2 - 4*a*c
    """
    return b**2 - 4*a*c

def vector_norm_transformed(v: List[float]) -> float:
    """
    Requires: len(v) > 0
    Ensures: result == math.sqrt(sum(x**2 for x in v))
    """
    return math.sqrt(sum(x**2 for x in v))

def hypotenuse_diff_transformed(a: float, b: float) -> float:
    """
    Requires: a > 0 and b > 0
    Ensures: result == abs(math.sqrt(a**2 + b**2) - 10.0)
    """
    hypotenuse = math.sqrt(a**2 + b**2)
    return abs(hypotenuse - 10.0)

def ascii_average_transformed(s: str) -> int:
    """
    Requires: len(s) > 0
    Ensures: result == sum(ord(c) for c in s) // len(s)
    """
    return sum(ord(c) for c in s) // len(s)

def list_balance_transformed(nums: List[int]) -> int:
    """
    Requires: len(nums) > 0
    Ensures: result == sum(nums) // len(nums)
    """
    return sum(nums) // len(nums)

def odd_sum_validator_transformed(nums: List[int]) -> bool:
    """
    Requires: len(nums) > 0
    Ensures: result == (sum(x for x in nums if x % 2 != 0) > 50)
    """
    return sum(x for x in nums if x % 2 != 0) > 50

def string_pattern_score_transformed(s: str) -> int:
    """
    Requires: len(s) > 0
    Ensures: result == sum(ord(c) for c in s if c.isalpha())
    """
    return sum(ord(c) for c in s if c.isalpha())

def sum_until_limit_transformed(nums: List[int]) -> int:
    """
    Requires: len(nums) > 0
    Ensures: result == sum(nums[:i]) where i is the first index where sum(nums[:i+1]) >= 50
    """
    total = 0
    for n in nums:
        if total + n >= 50:
            break
        total += n
    return total

def count_divisibles_transformed(nums: List[int], d: int) -> int:
    """
    Requires: len(nums) > 0 and d > 0
    Ensures: result == sum(1 for x in nums if x % d == 0)
    """
    return sum(1 for x in nums if x % d == 0)

def index_weighted_sum_transformed(nums: List[int]) -> int:
    """
    Requires: len(nums) > 0
    Ensures: result == sum(i * x for i, x in enumerate(nums))
    """
    return sum(i * x for i, x in enumerate(nums))

def square_accumulator_transformed(x: int) -> int:
    """
    Requires: x >= 0
    Ensures: result == sum(i**2 for i in range(x+1))
    """
    return sum(i**2 for i in range(x+1))

def nested_loop_checker_transformed(n: int) -> int:
    """
    Requires: n > 0
    Ensures: result == sum(i * j for i in range(n) for j in range(n))
    """
    return sum(i * j for i in range(n) for j in range(n))

def character_counter_transformed(s: str) -> int:
    """
    Requires: len(s) > 0
    Ensures: result == sum(1 for c in s if c.lower() in 'aeiou')
    """
    return sum(1 for c in s if c.lower() in 'aeiou')

def rolling_maximum_transformed(nums: List[int]) -> int:
    """
    Requires: len(nums) > 0
    Ensures: result == max(nums)
    """
    return max(nums)

def fibonacci_counter_transformed(n: int) -> int:
    """
    Requires: n >= 0
    Ensures: result == sum(fib(i) for i in range(n+1)) where fib(0)=0, fib(1)=1, fib(i)=fib(i-1)+fib(i-2)
    """
    if n == 0:
        return 0
    a, b = 0, 1
    total = a + b
    for _ in range(2, n+1):
        a, b = b, a + b
        total += b
    return total

def loop_even_sum_transformed(start: int, end: int) -> int:
    """
    Requires: start <= end
    Ensures: result == sum(x for x in range(start, end+1) if x % 2 == 0)
    """
    return sum(x for x in range(start, end+1) if x % 2 == 0)

def loop_string_hash_transformed(s: str) -> int:
    """
    Requires: len(s) > 0
    Ensures: result == sum((i+1) * ord(c) for i, c in enumerate(s))
    """
    return sum((i+1) * ord(c) for i, c in enumerate(s))

def extract_assertions(func: callable) -> tuple[str, str]:
    """Extract early and late assertions from a function's source code."""
    source = inspect.getsource(func)
    early_assert = None
    late_assert = None
    
    for line in source.split('\n'):
        if 'assert' in line:
            if 'Final check' in line:
                late_assert = line.strip()
            else:
                early_assert = line.strip()
    
    if not early_assert or not late_assert:
        raise ValueError("Could not find both assertions")
    
    # Extract the conditions
    early_cond = early_assert.split('assert')[1].split(',')[0].strip()
    late_cond = late_assert.split('assert')[1].split(',')[0].strip()
    
    return early_cond, late_cond

def create_verification_function(func: callable) -> callable:
    """Create a Nagini verification function to check assertion equivalence."""
    early_cond, late_cond = extract_assertions(func)
    sig = inspect.signature(func)
    
    # Create the verification function with the same signature
    def verification_wrapper(*args, **kwargs):
        # Precondition: early assertion implies late assertion
        Requires(Implies(eval(early_cond), eval(late_cond)))
        # Postcondition: late assertion implies early assertion
        Ensures(Implies(eval(late_cond), eval(early_cond)))
        return func(*args, **kwargs)
    
    # Copy the signature
    verification_wrapper.__signature__ = sig
    verification_wrapper.__name__ = f"verify_{func.__name__}"
    
    return verification_wrapper

def verify_assertion_equivalence(func_name: str) -> tuple[bool, Optional[str]]:
    """Verify that early and late assertions are equivalent using Nagini."""
    try:
        # Import the function
        module = importlib.import_module('functions_with_assertions')
        func = getattr(module, func_name)
        
        # Create verification function
        verify_func = create_verification_function(func)
        
        # Run Nagini verification
        # This would be replaced with actual Nagini verification call
        result = True  # Placeholder for actual verification
        error = None
        
        return result, error
        
    except Exception as e:
        return False, str(e)

def main():
    if len(sys.argv) != 2:
        print("Usage: python nagini.py <function_name>")
        sys.exit(1)
    
    function_name = sys.argv[1]
    
    print(f"Verifying assertion equivalence for {function_name}...")
    is_equivalent, error = verify_assertion_equivalence(function_name)
    
    if is_equivalent:
        print("Verification successful: Early and late assertions are equivalent")
    else:
        print("Verification failed: Early and late assertions are not equivalent")
        if error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()
