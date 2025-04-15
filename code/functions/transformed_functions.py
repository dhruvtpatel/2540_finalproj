"""
Transformed Programs for Assertion Equivalence Checking
Each function has been transformed to explicitly check if the early and final assertions are equivalent.
"""

import math
from typing import List

def fibonacci(n: int) -> List[int]:
    """Helper function to generate Fibonacci sequence."""
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def process_data_transformed(x: int) -> int:
    """Process data with absolute value handling."""
    b_early = (x == 50)
    y = x * 2
    z = abs(y)  # Use abs instead of conditional
    b_final = (z == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return z

def convert_temperature_transformed(celsius: float):
    b_early = abs(celsius - 37.7778) < 0.01
    fahrenheit = (celsius * 9/5) + 32
    rounded_temp = round(fahrenheit)
    b_final = (rounded_temp == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_temp

def calculate_discount_transformed(price: float, discount_rate: float) -> int:
    """Calculate discount with proper rounding."""
    b_early = (abs(price - 100) < 0.001 and abs(discount_rate - 0.5) < 0.001)
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    b_final = (rounded_price == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_price

def process_complex_number_transformed(real: float, imag: float):
    b_early = round((real**2 + imag**2)**0.5) == 10
    complex_num = complex(real, imag)
    magnitude = abs(complex_num)
    rounded_magnitude = round(magnitude)
    b_final = (rounded_magnitude == 10)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_magnitude

def transform_data_transformed(input_value: int):
    b_early = (input_value == 33)
    transformed = input_value * 3 + 1
    processed = transformed // 2
    b_final = (processed == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return processed

def circle_area_diff_transformed(r: float):
    b_early = round(math.pi * r**2 - 2 * math.pi * r) == 50
    area = math.pi * r ** 2
    circ = 2 * math.pi * r
    diff = round(area - circ)
    b_final = (diff == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return diff

def triangle_checker_transformed(a: int, b: int, c: int):
    b_early = (a + b > c and a + c > b and b + c > a)
    sides = sorted([a, b, c])
    is_triangle = sides[0] + sides[1] > sides[2]
    code = 100 if is_triangle else 0
    b_final = (code == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return code

def temperature_offset_transformed(c: float):
    b_early = round((c * 9/5) + 32) - int(c) == 68
    f = (c * 9/5) + 32
    rounded = round(f)
    adjusted = rounded - int(c)
    b_final = (adjusted == 68)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adjusted

def quadratic_discriminant_transformed(a: int, b: int, c: int):
    b_early = abs(b**2 - 4*a*c) % 100 == 25
    disc = b**2 - 4*a*c
    normalized = abs(disc) % 100
    b_final = (normalized == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return normalized

def vector_norm_transformed(x: float, y: float):
    b_early = round(math.sqrt(x**2 + y**2)) == 10
    norm = math.sqrt(x**2 + y**2)
    rounded = round(norm)
    b_final = (rounded == 10)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded

def hypotenuse_diff_transformed(a: float, b: float):
    b_early = abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3
    hyp = math.hypot(a, b)
    rounded = round(hyp)
    diff = abs(rounded - int(a) - int(b))
    b_final = (diff == 3)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return diff

def ascii_average_transformed(s: str):
    b_early = sum(ord(c) for c in s) // len(s) == 83
    total = sum(ord(c) for c in s)
    avg = total // len(s) if s else 0
    b_final = (avg == 83)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return avg

def list_balance_transformed(nums: list):
    b_early = abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5
    half = len(nums) // 2
    left = sum(nums[:half])
    right = sum(nums[half:])
    balance = abs(left - right)
    b_final = (balance == 5)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return balance

def odd_sum_validator_transformed(lst: list):
    b_early = sum(n for n in lst if n % 2 == 1) % 100 == 33
    odds = [n for n in lst if n % 2 == 1]
    total = sum(odds)
    mod = total % 100
    b_final = (mod == 33)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return mod

def string_pattern_score_transformed(s: str):
    b_early = sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25
    score = sum(1 for c in s if c in 'aeiouAEIOU')
    result = score * 5
    b_final = (result == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def sum_until_limit_transformed(nums: list):
    b_early = sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60
    running_sum = 0
    total = 0
    for n in nums:
        if running_sum + n >= 50:
            break
        running_sum += n
        total += n
    adjusted = total + len(nums)
    b_final = (adjusted == 60)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adjusted

def count_divisibles_transformed(nums: list):
    b_early = sum(1 for n in nums if n % 4 == 0) * 10 == 40
    count = 0
    for n in nums:
        if n % 4 == 0:
            count += 1
    score = count * 10
    b_final = (score == 40)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return score

def index_weighted_sum_transformed(lst: list):
    b_early = sum(val * i for i, val in enumerate(lst)) % 100 == 35
    weighted = 0
    for i, val in enumerate(lst):
        weighted += val * i
    result = weighted % 100
    b_final = (result == 35)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def square_accumulator_transformed(x: int):
    b_early = sum(i * i for i in range(x)) % 100 == 55
    acc = 0
    for i in range(x):
        acc += i * i
    final = acc % 100
    b_final = (final == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final

def nested_loop_checker_transformed(limit: int):
    b_early = sum(1 for i in range(limit) for j in range(i)) % 200 == 36
    counter = 0
    for i in range(limit):
        for j in range(i):
            counter += 1
    final = counter % 200
    b_final = (final == 36)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final

def character_counter_transformed(text: str):
    b_early = sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for ch in text:
        if ch in vowels:
            vowel_count += 1
    result = vowel_count * 3
    b_final = (result == 27)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def rolling_maximum_transformed(values: list):
    b_early = max(values) + 10 == 99
    max_val = float('-inf')
    for v in values:
        if v > max_val:
            max_val = v
    final = max_val + 10
    b_final = (final == 99)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final

def fibonacci_counter_transformed(n: int):
    b_early = sum(fibonacci(n)) % 100 == 89
    a, b = 0, 1
    fib_sum = 0
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    mod_sum = fib_sum % 100
    b_final = (mod_sum == 89)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return mod_sum

def loop_even_sum_transformed(start: int, end: int):
    b_early = sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    final = total // 2
    b_final = (final == 110)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final

def loop_string_hash_transformed(text: str):
    b_early = sum(ord(c) * 3 for c in text) % 200 == 66
    hash_val = 0
    for c in text:
        hash_val += ord(c) * 3
    final = hash_val % 200
    b_final = (final == 66)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final 