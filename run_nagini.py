import os
import tempfile
import subprocess

functions = {
    "process_data_transformed": """
from typing import *
import math

def process_data_transformed(x: int) -> int:
    b_early = (x == 50)
    y = x * 2
    z = y if y > 0 else -y
    b_final = (z == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return z
""",

    "convert_temperature_transformed": """
from typing import *
import math

def convert_temperature_transformed(celsius: float) -> int:
    b_early = abs(celsius - 37.7778) < 0.01
    fahrenheit = (celsius * 9/5) + 32
    rounded_temp = round(fahrenheit)
    b_final = (rounded_temp == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_temp
""",

    "calculate_discount_transformed": """
from typing import *
import math

def calculate_discount_transformed(price: float, discount_rate: float) -> int:
    b_early = (price == 100 and discount_rate == 0.5)
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    b_final = (rounded_price == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_price
""",

    "process_complex_number_transformed": """
from typing import *
import math

def process_complex_number_transformed(real: float, imag: float) -> int:
    b_early = round((real**2 + imag**2)**0.5) == 10
    complex_num = complex(real, imag)
    magnitude = abs(complex_num)
    rounded_magnitude = round(magnitude)
    b_final = (rounded_magnitude == 10)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_magnitude
""",

    "transform_data_transformed": """
from typing import *
import math

def transform_data_transformed(input_value: int) -> int:
    b_early = (input_value == 33)
    transformed = input_value * 3 + 1
    processed = transformed // 2
    b_final = (processed == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return processed
""",

    "circle_area_diff_transformed": """
from typing import *
import math

def circle_area_diff_transformed(r: float) -> int:
    b_early = round(math.pi * r**2 - 2 * math.pi * r) == 50
    area = math.pi * r ** 2
    circ = 2 * math.pi * r
    diff = round(area - circ)
    b_final = (diff == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return diff
""",

    "triangle_checker_transformed": """
from typing import *

def triangle_checker_transformed(a: int, b: int, c: int) -> int:
    b_early = (a + b > c and a + c > b and b + c > a)
    sides = sorted([a, b, c])
    is_triangle = sides[0] + sides[1] > sides[2]
    code = 100 if is_triangle else 0
    b_final = (code == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return code
""",

    "temperature_offset_transformed": """
from typing import *
import math

def temperature_offset_transformed(c: float) -> int:
    b_early = round((c * 9/5) + 32) - int(c) == 68
    f = (c * 9/5) + 32
    rounded = round(f)
    adjusted = rounded - int(c)
    b_final = (adjusted == 68)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adjusted
""",

    "quadratic_discriminant_transformed": """
from typing import *

def quadratic_discriminant_transformed(a: int, b: int, c: int) -> int:
    b_early = abs(b**2 - 4*a*c) % 100 == 25
    disc = b**2 - 4*a*c
    normalized = abs(disc) % 100
    b_final = (normalized == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return normalized
""",

    "vector_norm_transformed": """
from typing import *
import math

def vector_norm_transformed(x: float, y: float) -> int:
    b_early = round(math.sqrt(x**2 + y**2)) == 10
    norm = math.sqrt(x**2 + y**2)
    rounded = round(norm)
    b_final = (rounded == 10)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded
""",

    "hypotenuse_diff_transformed": """
from typing import *
import math

def hypotenuse_diff_transformed(a: float, b: float) -> int:
    b_early = abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3
    hyp = math.hypot(a, b)
    rounded = round(hyp)
    diff = abs(rounded - int(a) - int(b))
    b_final = (diff == 3)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return diff
""",

    "ascii_average_transformed": """
from typing import *

def ascii_average_transformed(s: str) -> int:
    b_early = sum(ord(c) for c in s) // len(s) == 83 if s else False
    total = sum(ord(c) for c in s)
    avg = total // len(s) if s else 0
    b_final = (avg == 83)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return avg
""",

    "list_balance_transformed": """
from typing import *

def list_balance_transformed(nums: list) -> int:
    b_early = abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5
    half = len(nums) // 2
    left = sum(nums[:half])
    right = sum(nums[half:])
    balance = abs(left - right)
    b_final = (balance == 5)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return balance
""",

    "odd_sum_validator_transformed": """
from typing import *

def odd_sum_validator_transformed(lst: list) -> int:
    b_early = sum(n for n in lst if n % 2 == 1) % 100 == 33
    odds = [n for n in lst if n % 2 == 1]
    total = sum(odds)
    mod = total % 100
    b_final = (mod == 33)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return mod
""",

    "string_pattern_score_transformed": """
from typing import *

def string_pattern_score_transformed(s: str) -> int:
    b_early = sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25
    score = sum(1 for c in s if c in 'aeiouAEIOU')
    result = score * 5
    b_final = (result == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
""",

    "sum_until_limit_transformed": """
from typing import *

def sum_until_limit_transformed(nums: list) -> int:
    # The b_early is tricky because it uses sum(nums[:nums.index(n)+1]) < 50 in a comprehension.
    # We'll keep your logic as-is.
    b_early = sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60

    total = 0
    for n in nums:
        if total >= 50:
            break
        total += n
    adjusted = total + len(nums)
    b_final = (adjusted == 60)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adjusted
""",

    "count_divisibles_transformed": """
from typing import *

def count_divisibles_transformed(nums: list) -> int:
    b_early = sum(1 for n in nums if n % 4 == 0) * 10 == 40
    count = 0
    for n in nums:
        if n % 4 == 0:
            count += 1
    score = count * 10
    b_final = (score == 40)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return score
""",

    "index_weighted_sum_transformed": """
from typing import *

def index_weighted_sum_transformed(lst: list) -> int:
    b_early = sum(val * i for i, val in enumerate(lst)) % 100 == 35
    weighted = 0
    for i, val in enumerate(lst):
        weighted += val * i
    result = weighted % 100
    b_final = (result == 35)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
""",

    "square_accumulator_transformed": """
from typing import *

def square_accumulator_transformed(x: int) -> int:
    b_early = sum(i * i for i in range(x)) % 100 == 55
    acc = 0
    for i in range(x):
        acc += i * i
    final = acc % 100
    b_final = (final == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
""",

    "nested_loop_checker_transformed": """
from typing import *

def nested_loop_checker_transformed(limit: int) -> int:
    b_early = sum(1 for i in range(limit) for j in range(i)) % 200 == 36
    counter = 0
    for i in range(limit):
        for j in range(i):
            counter += 1
    final = counter % 200
    b_final = (final == 36)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
""",

    "character_counter_transformed": """
from typing import *

def character_counter_transformed(text: str) -> int:
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
""",

    "rolling_maximum_transformed": """
from typing import *

def rolling_maximum_transformed(values: list) -> int:
    b_early = max(values) + 10 == 99
    max_val = float('-inf')
    for v in values:
        if v > max_val:
            max_val = v
    final = max_val + 10
    b_final = (final == 99)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
""",

    "loop_even_sum_transformed": """
from typing import *

def loop_even_sum_transformed(start: int, end: int) -> int:
    b_early = sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    final = total // 2
    b_final = (final == 110)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
""",

    "loop_string_hash_transformed": """
from typing import *

def loop_string_hash_transformed(text: str) -> int:
    b_early = sum(ord(c) * 3 for c in text) % 200 == 66
    hash_val = 0
    for c in text:
        hash_val += ord(c) * 3
    final = hash_val % 200
    b_final = (final == 66)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
"""
}


def verify_with_nagini(func_name: str, code: str):
    """Creates a temp file for the given function, then runs Nagini on it."""
    with tempfile.TemporaryDirectory() as tmpdir:
        py_file = os.path.join(tmpdir, f"{func_name}.py")
        with open(py_file, "w") as f:
            f.write(code)

        try:
            result = subprocess.run(
                ["nagini", py_file],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"✅ {func_name}: Verified")
            else:
                print(f"❌ {func_name}: Failed")
                print(result.stderr)
        except FileNotFoundError:
            print("Nagini not found. Please ensure it's installed and on your PATH.")

if __name__ == "__main__":
    for name, code in functions.items():
        verify_with_nagini(name, code)
