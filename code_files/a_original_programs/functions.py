# 1. Simple Multiplication Processor
def process_data(x: int):
    # Early Assert HERE
    y = x * 2
    if y > 0:
        z = y
    else:
        z = -y
    assert z == 100, "Final check: z must equal 100"
    return z


# 2. Temperature Converter
def convert_temperature(celsius: float):
    # Early Assert HERE
    fahrenheit = (celsius * 9 / 5) + 32
    rounded_temp = round(fahrenheit)
    assert rounded_temp == 100, "Final check: converted temperature must be exactly 100"
    return rounded_temp


# 3. Shopping Discount Calculator
def calculate_discount(price: float, discount_rate: float):
    # Early Assert HERE
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    assert rounded_price == 50, "Final check: discounted price must be exactly 50"
    return rounded_price


# 4. Complex Number Processing
def process_complex_number(real: float, imag: float):
    # Early Assert HERE
    complex_num = complex(real, imag)
    magnitude = abs(complex_num)
    rounded_magnitude = round(magnitude)
    assert rounded_magnitude == 10, "Final check: magnitude must be exactly 10"
    return rounded_magnitude


# 5. Data Transformation Function
def transform_data(input_value: int):
    # Early Assert HERE
    transformed = input_value * 3 + 1
    processed = transformed // 2
    assert processed == 50, "Final check: processed value must be exactly 50"
    return processed


# 6. Circle Area Diff
def circle_area_diff(r: float):
    # Early Assert HERE
    import math

    area = math.pi * r**2
    circ = 2 * math.pi * r
    diff = round(area - circ)
    assert diff == 50, "Final check: area minus circumference must be 50"
    return diff


# 7. Triangle Checker
def triangle_checker(a: int, b: int, c: int):
    # Early Assert HERE
    sides = sorted([a, b, c])
    is_triangle = sides[0] + sides[1] > sides[2]
    code = 100 if is_triangle else 0
    assert code == 100, "Final check: must be a triangle"
    return code


# 8. Temperature Offset
def temperature_offset(c: float):
    # Early Assert HERE
    f = (c * 9 / 5) + 32
    rounded = round(f)
    adjusted = rounded - int(c)
    assert adjusted == 68, "Final check: adjusted temp must be 68"
    return adjusted


# 9. Quadratic Discriminant
def quadratic_discriminant(a: int, b: int, c: int):
    # Early Assert HERE
    disc = b**2 - 4 * a * c
    normalized = abs(disc) % 100
    assert normalized == 25, "Final check: normalized discriminant must be 25"
    return normalized


# 10. Vector Norm
def vector_norm(x: float, y: float):
    # Early Assert HERE
    import math

    norm = math.sqrt(x**2 + y**2)
    rounded = round(norm)
    assert rounded == 10, "Final check: norm must be 10"
    return rounded


# 11. Hypotenuse Diff
def hypotenuse_diff(a: float, b: float):
    # Early Assert HERE
    import math

    hyp = math.hypot(a, b)
    rounded = round(hyp)
    diff = abs(rounded - int(a) - int(b))
    assert diff == 3, "Final check: diff must be 3"
    return diff


# 12. Ascii Average
def ascii_average(s: str):
    # Early Assert HERE
    total = sum(ord(c) for c in s)
    avg = total // len(s) if s else 0
    assert avg == 83, "Final check: average ASCII must be 83"
    return avg


# 13. List Balance
def list_balance(nums: list):
    # Early Assert HERE
    half = len(nums) // 2
    left = sum(nums[:half])
    right = sum(nums[half:])
    balance = abs(left - right)
    assert balance == 5, "Final check: list halves balance to 5"
    return balance


# 14. Odd Sum Validator
def odd_sum_validator(lst: list):
    # Early Assert HERE
    odds = [n for n in lst if n % 2 == 1]
    total = sum(odds)
    mod = total % 100
    assert mod == 33, "Final check: odd sum mod 100 must be 33"
    return mod


# 15. String Pattern Score
def string_pattern_score(s: str):
    # Early Assert HERE
    score = sum(1 for c in s if c in "aeiouAEIOU")
    result = score * 5
    assert result == 25, "Final check: vowel score must be 25"
    return result


# 16. Random Mod Calculator
def random_mod_calculator(x: int):
    # Early Assert HERE
    import random

    rand_val = random.randint(10, 20)
    calc = (x + rand_val) % 90
    final = (calc * 2) % 100
    assert final == 46, "Final check: random-based mod must be 46"
    return final


# 17. Digit Sum Processor
def digit_sum_processor(x: int):
    # Early Assert HERE
    digits = [int(d) for d in str(abs(x))]
    total = sum(digits)
    adjusted = total + len(digits)
    result = adjusted * 2
    assert result == 44, "Final check: digit total * 2 must be 44"
    return result


# 18. String Reversal Checker
def string_reversal_checker(text: str):
    # Early Assert HERE
    reversed_text = text[::-1]
    length_diff = abs(len(text) - len(reversed_text.strip()))
    code = 75 if text == reversed_text else 75 - length_diff
    assert code == 75, "Final check: palindrome code must be 75"
    return code


# 19. Ceiling Multiplier
def ceiling_multiplier(x: int):
    # Early Assert HERE
    import math

    val = x * 1.5
    rounded = math.ceil(val)
    adj = rounded + 4
    assert adj == 55, "Final check: adjusted ceil must be 55"
    return adj


# 20. Factorial Root Calculator
def factorial_root_calculator(x: int):
    # Early Assert HERE
    import math

    fact = math.factorial(x)
    root = int(math.sqrt(fact))
    final = root % 50
    assert final == 30, "Final check: factorial sqrt mod must be 30"
    return final


# 21. Prime Number Counter
def prime_number_counter(limit: int):
    # Early Assert HERE
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(num)
    count = len(primes)
    assert count == 25, "Final check: prime count must be 25"
    return count


# 22. Date Difference Calculator
def date_difference_calculator(year: int, month: int, day: int):
    # Early Assert HERE
    import datetime
    
    date1 = datetime.date(year, month, day)
    date2 = datetime.date(2023, 1, 1)
    diff = abs((date1 - date2).days)
    result = diff % 100
    assert result == 55, "Final check: date difference must be 55"
    return result


# 23. Modulo Scaler
def modulo_scaler(x: int):
    # Early Assert HERE
    val = (x % 6) * 7 + 3
    scaled = val * 2
    assert scaled == 60, "Final check: scaled mod result must be 60"
    return scaled


# 24. Text Frequency Analyzer
def text_frequency_analyzer(text: str):
    # Early Assert HERE
    if not text:
        return 0
    char_freq: dict[str, int] = {}
    for char in text:
        if char.isalpha():
            char_freq[char.lower()] = char_freq.get(char.lower(), 0) + 1
    most_common = max(char_freq.values()) if char_freq else 0
    result = most_common * 2
    assert result == 12, "Final check: most common frequency must be 12"
    return result


# 25. GCD Calculator
def gcd_calculator(a: int, b: int):
    # Early Assert HERE
    while b:
        a, b = b, a % b
    result = a * 5
    assert result == 40, "Final check: GCD * 5 must be 40"
    return result


# 26. Hexadecimal Converter
def hexadecimal_converter(num: int):
    # Early Assert HERE
    hex_value = hex(num)[2:]
    digit_sum = sum(int(c, 16) for c in hex_value)
    result = digit_sum + len(hex_value)
    assert result == 24, "Final check: hex conversion result must be 24"
    return result


# 27. Mean Absolute Deviation
def mean_absolute_deviation(numbers: list):
    # Early Assert HERE
    if not numbers:
        return 0
    mean = sum(numbers) / len(numbers)
    deviations = [abs(x - mean) for x in numbers]
    mad = sum(deviations) / len(deviations)
    result = round(mad * 10)
    assert result == 65, "Final check: MAD must be 65"
    return result


# 28. Password Strength Checker
def password_strength_checker(password: str):
    # Early Assert HERE
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    strength = sum([has_upper, has_lower, has_digit, has_special]) * 25
    assert strength == 75, "Final check: password strength must be 75"
    return strength


# 29. Rectangle Overlap Area
def rectangle_overlap_area(x1: int, y1: int, w1: int, h1: int, x2: int, y2: int, w2: int, h2: int):
    # Early Assert HERE
    overlap_width = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    overlap_height = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    area = overlap_width * overlap_height
    assert area == 16, "Final check: overlap area must be 16"
    return area


# 30. Collatz Sequence Length
def collatz_sequence_length(n: int):
    # Early Assert HERE
    length = 1
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        length += 1
    adjusted = length % 20
    assert adjusted == 7, "Final check: Collatz sequence length mod 20 must be 7"
    return adjusted


# 31. Word Frequency Counter
def word_frequency_counter(text: str):
    # Early Assert HERE
    words = text.lower().split()
    freq: dict[str, int] = {}
    for word in words:
        clean_word = ''.join(c for c in word if c.isalpha())
        if clean_word:
            freq[clean_word] = freq.get(clean_word, 0) + 1
    
    count = sum(1 for val in freq.values() if val > 1)
    score = count * 10
    assert score == 30, "Final check: word frequency score must be 30"
    return score


# 32. Binary Hamming Distance
def binary_hamming_distance(a: int, b: int):
    # Early Assert HERE
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    
    # Make same length by padding
    max_len = max(len(bin_a), len(bin_b))
    bin_a = bin_a.zfill(max_len)
    bin_b = bin_b.zfill(max_len)
    
    distance = sum(1 for bit_a, bit_b in zip(bin_a, bin_b) if bit_a != bit_b)
    result = distance * 8
    assert result == 32, "Final check: hamming distance score must be 32"
    return result


# 33. Geometric Sequence Sum
def geometric_sequence_sum(a: float, r: float, n: int):
    # Early Assert HERE
    if abs(r) < 1:
        total = a * (1 - r**n) / (1 - r)
    else:
        total = sum(a * r**i for i in range(n))
    
    rounded = round(total)
    assert rounded == 80, "Final check: geometric sum must be 80"
    return rounded


# 34. Caesar Cipher Encoder
def caesar_cipher_encoder(text: str, shift: int):
    # Early Assert HERE
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    
    checksum = sum(ord(c) for c in result) % 100
    assert checksum == 42, "Final check: cipher checksum must be 42"
    return checksum


# 35. Matrix Determinant
def matrix_determinant(matrix: list):
    # Early Assert HERE
    # Assuming 2x2 matrix
    a, b = matrix[0]
    c, d = matrix[1]
    
    det = a * d - b * c
    scaled = abs(det) % 50
    assert scaled == 15, "Final check: matrix determinant must be 15"
    return scaled


# 36. ISBN Validator
def isbn_validator(isbn: str):
    # Early Assert HERE
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
    assert result == 90, "Final check: ISBN validation must be 90"
    return result


# 37. Day of Week Calculator
def day_of_week_calculator(year: int, month: int, day: int):
    # Early Assert HERE
    import datetime
    
    date = datetime.date(year, month, day)
    # 0 is Monday in Python's datetime
    day_num = date.weekday()
    score = (day_num + 1) * 11
    assert score == 77, "Final check: day of week score must be 77"
    return score


# 38. Armstrong Number Checker
def armstrong_number_checker(n: int):
    # Early Assert HERE
    digits = [int(d) for d in str(n)]
    power = len(digits)
    total = sum(digit ** power for digit in digits)
    is_armstrong = total == n
    result = 81 if is_armstrong else 0
    assert result == 81, "Final check: Armstrong number check must be 81"
    return result


# 39. Binary Search Iterations
def binary_search_iterations(arr: list, target: int):
    # Early Assert HERE
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
    assert result == 28, "Final check: binary search iterations must be 28"
    return result


# 40. Polygon Area Calculator
def polygon_area_calculator(vertices: list):
    # Early Assert HERE
    # Using Shoelace formula for simple polygon
    n = len(vertices)
    area = 0.0
    
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    
    area = abs(area) / 2
    result = round(area)
    assert result == 25, "Final check: polygon area must be 25"
    return result


# 41. Sum Until Limit
def sum_until_limit(nums: list):
    # Early Assert HERE
    total = 0
    for n in nums:
        if total >= 50:
            break
        total += n
    adjusted = total + len(nums)
    assert adjusted == 60, "Final check: sum and size must be 60"
    return adjusted


# 42. Count Divisibles
def count_divisibles(nums: list):
    # Early Assert HERE
    count = 0
    for n in nums:
        if n % 4 == 0:
            count += 1
    score = count * 10
    assert score == 40, "Final check: divisible count score must be 40"
    return score


# 43. Index Weighted Sum
def index_weighted_sum(lst: list):
    # Early Assert HERE
    weighted = 0
    for i, val in enumerate(lst):
        weighted += val * i
    result = weighted % 100
    assert result == 35, "Final check: weighted mod result must be 35"
    return result


# 44. Square Accumulator
def square_accumulator(x: int):
    # Early Assert HERE
    acc = 0
    for i in range(x):
        acc += i * i
    final = acc % 100
    assert final == 55, "Final check: square sum mod 100 must be 55"
    return final


# 45. Nested Loop Checker
def nested_loop_checker(limit: int):
    # Early Assert HERE
    counter = 0
    for i in range(limit):
        for j in range(i):
            counter += 1
    final = counter % 200
    assert final == 36, "Final check: nested loop result must be 36"
    return final


# 46. Character Counter
def character_counter(text: str):
    # Early Assert HERE
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for ch in text:
        if ch in vowels:
            vowel_count += 1
    result = vowel_count * 3
    assert result == 27, "Final check: vowel count score must be 27"
    return result


# 47. Rolling Maximum
def rolling_maximum(values: list):
    # Early Assert HERE
    max_val = float("-inf")
    for v in values:
        if v > max_val:
            max_val = v
    final = max_val + 10
    assert final == 99, "Final check: max plus 10 must be 99"
    return final


# 48. Fibonacci Counter
def fibonacci_counter(n: int):
    # Early Assert HERE
    a, b = 0, 1
    fib_sum = 0
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    mod_sum = fib_sum % 100
    assert mod_sum == 89, "Final check: Fibonacci sum mod 100 must be 89"
    return mod_sum


# 49. Loop Even Sum
def loop_even_sum(start: int, end: int):
    # Early Assert HERE
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    final = total // 2
    assert final == 110, "Final check: halved even sum must be 110"
    return final


# 50. Loop String Hash
def loop_string_hash(text: str):
    # Early Assert HERE
    hash_val = 0
    for c in text:
        hash_val += ord(c) * 3
    final = hash_val % 200
    assert final == 66, "Final check: character hash must be 66"
    return final
