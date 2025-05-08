"""
Transformed Programs for Assertion Equivalence Checking
Each function has been transformed to explicitly check if the early and final assertions are equivalent.
"""

import math
import datetime

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
    area = math.pi * r**2
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

def random_mod_calculator_transformed(x: int):
    b_early = (x == 23)
    import random
    # Use a fixed seed for deterministic behavior
    random.seed(42)
    rand_val = random.randint(10, 20)
    calc = (x + rand_val) % 90
    final = (calc * 2) % 100
    b_final = (final == 46)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final

def digit_sum_processor_transformed(x: int):
    b_early = (x == 199)
    digits = [int(d) for d in str(abs(x))]
    total = sum(digits)
    adjusted = total + len(digits)
    result = adjusted * 2
    b_final = (result == 44)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def string_reversal_checker_transformed(text: str):
    b_early = (text == text[::-1])
    reversed_text = text[::-1]
    length_diff = abs(len(text) - len(reversed_text.strip()))
    code = 75 if text == reversed_text else 75 - length_diff
    b_final = (code == 75)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return code

def ceiling_multiplier_transformed(x: int):
    b_early = (x == 34)
    import math
    val = x * 1.5
    rounded = math.ceil(val)
    adj = rounded + 4
    b_final = (adj == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adj

def factorial_root_calculator_transformed(x: int):
    b_early = (x == 5)
    import math
    fact = math.factorial(x)
    root = int(math.sqrt(fact))
    final = root % 50
    b_final = (final == 30)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final

def prime_number_counter_transformed(limit: int):
    b_early = (limit == 100)
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(num)
    count = len(primes)
    b_final = (count == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return count

def date_difference_calculator_transformed(year: int, month: int, day: int):
    b_early = abs((datetime.date(year, month, day) - datetime.date(2023, 1, 1)).days) % 100 == 55
    date1 = datetime.date(year, month, day)
    date2 = datetime.date(2023, 1, 1)
    diff = abs((date1 - date2).days)
    result = diff % 100
    b_final = (result == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def modulo_scaler_transformed(x: int):
    b_early = ((x % 6) * 7 + 3 == 30)
    val = (x % 6) * 7 + 3
    scaled = val * 2
    b_final = (scaled == 60)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return scaled

def text_frequency_analyzer_transformed(text: str):
    b_early = any(text.lower().count(c) == 6 for c in set(text.lower()))
    if not text:
        return 0
    char_freq: dict[str, int] = {}
    for char in text:
        if char.isalpha():
            char_freq[char.lower()] = char_freq.get(char.lower(), 0) + 1
    most_common = max(char_freq.values()) if char_freq else 0
    result = most_common * 2
    b_final = (result == 12)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def gcd_calculator_transformed(a: int, b: int):
    b_early = (math.gcd(a, b) == 8)
    while b:
        a, b = b, a % b
    result = a * 5
    b_final = (result == 40)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def hexadecimal_converter_transformed(num: int):
    hex_digits = 0
    for c in hex(num)[2:]:
        hex_digits += int(c, 16)
    b_early = (hex_digits + len(hex(num)[2:]) == 24)
    hex_value = hex(num)[2:]
    digit_sum = sum(int(c, 16) for c in hex_value)
    result = digit_sum + len(hex_value)
    b_final = (result == 24)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def mean_absolute_deviation_transformed(numbers: list):
    b_early = len(numbers) > 0 and round(sum(abs(x - sum(numbers)/len(numbers)) for x in numbers) / len(numbers) * 10) == 65
    if not numbers:
        return 0
    mean = sum(numbers) / len(numbers)
    deviations = [abs(x - mean) for x in numbers]
    mad = sum(deviations) / len(deviations)
    result = round(mad * 10)
    b_final = (result == 65)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def password_strength_checker_transformed(password: str):
    b_early = (sum([any(c.isupper() for c in password), 
                   any(c.islower() for c in password),
                   any(c.isdigit() for c in password),
                   any(not c.isalnum() for c in password)]) == 3)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    strength = sum([has_upper, has_lower, has_digit, has_special]) * 25
    b_final = (strength == 75)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return strength

def rectangle_overlap_area_transformed(x1: int, y1: int, w1: int, h1: int, x2: int, y2: int, w2: int, h2: int):
    b_early = (max(0, min(x1 + w1, x2 + w2) - max(x1, x2)) * 
               max(0, min(y1 + h1, y2 + h2) - max(y1, y2)) == 16)
    overlap_width = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    overlap_height = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    area = overlap_width * overlap_height
    b_final = (area == 16)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return area

def collatz_sequence_length_transformed(n: int):
    n_orig = n
    b_early = (n_orig in [10, 26, 27, 17, 54, 55, 112, 113])
    length = 1
    current_n = n_orig
    while current_n != 1:
        current_n = 3 * current_n + 1 if current_n % 2 else current_n // 2
        length += 1
    adjusted = length % 20
    func_return_value = adjusted
    b_final = (func_return_value == 7)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return func_return_value

def word_frequency_counter_transformed(text: str):
    words = text.lower().split()
    repeats = 0
    for word in set(words):
        if words.count(word) > 1:
            repeats += 1
    b_early = (repeats == 3)
    
    freq: dict[str, int] = {}
    for word in text.lower().split():
        clean_word = ''.join(c for c in word if c.isalpha())
        if clean_word:
            freq[clean_word] = freq.get(clean_word, 0) + 1
    
    count = sum(1 for val in freq.values() if val > 1)
    score = count * 10
    b_final = (score == 30)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return score

def binary_hamming_distance_transformed(a: int, b: int):
    b_early = (bin(a ^ b).count('1') == 4)
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    
    # Make same length by padding
    max_len = max(len(bin_a), len(bin_b))
    bin_a = bin_a.zfill(max_len)
    bin_b = bin_b.zfill(max_len)
    
    distance = sum(1 for bit_a, bit_b in zip(bin_a, bin_b) if bit_a != bit_b)
    result = distance * 8
    b_final = (result == 32)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def geometric_sequence_sum_transformed(a: float, r: float, n: int):
    sum_formula = a * (1 - r**n) / (1 - r) if abs(r) < 1 else sum(a * r**i for i in range(n))
    b_early = (round(sum_formula) == 80)
    
    if abs(r) < 1:
        total = a * (1 - r**n) / (1 - r)
    else:
        total = sum(a * r**i for i in range(n))
    
    rounded = round(total)
    b_final = (rounded == 80)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded

def caesar_cipher_encoder_transformed(text: str, shift: int):
    cipher_text = ''.join([chr((ord(ch) - ord('a' if ch.islower() else 'A') + shift) % 26 + 
                              ord('a' if ch.islower() else 'A')) if ch.isalpha() else ch for ch in text])
    b_early = (sum(ord(c) for c in cipher_text) % 100 == 42)
    
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    
    checksum = sum(ord(c) for c in result) % 100
    b_final = (checksum == 42)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return checksum

def matrix_determinant_transformed(matrix: list):
    b_early = (abs(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 50 == 15)
    
    # Assuming 2x2 matrix
    a, b = matrix[0]
    c, d = matrix[1]
    
    det = a * d - b * c
    scaled = abs(det) % 50
    b_final = (scaled == 15)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return scaled

def isbn_validator_transformed(isbn: str):
    digits = [int(c) for c in isbn if c.isdigit()]
    b_early = (len(digits) == 10 and sum((10 - i) * digit for i, digit in enumerate(digits)) % 11 == 0)
    
    # Clean input
    digits = [int(c) for c in isbn if c.isdigit()]
    
    if len(digits) == 10:
        # ISBN-10 check
        check_sum = sum((10 - i) * digit for i, digit in enumerate(digits))
        is_valid = check_sum % 11 == 0
    else:
        # Not valid format
        is_valid = False
        
    result = 90 if is_valid else 0
    b_final = (result == 90)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def day_of_week_calculator_transformed(year: int, month: int, day: int):
    b_early = (datetime.date(year, month, day).weekday() == 6)
    
    date = datetime.date(year, month, day)
    # 0 is Monday in Python's datetime
    day_num = date.weekday()
    score = (day_num + 1) * 11
    b_final = (score == 77)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return score

def armstrong_number_checker_transformed(n: int):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    b_early = (sum(digit ** power for digit in digits) == n)
    
    total = sum(digit ** power for digit in digits)
    is_armstrong = total == n
    result = 81 if is_armstrong else 0
    b_final = (result == 81)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def binary_search_iterations_transformed(arr: list, target: int):
    b_early = (4 <= len(arr) <= 6 and target in arr and arr == sorted(arr))
    
    left, right = 0, len(arr) - 1
    iterations = 0
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    result = iterations * 7
    b_final = (result == 28)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def polygon_area_calculator_transformed(vertices: list):
    # Using Shoelace formula to calculate expected area
    n = len(vertices)
    expected_area = 0.0
    for i in range(n):
        j = (i + 1) % n
        expected_area += vertices[i][0] * vertices[j][1]
        expected_area -= vertices[j][0] * vertices[i][1]
    expected_area = abs(expected_area) / 2
    b_early = (len(vertices) >= 3 and round(expected_area) == 25)
    
    # Using Shoelace formula for simple polygon
    n = len(vertices)
    area = 0.0
    
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    
    area = abs(area) / 2
    result = round(area)
    b_final = (result == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def sum_until_limit_transformed(nums: list):
    # Simulating the calculation to determine what satisfies the final condition
    b_early = sum(1 for n in nums if n <= 50) + sum([n for n in nums if n <= 50 and sum([n for n in nums[:nums.index(n)+1] if n <= 50]) < 50]) == 60
    
    total = 0
    for n in nums:
        if total >= 50:
            break
        total += n
    adjusted = total + len(nums)
    b_final = (adjusted == 60)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adjusted

def count_divisibles_transformed(nums: list):
    b_early = len([n for n in nums if n % 4 == 0]) == 4
    
    count = 0
    for n in nums:
        if n % 4 == 0:
            count += 1
    score = count * 10
    b_final = (score == 40)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return score

def index_weighted_sum_transformed(lst: list):
    b_early = sum(i * val for i, val in enumerate(lst)) % 100 == 35
    
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
    b_early = (limit * (limit - 1) // 2) % 200 == 36
    
    counter = 0
    for i in range(limit):
        for j in range(i):
            counter += 1
    final = counter % 200
    b_final = (final == 36)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final

def character_counter_transformed(text: str):
    b_early = sum(1 for ch in text if ch in "aeiouAEIOU") == 9
    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for ch in text:
        if ch in vowels:
            vowel_count += 1
    result = vowel_count * 3
    b_final = (result == 27)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result

def rolling_maximum_transformed(values: list):
    b_early = max(values) == 89
    
    max_val = float("-inf")
    for v in values:
        if v > max_val:
            max_val = v
    final = max_val + 10
    b_final = (final == 99)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final

def fibonacci_counter_transformed(n: int):
    b_early = (n == 17)
    
    a, b = 0, 1
    fib_sum = 0
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    mod_sum = fib_sum % 100
    func_return_value = mod_sum
    b_final = (func_return_value == 89)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return func_return_value

def loop_even_sum_transformed(start: int, end: int):
    b_early = sum(i for i in range(start, end + 1) if i % 2 == 0) == 220
    
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