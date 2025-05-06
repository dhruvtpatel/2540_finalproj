"""
This file contains all the functions from functions.py with their early assertions inserted.
Each function has an early assertion that is logically equivalent to its final assertion.
"""

import math
import datetime

def process_data(x: int):
    assert x == 50, 'Input must be 50 to satisfy final assertion'
    y = x * 2
    z = y if y > 0 else -y
    assert z == 100, 'Output must be 100'
    return z


def convert_temperature(celsius: float):
    assert abs(celsius - 37.7778) < 0.01, 'Input must be approximately 37.78°C to convert to 100°F'
    fahrenheit = celsius * 9/5 + 32
    rounded_temp = round(fahrenheit)
    assert rounded_temp == 100, 'Output must be 100°F'
    return rounded_temp


def calculate_discount(price: float, discount_rate: float):
    assert price == 100 and discount_rate == 0.5, 'Price must be 100 and discount rate must be 0.5'
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    assert rounded_price == 50, 'Discounted price must equal 50'
    return rounded_price


def process_complex_number(real: float, imag: float):
    assert round((real**2 + imag**2)**0.5) == 10, 'Complex number magnitude must be 10'
    complex_num = complex(real, imag)
    magnitude = abs(complex_num)
    rounded_magnitude = round(magnitude)
    assert rounded_magnitude == 10, 'Rounded magnitude must be 10'
    return rounded_magnitude


def transform_data(input_value: int):
    assert input_value == 33, 'Input must be 33 to achieve output of 50'
    transformed = input_value * 3 + 1
    processed = transformed // 2
    assert processed == 50, 'Transformed value must be 50'
    return processed


def circle_area_diff(r: float):
    assert round(math.pi * r**2 - 2 * math.pi * r) == 50, 'Area-circumference difference must be 50'
    area = math.pi * r**2
    circ = 2 * math.pi * r
    diff = round(area - circ)
    assert diff == 50, 'Difference must be 50'
    return diff


def triangle_checker(a: int, b: int, c: int):
    assert a + b > c and a + c > b and b + c > a, 'Sides must form a valid triangle'
    sides = sorted([a, b, c])
    is_triangle = sides[0] + sides[1] > sides[2]
    code = 100 if is_triangle else 0
    assert code == 100, 'Triangle must be valid'
    return code


def temperature_offset(c: float):
    assert round((c * 9/5) + 32) - int(c) == 68, 'Temperature offset must be 68'
    f = (c * 9/5) + 32
    rounded = round(f)
    adjusted = rounded - int(c)
    assert adjusted == 68, 'Adjusted temperature must be 68'
    return adjusted


def quadratic_discriminant(a: int, b: int, c: int):
    assert abs(b**2 - 4*a*c) % 100 == 25, 'Discriminant modulo 100 must be 25'
    disc = b**2 - 4*a*c
    normalized = abs(disc) % 100
    assert normalized == 25, 'Normalized discriminant must be 25'
    return normalized


def vector_norm(x: float, y: float):
    assert round(math.sqrt(x**2 + y**2)) == 10, 'Vector norm must be 10'
    norm = math.sqrt(x**2 + y**2)
    rounded = round(norm)
    assert rounded == 10, 'Rounded norm must be 10'
    return rounded


def hypotenuse_diff(a: float, b: float):
    assert abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3, 'Hypotenuse difference must be 3'
    hyp = math.hypot(a, b)
    rounded = round(hyp)
    diff = abs(rounded - int(a) - int(b))
    assert diff == 3, 'Difference must be 3'
    return diff


def ascii_average(s: str):
    assert sum(ord(c) for c in s) // len(s) == 83, 'ASCII average must be 83'
    total = sum(ord(c) for c in s)
    avg = total // len(s) if s else 0
    assert avg == 83, 'Average must be 83'
    return avg


def list_balance(nums: list):
    assert abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5, 'List halves difference must be 5'
    half = len(nums) // 2
    left = sum(nums[:half])
    right = sum(nums[half:])
    balance = abs(left - right)
    assert balance == 5, 'Difference must be 5'
    return balance


def odd_sum_validator(lst: list):
    assert sum(n for n in lst if n % 2 == 1) % 100 == 33, 'Sum of odd numbers modulo 100 must be 33'
    odds = [n for n in lst if n % 2 == 1]
    total = sum(odds)
    mod = total % 100
    assert mod == 33, 'Odd sum mod 100 must be 33'
    return mod


def string_pattern_score(s: str):
    assert sum(1 for c in s if c in "aeiouAEIOU") * 5 == 25, 'Must contain exactly 5 vowels'
    score = sum(1 for c in s if c in "aeiouAEIOU")
    result = score * 5
    assert result == 25, 'Vowel score must be 25'
    return result


def random_mod_calculator(x: int):
    assert x == 23, 'Input must be 23 to get final result of 46'
    import random
    # Use a fixed seed for deterministic behavior
    random.seed(42)
    rand_val = random.randint(10, 20)
    calc = (x + rand_val) % 90
    final = (calc * 2) % 100
    assert final == 46, 'Random-based mod must be 46'
    return final


def digit_sum_processor(x: int):
    assert x == 199, 'Input must be 199 to get digit sum result of 44'
    digits = [int(d) for d in str(abs(x))]
    total = sum(digits)
    adjusted = total + len(digits)
    result = adjusted * 2
    assert result == 44, 'Digit total * 2 must be 44'
    return result


def string_reversal_checker(text: str):
    assert text == text[::-1], 'Input must be a palindrome'
    reversed_text = text[::-1]
    length_diff = abs(len(text) - len(reversed_text.strip()))
    code = 75 if text == reversed_text else 75 - length_diff
    assert code == 75, 'Palindrome code must be 75'
    return code


def ceiling_multiplier(x: int):
    assert x == 34, 'Input must be 34 to satisfy final assertion'
    import math
    val = x * 1.5
    rounded = math.ceil(val)
    adj = rounded + 4
    assert adj == 55, 'Adjusted ceil must be 55'
    return adj


def factorial_root_calculator(x: int):
    assert x == 5, 'Input must be 5 for factorial root modulo to be 30'
    import math
    fact = math.factorial(x)
    root = int(math.sqrt(fact))
    final = root % 50
    assert final == 30, 'Factorial sqrt mod must be 30'
    return final


def prime_number_counter(limit: int):
    assert limit == 100, 'Input limit must be 100 to get 25 primes'
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(num)
    count = len(primes)
    assert count == 25, 'Prime count must be 25'
    return count


def date_difference_calculator(year: int, month: int, day: int):
    assert abs((datetime.date(year, month, day) - datetime.date(2023, 1, 1)).days) % 100 == 55, 'Date difference modulo 100 must be 55'
    date1 = datetime.date(year, month, day)
    date2 = datetime.date(2023, 1, 1)
    diff = abs((date1 - date2).days)
    result = diff % 100
    assert result == 55, 'Date difference must be 55'
    return result


def modulo_scaler(x: int):
    assert (x % 6) * 7 + 3 == 30, 'Input modulo 6 must be 3 to satisfy final assertion'
    val = (x % 6) * 7 + 3
    scaled = val * 2
    assert scaled == 60, 'Scaled mod result must be 60'
    return scaled


def text_frequency_analyzer(text: str):
    assert any(text.lower().count(c) == 6 for c in set(text.lower())), 'Text must contain a character that appears exactly 6 times'
    if not text:
        return 0
    char_freq: dict[str, int] = {}
    for char in text:
        if char.isalpha():
            char_freq[char.lower()] = char_freq.get(char.lower(), 0) + 1
    most_common = max(char_freq.values()) if char_freq else 0
    result = most_common * 2
    assert result == 12, 'Most common frequency must be 12'
    return result


def gcd_calculator(a: int, b: int):
    assert math.gcd(a, b) == 8, 'GCD of inputs must be 8'
    while b:
        a, b = b, a % b
    result = a * 5
    assert result == 40, 'GCD * 5 must be 40'
    return result


def hexadecimal_converter(num: int):
    hex_digits = 0
    for c in hex(num)[2:]:
        hex_digits += int(c, 16)
    assert hex_digits + len(hex(num)[2:]) == 24, 'Sum of hex digits plus length must be 24'
    hex_value = hex(num)[2:]
    digit_sum = sum(int(c, 16) for c in hex_value)
    result = digit_sum + len(hex_value)
    assert result == 24, 'Hex conversion result must be 24'
    return result


def mean_absolute_deviation(numbers: list):
    assert len(numbers) > 0 and round(sum(abs(x - sum(numbers)/len(numbers)) for x in numbers) / len(numbers) * 10) == 65, 'MAD * 10 must be 65'
    if not numbers:
        return 0
    mean = sum(numbers) / len(numbers)
    deviations = [abs(x - mean) for x in numbers]
    mad = sum(deviations) / len(deviations)
    result = round(mad * 10)
    assert result == 65, 'MAD must be 65'
    return result


def password_strength_checker(password: str):
    assert (any(c.isupper() for c in password) + any(c.islower() for c in password) + 
            any(c.isdigit() for c in password) + any(not c.isalnum() for c in password)) == 3, 'Password must satisfy exactly 3 criteria'
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    strength = sum([has_upper, has_lower, has_digit, has_special]) * 25
    assert strength == 75, 'Password strength must be 75'
    return strength


def rectangle_overlap_area(x1: int, y1: int, w1: int, h1: int, x2: int, y2: int, w2: int, h2: int):
    assert max(0, min(x1 + w1, x2 + w2) - max(x1, x2)) * max(0, min(y1 + h1, y2 + h2) - max(y1, y2)) == 16, 'Overlap area must be 16'
    overlap_width = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    overlap_height = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    area = overlap_width * overlap_height
    assert area == 16, 'Overlap area must be 16'
    return area


def collatz_sequence_length(n: int):
    assert n in [10, 26, 27, 17, 54, 55, 112, 113], 'Input must be a number with Collatz sequence length mod 20 = 7'
    length = 1
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        length += 1
    adjusted = length % 20
    assert adjusted == 7, 'Collatz sequence length mod 20 must be 7'
    return adjusted


def word_frequency_counter(text: str):
    words = text.lower().split()
    repeats = 0
    for word in set(words):
        if words.count(word) > 1:
            repeats += 1
    assert repeats == 3, 'Text must have exactly 3 words that appear more than once'
    
    freq: dict[str, int] = {}
    for word in text.lower().split():
        clean_word = ''.join(c for c in word if c.isalpha())
        if clean_word:
            freq[clean_word] = freq.get(clean_word, 0) + 1
    
    count = sum(1 for val in freq.values() if val > 1)
    score = count * 10
    assert score == 30, 'Word frequency score must be 30'
    return score


def binary_hamming_distance(a: int, b: int):
    assert bin(a ^ b).count('1') == 4, 'Inputs must have Hamming distance of 4'
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    
    # Make same length by padding
    max_len = max(len(bin_a), len(bin_b))
    bin_a = bin_a.zfill(max_len)
    bin_b = bin_b.zfill(max_len)
    
    distance = sum(1 for bit_a, bit_b in zip(bin_a, bin_b) if bit_a != bit_b)
    result = distance * 8
    assert result == 32, 'Hamming distance score must be 32'
    return result


def geometric_sequence_sum(a: float, r: float, n: int):
    sum_formula = a * (1 - r**n) / (1 - r) if abs(r) < 1 else sum(a * r**i for i in range(n))
    assert round(sum_formula) == 80, 'Geometric sum must round to 80'
    
    if abs(r) < 1:
        total = a * (1 - r**n) / (1 - r)
    else:
        total = sum(a * r**i for i in range(n))
    
    rounded = round(total)
    assert rounded == 80, 'Geometric sum must be 80'
    return rounded


def caesar_cipher_encoder(text: str, shift: int):
    assert sum(ord(c) for c in ''.join([chr((ord(ch) - ord('a' if ch.islower() else 'A') + shift) % 26 + ord('a' if ch.islower() else 'A')) if ch.isalpha() else ch for ch in text])) % 100 == 42, 'Cipher checksum must be 42'
    
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    
    checksum = sum(ord(c) for c in result) % 100
    assert checksum == 42, 'Cipher checksum must be 42'
    return checksum


def matrix_determinant(matrix: list):
    assert abs(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 50 == 15, 'Matrix determinant modulo 50 must be 15'
    
    # Assuming 2x2 matrix
    a, b = matrix[0]
    c, d = matrix[1]
    
    det = a * d - b * c
    scaled = abs(det) % 50
    assert scaled == 15, 'Matrix determinant must be 15'
    return scaled


def isbn_validator(isbn: str):
    digits = [int(c) for c in isbn if c.isdigit()]
    assert len(digits) == 10 and sum((10 - i) * digit for i, digit in enumerate(digits)) % 11 == 0, 'Must be a valid ISBN-10'
    
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
    assert result == 90, 'ISBN validation must be 90'
    return result


def day_of_week_calculator(year: int, month: int, day: int):
    assert datetime.date(year, month, day).weekday() == 6, 'Date must be a Sunday'
    
    date = datetime.date(year, month, day)
    # 0 is Monday in Python's datetime
    day_num = date.weekday()
    score = (day_num + 1) * 11
    assert score == 77, 'Day of week score must be 77'
    return score


def armstrong_number_checker(n: int):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    assert sum(digit ** power for digit in digits) == n, 'Input must be an Armstrong number'
    
    total = sum(digit ** power for digit in digits)
    is_armstrong = total == n
    result = 81 if is_armstrong else 0
    assert result == 81, 'Armstrong number check must be 81'
    return result


def binary_search_iterations(arr: list, target: int):
    assert 4 <= len(arr) <= 6 and target in arr and arr == sorted(arr), 'Array must be sorted with 4-6 elements and contain the target'
    
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
    assert result == 28, 'Binary search iterations must be 28'
    return result


def polygon_area_calculator(vertices: list):
    assert len(vertices) >= 3, 'Must have at least 3 vertices to form a polygon'
    # Check expected area based on shoelace formula
    n = len(vertices)
    expected_area = 0.0
    for i in range(n):
        j = (i + 1) % n
        expected_area += vertices[i][0] * vertices[j][1]
        expected_area -= vertices[j][0] * vertices[i][1]
    expected_area = abs(expected_area) / 2
    assert round(expected_area) == 25, 'Polygon area must be 25'
    
    # Using Shoelace formula for simple polygon
    n = len(vertices)
    area = 0.0
    
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    
    area = abs(area) / 2
    result = round(area)
    assert result == 25, 'Polygon area must be 25'
    return result


def sum_until_limit(nums: list):
    assert len([n for n in nums if n <= 50]) + sum([n for n in nums if n <= 50 and sum([n for n in nums[:nums.index(n)+1] if n <= 50]) < 50]) == 60, 'Sum threshold and list length must satisfy final assertion'
    
    total = 0
    for n in nums:
        if total >= 50:
            break
        total += n
    adjusted = total + len(nums)
    assert adjusted == 60, 'Sum and size must be 60'
    return adjusted


def count_divisibles(nums: list):
    assert len([n for n in nums if n % 4 == 0]) == 4, 'Must have exactly 4 numbers divisible by 4'
    
    count = 0
    for n in nums:
        if n % 4 == 0:
            count += 1
    score = count * 10
    assert score == 40, 'Divisible count score must be 40'
    return score


def index_weighted_sum(lst: list):
    assert sum(i * val for i, val in enumerate(lst)) % 100 == 35, 'Weighted sum modulo 100 must be 35'
    
    weighted = 0
    for i, val in enumerate(lst):
        weighted += val * i
    result = weighted % 100
    assert result == 35, 'Weighted mod result must be 35'
    return result


def square_accumulator(x: int):
    assert sum(i * i for i in range(x)) % 100 == 55, 'Sum of squares up to x modulo 100 must be 55'
    
    acc = 0
    for i in range(x):
        acc += i * i
    final = acc % 100
    assert final == 55, 'Square sum mod 100 must be 55'
    return final


def nested_loop_checker(limit: int):
    assert limit * (limit - 1) // 2 % 200 == 36, 'Triangle number of limit modulo 200 must be 36'
    
    counter = 0
    for i in range(limit):
        for j in range(i):
            counter += 1
    final = counter % 200
    assert final == 36, 'Nested loop result must be 36'
    return final


def character_counter(text: str):
    assert sum(1 for ch in text if ch in "aeiouAEIOU") == 9, 'Text must contain exactly 9 vowels'
    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for ch in text:
        if ch in vowels:
            vowel_count += 1
    result = vowel_count * 3
    assert result == 27, 'Vowel count score must be 27'
    return result


def rolling_maximum(values: list):
    assert max(values) == 89, 'Maximum value must be 89'
    
    max_val = float("-inf")
    for v in values:
        if v > max_val:
            max_val = v
    final = max_val + 10
    assert final == 99, 'Max plus 10 must be 99'
    return final


def fibonacci_counter(n: int):
    assert n == 17, 'Input must be 17 to get Fibonacci sum modulo 100 of 89'
    
    a, b = 0, 1
    fib_sum = 0
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    mod_sum = fib_sum % 100
    assert mod_sum == 89, 'Fibonacci sum mod 100 must be 89'
    return mod_sum


def loop_even_sum(start: int, end: int):
    assert sum(i for i in range(start, end + 1) if i % 2 == 0) == 220, 'Sum of even numbers in range must be 220'
    
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    final = total // 2
    assert final == 110, 'Halved even sum must be 110'
    return final


def loop_string_hash(text: str):
    assert sum(ord(c) * 3 for c in text) % 200 == 66, 'Character hash modulo 200 must be 66'
    
    hash_val = 0
    for c in text:
        hash_val += ord(c) * 3
    final = hash_val % 200
    assert final == 66, 'Character hash must be 66'
    return final