"""
This file contains all the functions from functions.py with their early assertions inserted.
Each function has an early assertion that is logically equivalent to its final assertion.
"""

import math

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
    assert round((real*2 + imag*2)**0.5) == 10, 'Complex number magnitude must be 10'
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
    area = math.pi * r ** 2
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
    diff = abs(left - right)
    assert diff == 5, 'Difference must be 5'
    return diff


def odd_sum_validator(nums: list):
    assert sum(x for x in nums if x % 2 == 1) == 100, 'Sum of odd numbers must be 100'
    odd_sum = sum(x for x in nums if x % 2 == 1)
    assert odd_sum == 100, 'Sum must be 100'
    return odd_sum


def string_pattern_score(s: str):
    assert sum(ord(c) - ord('a') + 1 for c in s.lower() if c.isalpha()) == 50, 'Pattern score must be 50'
    score = sum(ord(c) - ord('a') + 1 for c in s.lower() if c.isalpha())
    assert score == 50, 'Score must be 50'
    return score


def sum_until_limit(nums: list, limit: int):
    assert sum(x for x in nums if x <= limit) == 100, 'Sum of numbers up to limit must be 100'
    filtered_sum = sum(x for x in nums if x <= limit)
    assert filtered_sum == 100, 'Sum must be 100'
    return filtered_sum


def count_divisibles(nums: list, divisor: int):
    assert len([x for x in nums if x % divisor == 0]) == 5, 'Must have exactly 5 numbers divisible by divisor'
    count = len([x for x in nums if x % divisor == 0])
    assert count == 5, 'Count must be 5'
    return count


def index_weighted_sum(nums: list):
    assert sum(i * x for i, x in enumerate(nums, 1)) == 100, 'Index-weighted sum must be 100'
    weighted_sum = sum(i * x for i, x in enumerate(nums, 1))
    assert weighted_sum == 100, 'Sum must be 100'
    return weighted_sum


def square_accumulator(nums: list):
    assert sum(x * x for x in nums) == 100, 'Sum of squares must be 100'
    square_sum = sum(x * x for x in nums)
    assert square_sum == 100, 'Sum must be 100'
    return square_sum


def nested_loop_checker(matrix: list):
    assert sum(sum(row) for row in matrix) == 100, 'Sum of all elements must be 100'
    total = sum(sum(row) for row in matrix)
    assert total == 100, 'Total must be 100'
    return total


def character_counter(s: str, target: str):
    assert s.count(target) == 5, 'Must have exactly 5 occurrences of target character'
    count = s.count(target)
    assert count == 5, 'Count must be 5'
    return count


def rolling_maximum(nums: list):
    assert all(max(nums[:i+1]) == i+1 for i in range(len(nums))), 'Each prefix must have maximum equal to its length'
    result = all(max(nums[:i+1]) == i+1 for i in range(len(nums)))
    assert result, 'All prefix maximums must match their lengths'
    return result


def fibonacci_counter(nums: list):
    assert len([x for x in nums if x in [1, 1, 2, 3, 5, 8, 13, 21]]) == 5, 'Must have exactly 5 Fibonacci numbers'
    count = len([x for x in nums if x in [1, 1, 2, 3, 5, 8, 13, 21]])
    assert count == 5, 'Count must be 5'
    return count


def loop_even_sum(nums: list):
    assert sum(x for x in nums if x % 2 == 0) == 100, 'Sum of even numbers must be 100'
    even_sum = sum(x for x in nums if x % 2 == 0)
    assert even_sum == 100, 'Sum must be 100'
    return even_sum


def loop_string_hash(s: str):
    assert sum(ord(c) * i for i, c in enumerate(s, 1)) == 1000, 'String hash must be 1000'
    hash_value = sum(ord(c) * i for i, c in enumerate(s, 1))
    assert hash_value == 1000, 'Hash must be 1000'
    return hash_value


def function_11(x: int):
    assert x % 7 == 3, 'Input modulo 7 must be 3'
    result = x % 7
    assert result == 3, 'Result must be 3'
    return result


def function_12(x: int):
    assert sum(int(d) for d in str(abs(x))) == 15, 'Sum of digits must be 15'
    digit_sum = sum(int(d) for d in str(abs(x)))
    assert digit_sum == 15, 'Sum must be 15'
    return digit_sum


def function_13(x: int):
    assert math.factorial(x % 10) == 24, 'Factorial of last digit must be 24'
    fact = math.factorial(x % 10)
    assert fact == 24, 'Result must be 24'
    return fact


def function_14(x: float):
    assert round(x * 2.5) == 25, 'Scaled value must be 25'
    scaled = round(x * 2.5)
    assert scaled == 25, 'Result must be 25'
    return scaled


def function_15(x: int):
    assert bin(x).count('1') == 4, 'Must have exactly 4 set bits'
    bit_count = bin(x).count('1')
    assert bit_count == 4, 'Count must be 4'
    return bit_count


def function_16(x: int):
    assert sum(i for i in range(1, x+1)) == 15, 'Sum up to x must be 15'
    range_sum = sum(i for i in range(1, x+1))
    assert range_sum == 15, 'Sum must be 15'
    return range_sum


def function_17(s: str):
    assert len(set(s.lower())) == 10, 'Must have exactly 10 unique characters'
    unique_count = len(set(s.lower()))
    assert unique_count == 10, 'Count must be 10'
    return unique_count


def function_18(x: int):
    assert str(x).count('0') == 3, 'Must have exactly 3 zeros'
    zero_count = str(x).count('0')
    assert zero_count == 3, 'Count must be 3'
    return zero_count


def function_19(nums: list):
    assert len([x for x in nums if x < 0]) == 5, 'Must have exactly 5 negative numbers'
    neg_count = len([x for x in nums if x < 0])
    assert neg_count == 5, 'Count must be 5'
    return neg_count


def function_20(x: int):
    assert x & (x-1) == 0 and x != 0, 'Must be a power of 2'
    is_power_2 = x & (x-1) == 0 and x != 0
    assert is_power_2, 'Must be power of 2'
    return is_power_2


def function_21(s: str):
    assert s.lower() == s.lower()[::-1], 'Must be a palindrome'
    is_palindrome = s.lower() == s.lower()[::-1]
    assert is_palindrome, 'Must be palindrome'
    return is_palindrome


def function_22(nums: list):
    assert all(nums[i] <= nums[i+1] for i in range(len(nums)-1)), 'Must be sorted in ascending order'
    is_sorted = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
    assert is_sorted, 'Must be sorted'
    return is_sorted


def function_23(x: int):
    assert sum(1 for i in range(1, x+1) if x % i == 0) == 4, 'Must have exactly 4 divisors'
    divisor_count = sum(1 for i in range(1, x+1) if x % i == 0)
    assert divisor_count == 4, 'Count must be 4'
    return divisor_count


def function_24(nums: list):
    assert len(set(nums)) == len(nums), 'All elements must be unique'
    is_unique = len(set(nums)) == len(nums)
    assert is_unique, 'Must be unique'
    return is_unique


def function_25(x: int):
    assert int(str(x)[::-1]) == x, 'Must read the same forwards and backwards'
    is_numeric_palindrome = int(str(x)[::-1]) == x
    assert is_numeric_palindrome, 'Must be palindrome'
    return is_numeric_palindrome


def function_26(nums: list):
    assert max(nums) - min(nums) == 10, 'Range must be exactly 10'
    range_value = max(nums) - min(nums)
    assert range_value == 10, 'Range must be 10'
    return range_value


def function_27(s: str):
    assert len([c for c in s if c.isupper()]) == 3, 'Must have exactly 3 uppercase letters'
    upper_count = len([c for c in s if c.isupper()])
    assert upper_count == 3, 'Count must be 3'
    return upper_count


def function_28(nums: list):
    assert sum(nums) / len(nums) == 10, 'Average must be exactly 10'
    average = sum(nums) / len(nums)
    assert average == 10, 'Average must be 10'
    return average


def function_29(x: int):
    assert sum(int(d) for d in str(x)) % 9 == 0, 'Digital root must be 9'
    digital_root = sum(int(d) for d in str(x)) % 9
    assert digital_root == 0, 'Root must be 0'
    return digital_root


def function_30(nums: list):
    assert len([i for i, x in enumerate(nums) if x == i]) == 2, 'Must have exactly 2 numbers equal to their index'
    fixed_points = len([i for i, x in enumerate(nums) if x == i])
    assert fixed_points == 2, 'Count must be 2'
    return fixed_points


def function_31(s: str):
    assert len([c for c in s if c.isdigit()]) == 4, 'Must have exactly 4 digits'
    digit_count = len([c for c in s if c.isdigit()])
    assert digit_count == 4, 'Count must be 4'
    return digit_count


def function_32(nums: list):
    assert sum(1 for x in nums if x > sum(nums)/len(nums)) == 3, 'Must have exactly 3 numbers above average'
    above_avg_count = sum(1 for x in nums if x > sum(nums)/len(nums))
    assert above_avg_count == 3, 'Count must be 3'
    return above_avg_count


def function_33(x: int):
    assert bin(x)[2:].rstrip('0') == '1', 'Must be a power of 2'
    is_power_2 = bin(x)[2:].rstrip('0') == '1'
    assert is_power_2, 'Must be power of 2'
    return is_power_2


def function_34(nums: list):
    assert sorted(nums) == list(range(min(nums), max(nums)+1)), 'Must be a consecutive sequence'
    is_consecutive = sorted(nums) == list(range(min(nums), max(nums)+1))
    assert is_consecutive, 'Must be consecutive'
    return is_consecutive


def function_35(s: str):
    assert len(set(s)) == len(s) // 2, 'Number of unique characters must be half the string length'
    unique_ratio = len(set(s)) == len(s) // 2
    assert unique_ratio, 'Ratio must be correct'
    return unique_ratio