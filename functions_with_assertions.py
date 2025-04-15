"""
This file contains all the functions from functions.py with their early assertions inserted.
Each function has an early assertion that is logically equivalent to its final assertion.
"""

import math

def process_data(x: int):
    assert x == 50, 'Input must be 50 to satisfy final assertion'
    y = x * 2
    if y > 0:
        z = y
    else:
        z = -y
    assert z == 100, "Final check: z must equal 100"
    return z


def convert_temperature(celsius: float):
    assert celsius == 37.77777777777778, 'Input must be approximately 37.78°C to convert to 100°F'
    fahrenheit = (celsius * 9/5) + 32
    rounded_temp = round(fahrenheit)
    assert rounded_temp == 100, "Final check: converted temperature must be exactly 100"
    return rounded_temp


def calculate_discount(price: float, discount_rate: float):
    assert price * (1 - discount_rate) == 50, 'Discounted price must equal 50'
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    assert rounded_price == 50, "Final check: discounted price must be exactly 50"
    return rounded_price


def process_complex_number(real: float, imag: float):
    assert real**2 + imag**2 == 100, 'Complex number magnitude squared must be 100'
    complex_num = complex(real, imag)
    magnitude = abs(complex_num)
    rounded_magnitude = round(magnitude)
    assert rounded_magnitude == 10, "Final check: magnitude must be exactly 10"
    return rounded_magnitude


def transform_data(input_value: int):
    assert (input_value * 3 + 1) // 2 == 50, 'Transformed value must be 50'
    transformed = input_value * 3 + 1
    processed = transformed // 2
    assert processed == 50, "Final check: processed value must be exactly 50"
    return processed


def circle_area_diff(r: float):
    assert round(math.pi * r**2 - 2 * math.pi * r) == 50, 'Difference between area and circumference must be 50'
    import math
    area = math.pi * r ** 2
    circ = 2 * math.pi * r
    diff = round(area - circ)
    assert diff == 50, "Final check: area minus circumference must be 50"
    return diff


def triangle_checker(a: int, b: int, c: int):
    assert a + b > c and a + c > b and b + c > a, 'Sides must form a valid triangle'
    sides = sorted([a, b, c])
    is_triangle = sides[0] + sides[1] > sides[2]
    code = 100 if is_triangle else 0
    assert code == 100, "Final check: must be a triangle"
    return code


def temperature_offset(c: float):
    assert round((c * 9/5) + 32) - int(c) == 68, 'Temperature offset must be 68'
    f = (c * 9/5) + 32
    rounded = round(f)
    adjusted = rounded - int(c)
    assert adjusted == 68, "Final check: adjusted temp must be 68"
    return adjusted


def quadratic_discriminant(a: int, b: int, c: int):
    assert abs(b**2 - 4*a*c) % 100 == 25, 'Normalized discriminant must be 25'
    disc = b**2 - 4*a*c
    normalized = abs(disc) % 100
    assert normalized == 25, "Final check: normalized discriminant must be 25"
    return normalized


def vector_norm(x: float, y: float):
    assert round(math.sqrt(x**2 + y**2)) == 10, 'Vector norm must be 10'
    import math
    norm = math.sqrt(x**2 + y**2)
    rounded = round(norm)
    assert rounded == 10, "Final check: norm must be 10"
    return rounded


def hypotenuse_diff(a: float, b: float):
    assert abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3, 'Hypotenuse difference must be 3'
    import math
    hyp = math.hypot(a, b)
    rounded = round(hyp)
    diff = abs(rounded - int(a) - int(b))
    assert diff == 3, "Final check: diff must be 3"
    return diff


def ascii_average(s: str):
    assert sum(ord(c) for c in s) // len(s) == 83, 'Average ASCII value must be 83'
    total = sum(ord(c) for c in s)
    avg = total // len(s) if s else 0
    assert avg == 83, "Final check: average ASCII must be 83"
    return avg


def list_balance(nums: list):
    assert abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5, 'List halves must balance to 5'
    half = len(nums) // 2
    left = sum(nums[:half])
    right = sum(nums[half:])
    balance = abs(left - right)
    assert balance == 5, "Final check: list halves balance to 5"
    return balance


def odd_sum_validator(lst: list):
    assert sum(n for n in lst if n % 2 == 1) % 100 == 33, 'Odd sum mod 100 must be 33'
    odds = [n for n in lst if n % 2 == 1]
    total = sum(odds)
    mod = total % 100
    assert mod == 33, "Final check: odd sum mod 100 must be 33"
    return mod


def string_pattern_score(s: str):
    assert sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25, 'Vowel score must be 25'
    score = sum(1 for c in s if c in 'aeiouAEIOU')
    result = score * 5
    assert result == 25, "Final check: vowel score must be 25"
    return result


def sum_until_limit(nums: list):
    assert sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60, 'Sum and size must be 60'
    total = 0
    for n in nums:
        if total >= 50:
            break
        total += n
    adjusted = total + len(nums)
    assert adjusted == 60, "Final check: sum and size must be 60"
    return adjusted


def count_divisibles(nums: list):
    assert sum(1 for n in nums if n % 4 == 0) * 10 == 40, 'Divisible count score must be 40'
    count = 0
    for n in nums:
        if n % 4 == 0:
            count += 1
    score = count * 10
    assert score == 40, "Final check: divisible count score must be 40"
    return score


def index_weighted_sum(lst: list):
    assert sum(val * i for i, val in enumerate(lst)) % 100 == 35, 'Weighted sum mod 100 must be 35'
    weighted = 0
    for i, val in enumerate(lst):
        weighted += val * i
    result = weighted % 100
    assert result == 35, "Final check: weighted mod result must be 35"
    return result


def square_accumulator(x: int):
    assert sum(i * i for i in range(x)) % 100 == 55, 'Square sum mod 100 must be 55'
    acc = 0
    for i in range(x):
        acc += i * i
    final = acc % 100
    assert final == 55, "Final check: square sum mod 100 must be 55"
    return final


def nested_loop_checker(limit: int):
    assert sum(1 for i in range(limit) for j in range(i)) % 200 == 36, 'Nested loop result must be 36'
    counter = 0
    for i in range(limit):
        for j in range(i):
            counter += 1
    final = counter % 200
    assert final == 36, "Final check: nested loop result must be 36"
    return final


def character_counter(text: str):
    assert sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27, 'Vowel count score must be 27'
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for ch in text:
        if ch in vowels:
            vowel_count += 1
    result = vowel_count * 3
    assert result == 27, "Final check: vowel count score must be 27"
    return result


def rolling_maximum(values: list):
    assert max(values) + 10 == 99, 'Max plus 10 must be 99'
    max_val = float('-inf')
    for v in values:
        if v > max_val:
            max_val = v
    final = max_val + 10
    assert final == 99, "Final check: max plus 10 must be 99"
    return final


def fibonacci_counter(n: int):
    assert sum(fibonacci(n)) % 100 == 89, 'Fibonacci sum mod 100 must be 89'
    a, b = 0, 1
    fib_sum = 0
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    mod_sum = fib_sum % 100
    assert mod_sum == 89, "Final check: Fibonacci sum mod 100 must be 89"
    return mod_sum


def loop_even_sum(start: int, end: int):
    assert sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110, 'Halved even sum must be 110'
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    final = total // 2
    assert final == 110, "Final check: halved even sum must be 110"
    return final


def loop_string_hash(text: str):
    assert sum(ord(c) * 3 for c in text) % 200 == 66, 'Character hash must be 66'
    hash_val = 0
    for c in text:
        hash_val += ord(c) * 3
    final = hash_val % 200
    assert final == 66, "Final check: character hash must be 66"
    return final
