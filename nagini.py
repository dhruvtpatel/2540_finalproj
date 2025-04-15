"""
Transformed Programs for Assertion Equivalence Checking with Nagini Verification Contracts
Each function includes an "Ensures" contract to enable static verification with Nagini.
Note: Nagini supports a restricted Python 3.6 subset. Avoid complex control flow, dynamic types, and advanced built-ins.
"""

from typing import *
import math

def process_data_transformed(x: int) -> int:
    """
    Ensures: (x == 50) == ((x * 2 if x * 2 > 0 else -(x * 2)) == 100)
    """
    b_early = (x == 50)
    y = x * 2
    z = y if y > 0 else -y
    b_final = (z == 100)
    assert b_early == b_final
    return z

def convert_temperature_transformed(celsius: float) -> int:
    """
    Ensures: (abs(celsius - 37.7778) < 0.01) == (round((celsius * 9/5) + 32) == 100)
    """
    b_early = abs(celsius - 37.7778) < 0.01
    fahrenheit = (celsius * 9/5) + 32
    rounded_temp = round(fahrenheit)
    b_final = (rounded_temp == 100)
    assert b_early == b_final
    return rounded_temp

def calculate_discount_transformed(price: float, discount_rate: float) -> int:
    """
    Ensures: (price == 100 and discount_rate == 0.5) == (round(price * (1 - discount_rate)) == 50)
    """
    b_early = (price == 100 and discount_rate == 0.5)
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    b_final = (rounded_price == 50)
    assert b_early == b_final
    return rounded_price

def process_complex_number_transformed(real: float, imag: float) -> int:
    """
    Ensures: (round((real**2 + imag**2)**0.5) == 10) == (round(abs(complex(real, imag))) == 10)
    """
    b_early = round((real**2 + imag**2)**0.5) == 10
    complex_num = complex(real, imag)
    magnitude = abs(complex_num)
    rounded_magnitude = round(magnitude)
    b_final = (rounded_magnitude == 10)
    assert b_early == b_final
    return rounded_magnitude

def transform_data_transformed(input_value: int) -> int:
    """
    Ensures: (input_value == 33) == (((input_value * 3 + 1) // 2) == 50)
    """
    b_early = (input_value == 33)
    transformed = input_value * 3 + 1
    processed = transformed // 2
    b_final = (processed == 50)
    assert b_early == b_final
    return processed

def circle_area_diff_transformed(r: float) -> int:
    """
    Ensures: (round(math.pi * r**2 - 2 * math.pi * r) == 50) == (round(math.pi * r ** 2 - 2 * math.pi * r) == 50)
    """
    b_early = round(math.pi * r**2 - 2 * math.pi * r) == 50
    area = math.pi * r ** 2
    circ = 2 * math.pi * r
    diff = round(area - circ)
    b_final = (diff == 50)
    assert b_early == b_final
    return diff

def triangle_checker_transformed(a: int, b: int, c: int) -> int:
    """
    Ensures: ((a + b > c and a + c > b and b + c > a) == (100 if sorted([a,b,c])[0] + sorted([a,b,c])[1] > sorted([a,b,c])[2] else 0 == 100))
    """
    b_early = (a + b > c and a + c > b and b + c > a)
    sides = sorted([a, b, c])
    is_triangle = sides[0] + sides[1] > sides[2]
    code = 100 if is_triangle else 0
    b_final = (code == 100)
    assert b_early == b_final
    return code

def temperature_offset_transformed(c: float) -> int:
    """
    Ensures: (round((c * 9/5) + 32) - int(c) == 68) == ((round((c * 9/5) + 32) - int(c)) == 68)
    """
    b_early = round((c * 9/5) + 32) - int(c) == 68
    f = (c * 9/5) + 32
    rounded = round(f)
    adjusted = rounded - int(c)
    b_final = (adjusted == 68)
    assert b_early == b_final
    return adjusted

def quadratic_discriminant_transformed(a: int, b: int, c: int) -> int:
    """
    Ensures: (abs(b**2 - 4*a*c) % 100 == 25) == ((abs(b**2 - 4*a*c) % 100) == 25)
    """
    b_early = abs(b**2 - 4*a*c) % 100 == 25
    disc = b**2 - 4*a*c
    normalized = abs(disc) % 100
    b_final = (normalized == 25)
    assert b_early == b_final
    return normalized

def vector_norm_transformed(x: float, y: float) -> int:
    """
    Ensures: (round(math.sqrt(x**2 + y**2)) == 10) == (round(math.sqrt(x**2 + y**2)) == 10)
    """
    b_early = round(math.sqrt(x**2 + y**2)) == 10
    norm = math.sqrt(x**2 + y**2)
    rounded = round(norm)
    b_final = (rounded == 10)
    assert b_early == b_final
    return rounded

def hypotenuse_diff_transformed(a: float, b: float) -> int:
    """
    Ensures: (abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3) == (abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3)
    """
    b_early = abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3
    hyp = math.hypot(a, b)
    rounded = round(hyp)
    diff = abs(rounded - int(a) - int(b))
    b_final = (diff == 3)
    assert b_early == b_final
    return diff

def ascii_average_transformed(s: str) -> int:
    """
    Ensures: (len(s) > 0) ==> ((sum(ord(c) for c in s) // len(s)) == 83) == ((sum(ord(c) for c in s) // len(s)) == 83)
    """
    b_early = sum(ord(c) for c in s) // len(s) == 83
    total = sum(ord(c) for c in s)
    avg = total // len(s) if s else 0
    b_final = (avg == 83)
    assert b_early == b_final
    return avg

def list_balance_transformed(nums: List[int]) -> int:
    """
    Ensures: (abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5) == (abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5)
    """
    half = len(nums) // 2
    left = sum(nums[:half])
    right = sum(nums[half:])
    balance = abs(left - right)
    b_early = balance == 5
    b_final = (balance == 5)
    assert b_early == b_final
    return balance

def odd_sum_validator_transformed(lst: List[int]) -> int:
    """
    Ensures: (sum(n for n in lst if n % 2 == 1) % 100 == 33) == (sum(n for n in lst if n % 2 == 1) % 100 == 33)
    """
    odds = [n for n in lst if n % 2 == 1]
    total = sum(odds)
    mod = total % 100
    b_early = mod == 33
    b_final = (mod == 33)
    assert b_early == b_final
    return mod

def string_pattern_score_transformed(s: str) -> int:
    """
    Ensures: (sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25) == (sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25)
    """
    score = sum(1 for c in s if c in 'aeiouAEIOU')
    result = score * 5
    b_early = result == 25
    b_final = (result == 25)
    assert b_early == b_final
    return result

def sum_until_limit_transformed(nums: List[int]) -> int:
    """
    Ensures: (sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60) == ((sum_until + len(nums)) == 60)
    """
    total = 0
    for n in nums:
        if total >= 50:
            break
        total += n
    adjusted = total + len(nums)
    b_early = adjusted == 60
    b_final = (adjusted == 60)
    assert b_early == b_final
    return adjusted

def count_divisibles_transformed(nums: List[int]) -> int:
    """
    Ensures: (sum(1 for n in nums if n % 4 == 0) * 10 == 40) == ((sum(1 for n in nums if n % 4 == 0) * 10) == 40)
    """
    count = sum(1 for n in nums if n % 4 == 0)
    score = count * 10
    b_early = score == 40
    b_final = (score == 40)
    assert b_early == b_final
    return score

def index_weighted_sum_transformed(lst: List[int]) -> int:
    """
    Ensures: (sum(val * i for i, val in enumerate(lst)) % 100 == 35) == ((sum(val * i for i, val in enumerate(lst)) % 100) == 35)
    """
    weighted = sum(val * i for i, val in enumerate(lst))
    result = weighted % 100
    b_early = result == 35
    b_final = (result == 35)
    assert b_early == b_final
    return result

def square_accumulator_transformed(x: int) -> int:
    """
    Ensures: (sum(i * i for i in range(x)) % 100 == 55) == ((sum(i * i for i in range(x)) % 100) == 55)
    """
    acc = sum(i * i for i in range(x))
    final = acc % 100
    b_early = final == 55
    b_final = (final == 55)
    assert b_early == b_final
    return final

def nested_loop_checker_transformed(limit: int) -> int:
    """
    Ensures: (sum(1 for i in range(limit) for j in range(i)) % 200 == 36) == ((sum(1 for i in range(limit) for j in range(i)) % 200) == 36)
    """
    counter = sum(1 for i in range(limit) for j in range(i))
    final = counter % 200
    b_early = final == 36
    b_final = (final == 36)
    assert b_early == b_final
    return final

def character_counter_transformed(text: str) -> int:
    """
    Ensures: (sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27) == ((sum(1 for ch in text if ch in 'aeiouAEIOU') * 3) == 27)
    """
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for ch in text if ch in vowels)
    result = vowel_count * 3
    b_early = result == 27
    b_final = (result == 27)
    assert b_early == b_final
    return result

def rolling_maximum_transformed(values: List[int]) -> int:
    """
    Ensures: (max(values) + 10 == 99) == ((max(values) + 10) == 99)
    """
    max_val = max(values)
    final = max_val + 10
    b_early = final == 99
    b_final = (final == 99)
    assert b_early == b_final
    return final

def fibonacci_counter_transformed(n: int) -> int:
    """
    Ensures: (sum(fibonacci(n)) % 100 == 89) == ((fib_sum % 100) == 89)
    """
    a, b = 0, 1
    fib_sum = 0
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    mod_sum = fib_sum % 100
    b_early = mod_sum == 89
    b_final = (mod_sum == 89)
    assert b_early == b_final
    return mod_sum

def loop_even_sum_transformed(start: int, end: int) -> int:
    """
    Ensures: (sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110) == (((sum(i for i in range(start, end + 1) if i % 2 == 0)) // 2) == 110)
    """
    total = sum(i for i in range(start, end + 1) if i % 2 == 0)
    final = total // 2
    b_early = final == 110
    b_final = (final == 110)
    assert b_early == b_final
    return final

def loop_string_hash_transformed(text: str) -> int:
    """
    Ensures: (sum(ord(c) * 3 for c in text) % 200 == 66) == ((sum(ord(c) * 3 for c in text) % 200) == 66)
    """
    hash_val = sum(ord(c) * 3 for c in text)
    final = hash_val % 200
    b_early = final == 66
    b_final = (final == 66)
    assert b_early == b_final
    return final
