from nagini_contracts.contracts import *
import math

def process_data_verified(x: int) -> int:
    Requires(True)
    Ensures(Result() == abs(x * 2))
    b_early = (x == 50)
    y = x * 2
    z = y if y > 0 else -y
    b_final = (z == 100)
    Assert(b_early == b_final)
    return z

def convert_temperature_verified(celsius: float) -> int:
    Requires(True)
    Ensures(Result() == round((celsius * 9/5) + 32))
    b_early = abs(celsius - 37.7778) < 0.01
    fahrenheit = (celsius * 9/5) + 32
    rounded_temp = round(fahrenheit)
    b_final = (rounded_temp == 100)
    Assert(b_early == b_final)
    return rounded_temp

def calculate_discount_verified(price: float, discount_rate: float) -> int:
    Requires(True)
    Ensures(Result() == round(price * (1 - discount_rate)))
    b_early = (price == 100 and discount_rate == 0.5)
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    b_final = (rounded_price == 50)
    Assert(b_early == b_final)
    return rounded_price

def process_complex_number_verified(real: float, imag: float) -> int:
    Requires(True)
    Ensures(Result() == round(abs(complex(real, imag))))
    b_early = round((real**2 + imag**2)**0.5) == 10
    complex_num = complex(real, imag)
    magnitude = abs(complex_num)
    rounded_magnitude = round(magnitude)
    b_final = (rounded_magnitude == 10)
    Assert(b_early == b_final)
    return rounded_magnitude

def transform_data_verified(input_value: int) -> int:
    Requires(True)
    Ensures(Result() == (input_value * 3 + 1) // 2)
    b_early = (input_value == 33)
    transformed = input_value * 3 + 1
    processed = transformed // 2
    b_final = (processed == 50)
    Assert(b_early == b_final)
    return processed

def circle_area_diff_verified(r: float) -> int:
    Requires(True)
    Ensures(Result() == round(math.pi * r**2 - 2 * math.pi * r))
    b_early = round(math.pi * r**2 - 2 * math.pi * r) == 50
    area = math.pi * r ** 2
    circ = 2 * math.pi * r
    diff = round(area - circ)
    b_final = (diff == 50)
    Assert(b_early == b_final)
    return diff

def triangle_checker_verified(a: int, b: int, c: int) -> int:
    Requires(True)
    Ensures(Result() == 100 if (a + b > c and a + c > b and b + c > a) else 0)
    b_early = (a + b > c and a + c > b and b + c > a)
    sides = sorted([a, b, c])
    is_triangle = sides[0] + sides[1] > sides[2]
    code = 100 if is_triangle else 0
    b_final = (code == 100)
    Assert(b_early == b_final)
    return code

def temperature_offset_verified(c: float) -> int:
    Requires(True)
    Ensures(Result() == round((c * 9/5) + 32) - int(c))
    b_early = round((c * 9/5) + 32) - int(c) == 68
    f = (c * 9/5) + 32
    rounded = round(f)
    adjusted = rounded - int(c)
    b_final = (adjusted == 68)
    Assert(b_early == b_final)
    return adjusted

def quadratic_discriminant_verified(a: int, b: int, c: int) -> int:
    Requires(True)
    Ensures(Result() == abs(b**2 - 4*a*c) % 100)
    b_early = abs(b**2 - 4*a*c) % 100 == 25
    disc = b**2 - 4*a*c
    normalized = abs(disc) % 100
    b_final = (normalized == 25)
    Assert(b_early == b_final)
    return normalized

def vector_norm_verified(x: float, y: float) -> int:
    Requires(True)
    Ensures(Result() == round(math.sqrt(x**2 + y**2)))
    b_early = round(math.sqrt(x**2 + y**2)) == 10
    norm = math.sqrt(x**2 + y**2)
    rounded = round(norm)
    b_final = (rounded == 10)
    Assert(b_early == b_final)
    return rounded

def hypotenuse_diff_verified(a: float, b: float) -> int:
    Requires(True)
    Ensures(Result() == abs(round(math.hypot(a, b)) - int(a) - int(b)))
    b_early = abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3
    hyp = math.hypot(a, b)
    rounded = round(hyp)
    diff = abs(rounded - int(a) - int(b))
    b_final = (diff == 3)
    Assert(b_early == b_final)
    return diff

def ascii_average_verified(s: str) -> int:
    Requires(len(s) > 0)
    Ensures(Result() == sum(ord(c) for c in s) // len(s))
    b_early = sum(ord(c) for c in s) // len(s) == 83
    total = sum(ord(c) for c in s)
    avg = total // len(s)
    b_final = (avg == 83)
    Assert(b_early == b_final)
    return avg

def list_balance_verified(nums: list) -> int:
    Requires(len(nums) > 0)
    Ensures(Result() == abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])))
    b_early = abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5
    half = len(nums) // 2
    left = sum(nums[:half])
    right = sum(nums[half:])
    balance = abs(left - right)
    b_final = (balance == 5)
    Assert(b_early == b_final)
    return balance

def odd_sum_validator_verified(lst: list) -> int:
    Requires(True)
    Ensures(Result() == sum(n for n in lst if n % 2 == 1) % 100)
    b_early = sum(n for n in lst if n % 2 == 1) % 100 == 33
    odds = [n for n in lst if n % 2 == 1]
    total = sum(odds)
    mod = total % 100
    b_final = (mod == 33)
    Assert(b_early == b_final)
    return mod

def string_pattern_score_verified(s: str) -> int:
    Requires(True)
    Ensures(Result() == sum(1 for c in s if c in 'aeiouAEIOU') * 5)
    b_early = sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25
    score = sum(1 for c in s if c in 'aeiouAEIOU')
    result = score * 5
    b_final = (result == 25)
    Assert(b_early == b_final)
    return result

def sum_until_limit_verified(nums: list) -> int:
    Requires(True)
    Ensures(Result() == sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums))
    b_early = sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60
    total = 0
    for n in nums:
        if total >= 50:
            break
        total += n
    adjusted = total + len(nums)
    b_final = (adjusted == 60)
    Assert(b_early == b_final)
    return adjusted

def count_divisibles_verified(nums: list) -> int:
    Requires(True)
    Ensures(Result() == sum(1 for n in nums if n % 4 == 0) * 10)
    b_early = sum(1 for n in nums if n % 4 == 0) * 10 == 40
    count = 0
    for n in nums:
        if n % 4 == 0:
            count += 1
    score = count * 10
    b_final = (score == 40)
    Assert(b_early == b_final)
    return score

def index_weighted_sum_verified(lst: list) -> int:
    Requires(True)
    Ensures(Result() == sum(val * i for i, val in enumerate(lst)) % 100)
    b_early = sum(val * i for i, val in enumerate(lst)) % 100 == 35
    weighted = 0
    for i, val in enumerate(lst):
        weighted += val * i
    result = weighted % 100
    b_final = (result == 35)
    Assert(b_early == b_final)
    return result

def square_accumulator_verified(x: int) -> int:
    Requires(x >= 0)
    Ensures(Result() == sum(i * i for i in range(x)) % 100)
    b_early = sum(i * i for i in range(x)) % 100 == 55
    acc = 0
    for i in range(x):
        acc += i * i
    final = acc % 100
    b_final = (final == 55)
    Assert(b_early == b_final)
    return final

def nested_loop_checker_verified(limit: int) -> int:
    Requires(limit >= 0)
    Ensures(Result() == sum(1 for i in range(limit) for j in range(i)) % 200)
    b_early = sum(1 for i in range(limit) for j in range(i)) % 200 == 36
    counter = 0
    for i in range(limit):
        for j in range(i):
            counter += 1
    final = counter % 200
    b_final = (final == 36)
    Assert(b_early == b_final)
    return final

def character_counter_verified(text: str) -> int:
    Requires(True)
    Ensures(Result() == sum(1 for ch in text if ch in 'aeiouAEIOU') * 3)
    b_early = sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for ch in text:
        if ch in vowels:
            vowel_count += 1
    result = vowel_count * 3
    b_final = (result == 27)
    Assert(b_early == b_final)
    return result

def rolling_maximum_verified(values: list) -> int:
    Requires(len(values) > 0)
    Ensures(Result() == max(values) + 10)
    b_early = max(values) + 10 == 99
    max_val = float('-inf')
    for v in values:
        if v > max_val:
            max_val = v
    final = max_val + 10
    b_final = (final == 99)
    Assert(b_early == b_final)
    return final

# def fibonacci_counter_verified(n: int) -> int:
#     Requires(n >= 0)
#     Ensures(Result() == sum(fibonacci(n)) % 100)
#     b_early = sum(fibonacci(n)) % 100 == 89
#     a, b = 0, 1
#     fib_sum = 0
#     for _ in range(n):
#         fib_sum += a
#         a, b = b, a + b
#     mod_sum = fib_sum % 100
#     b_final = (mod_sum == 89)
#     Assert(b_early == b_final)
#     return mod_sum

def loop_even_sum_verified(start: int, end: int) -> int:
    Requires(start <= end)
    Ensures(Result() == sum(i for i in range(start, end + 1) if i % 2 == 0) // 2)
    b_early = sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    final = total // 2
    b_final = (final == 110)
    Assert(b_early == b_final)
    return final

def loop_string_hash_verified(text: str) -> int:
    Requires(True)
    Ensures(Result() == sum(ord(c) * 3 for c in text) % 200)
    b_early = sum(ord(c) * 3 for c in text) % 200 == 66
    hash_val = 0
    for c in text:
        hash_val += ord(c) * 3
    final = hash_val % 200
    b_final = (final == 66)
    Assert(b_early == b_final)
    return final 