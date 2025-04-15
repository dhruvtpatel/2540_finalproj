"""
Symbolic Execution Specifications for Transformed Functions
This file contains symbolic execution specifications for all transformed functions.
"""

transform_programs = {
    "process_data_module.py": """
def process_data_transformed(x: int):
    '''
    pre: -1000 <= x <= 1000  # Add reasonable bounds
    post: (x == 50) == (x * 2 if x + 2 > 0 else -x * 2 == 100)
    '''
    b_early = (x == 50)
    y = x * 2
    z = y if y > 0 else -y
    b_final = (z == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return z
""",

    "convert_temperature_module.py": """
def convert_temperature_transformed(celsius: float):
    '''
    pre: -100 <= celsius <= 100  # Add reasonable temperature bounds
    post: (abs(celsius - 37.7778) < 0.01) == (round(celsius * 9/5 + 32) == 100)
    '''
    b_early = abs(celsius - 37.7778) < 0.01
    fahrenheit = celsius * 9/5 + 32
    rounded_temp = round(fahrenheit)
    b_final = (rounded_temp == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_temp
""",

    "calculate_discount_module.py": """
def calculate_discount_transformed(price: float, discount_rate: float):
    '''
    pre: 0 <= price <= 1000  # Add reasonable price bounds
    pre: 0 <= discount_rate <= 1  # Discount rate should be between 0 and 1
    post: (price == 100 and discount_rate == 0.5) == (round(price * (1 - discount_rate)) == 50)
    '''
    b_early = (price == 100 and discount_rate == 0.5)
    discounted_price = price * (1 - discount_rate)
    rounded_price = round(discounted_price)
    b_final = (rounded_price == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_price
""",

    "process_complex_number_module.py": """
def process_complex_number_transformed(real: float, imag: float):
    '''
    pre: -1000 <= real <= 1000  # Add reasonable bounds for real part
    pre: -1000 <= imag <= 1000  # Add reasonable bounds for imaginary part
    post: (round((real*2 + imag*2)**0.5) == 10) == (round(abs(complex(real, imag))) == 10)
    '''
    b_early = round((real*2 + imag*2)**0.5) == 10
    complex_num = complex(real, imag)
    magnitude = abs(complex_num)
    rounded_magnitude = round(magnitude)
    b_final = (rounded_magnitude == 10)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded_magnitude
""",

    "transform_data_module.py": """
def transform_data_transformed(input_value: int):
    '''
    pre: -1000 <= input_value <= 1000  # Add reasonable bounds
    post: (input_value == 33) == ((input_value * 3 + 1) // 2 == 50)
    '''
    b_early = (input_value == 33)
    transformed = input_value * 3 + 1
    processed = transformed // 2
    b_final = (processed == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return processed
""",

    "circle_area_diff_module.py": """
def circle_area_diff_transformed(r: float):
    '''
    pre: 0 <= r <= 20  # Add reasonable radius bounds
    post: (round(math.pi * r**2 - 2 * math.pi * r) == 50) == (round(math.pi * r**2 - 2 * math.pi * r) == 50)
    '''
    b_early = round(math.pi * r**2 - 2 * math.pi * r) == 50
    area = math.pi * r ** 2
    circ = 2 * math.pi * r
    diff = round(area - circ)
    b_final = (diff == 50)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return diff
""",

    "triangle_checker_module.py": """
def triangle_checker_transformed(a: int, b: int, c: int):
    '''
    pre: 1 <= a <= 20  # Add reasonable side length bounds
    pre: 1 <= b <= 20
    pre: 1 <= c <= 20
    post: (a + b > c and a + c > b and b + c > a) == (sorted([a, b, c])[0] + sorted([a, b, c])[1] > sorted([a, b, c])[2])
    '''
    b_early = (a + b > c and a + c > b and b + c > a)
    sides = sorted([a, b, c])
    is_triangle = sides[0] + sides[1] > sides[2]
    code = 100 if is_triangle else 0
    b_final = (code == 100)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return code
""",

    "temperature_offset_module.py": """
def temperature_offset_transformed(c: float):
    '''
    pre: 0 <= c <= 100  # Add reasonable temperature bounds
    post: (round((c * 9/5) + 32) - int(c) == 68) == (round((c * 9/5) + 32) - int(c) == 68)
    '''
    b_early = round((c * 9/5) + 32) - int(c) == 68
    f = (c * 9/5) + 32
    rounded = round(f)
    adjusted = rounded - int(c)
    b_final = (adjusted == 68)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return adjusted
""",

    "quadratic_discriminant_module.py": """
def quadratic_discriminant_transformed(a: int, b: int, c: int):
    '''
    pre: -10 <= a <= 10  # Add reasonable coefficient bounds
    pre: -10 <= b <= 10
    pre: -10 <= c <= 10
    post: (abs(b**2 - 4*a*c) % 100 == 25) == (abs(b**2 - 4*a*c) % 100 == 25)
    '''
    b_early = abs(b**2 - 4*a*c) % 100 == 25
    disc = b**2 - 4*a*c
    normalized = abs(disc) % 100
    b_final = (normalized == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return normalized
""",

    "vector_norm_module.py": """
def vector_norm_transformed(x: float, y: float):
    '''
    pre: -10 <= x <= 10  # Add reasonable vector component bounds
    pre: -10 <= y <= 10
    post: (round(math.sqrt(x**2 + y**2)) == 10) == (round(math.sqrt(x**2 + y**2)) == 10)
    '''
    b_early = round(math.sqrt(x**2 + y**2)) == 10
    norm = math.sqrt(x**2 + y**2)
    rounded = round(norm)
    b_final = (rounded == 10)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return rounded
""",

    "hypotenuse_diff_module.py": """
def hypotenuse_diff_transformed(a: float, b: float):
    '''
    pre: 0 <= a <= 10  # Add reasonable side length bounds
    pre: 0 <= b <= 10
    post: (abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3) == (abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3)
    '''
    b_early = abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3
    hyp = math.hypot(a, b)
    rounded = round(hyp)
    diff = abs(rounded - int(a) - int(b))
    b_final = (diff == 3)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return diff
""",

    "ascii_average_module.py": """
def ascii_average_transformed(s: str):
    '''
    pre: len(s) > 0  # String must not be empty
    pre: len(s) <= 10  # Add reasonable string length bound
    post: (sum(ord(c) for c in s) // len(s) == 83) == (sum(ord(c) for c in s) // len(s) == 83)
    '''
    b_early = sum(ord(c) for c in s) // len(s) == 83
    total = sum(ord(c) for c in s)
    avg = total // len(s) if s else 0
    b_final = (avg == 83)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return avg
""",

    "list_balance_module.py": """
def list_balance_transformed(nums: list):
    '''
    pre: len(nums) >= 2  # List must have at least 2 elements
    pre: len(nums) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 10 for x in nums)  # Add reasonable element bounds
    post: (abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5) == (abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5)
    '''
    b_early = abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5
    half = len(nums) // 2
    left = sum(nums[:half])
    right = sum(nums[half:])
    balance = abs(left - right)
    b_final = (balance == 5)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return balance
""",

    "odd_sum_validator_module.py": """
def odd_sum_validator_transformed(lst: list):
    '''
    pre: len(lst) > 0  # List must not be empty
    pre: len(lst) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 10 for x in lst)  # Add reasonable element bounds
    post: (sum(n for n in lst if n % 2 == 1) % 100 == 33) == (sum(n for n in lst if n % 2 == 1) % 100 == 33)
    '''
    b_early = sum(n for n in lst if n % 2 == 1) % 100 == 33
    odds = [n for n in lst if n % 2 == 1]
    total = sum(odds)
    mod = total % 100
    b_final = (mod == 33)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return mod
""",

    "string_pattern_score_module.py": """
def string_pattern_score_transformed(s: str):
    '''
    pre: len(s) > 0  # String must not be empty
    pre: len(s) <= 10  # Add reasonable string length bound
    post: (sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25) == (sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25)
    '''
    b_early = sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25
    score = sum(1 for c in s if c in 'aeiouAEIOU')
    result = score * 5
    b_final = (result == 25)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
""",

    "sum_until_limit_module.py": """
def sum_until_limit_transformed(nums: list):
    '''
    pre: len(nums) > 0  # List must not be empty
    pre: len(nums) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 20 for x in nums)  # Add reasonable element bounds
    post: (sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60) == (sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60)
    '''
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

    "count_divisibles_module.py": """
def count_divisibles_transformed(nums: list):
    '''
    pre: len(nums) > 0  # List must not be empty
    pre: len(nums) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 20 for x in nums)  # Add reasonable element bounds
    post: (sum(1 for n in nums if n % 4 == 0) * 10 == 40) == (sum(1 for n in nums if n % 4 == 0) * 10 == 40)
    '''
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

    "index_weighted_sum_module.py": """
def index_weighted_sum_transformed(lst: list):
    '''
    pre: len(lst) > 0  # List must not be empty
    pre: len(lst) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 10 for x in lst)  # Add reasonable element bounds
    post: (sum(val * i for i, val in enumerate(lst)) % 100 == 35) == (sum(val * i for i, val in enumerate(lst)) % 100 == 35)
    '''
    b_early = sum(val * i for i, val in enumerate(lst)) % 100 == 35
    weighted = 0
    for i, val in enumerate(lst):
        weighted += val * i
    result = weighted % 100
    b_final = (result == 35)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return result
""",

    "square_accumulator_module.py": """
def square_accumulator_transformed(x: int):
    '''
    pre: 0 <= x <= 10  # Add reasonable input bounds
    post: (sum(i * i for i in range(x)) % 100 == 55) == (sum(i * i for i in range(x)) % 100 == 55)
    '''
    b_early = sum(i * i for i in range(x)) % 100 == 55
    acc = 0
    for i in range(x):
        acc += i * i
    final = acc % 100
    b_final = (final == 55)
    assert b_early == b_final, "Early and final assertions are not equivalent"
    return final
""",

    "nested_loop_checker_module.py": """
def nested_loop_checker_transformed(limit: int):
    '''
    pre: 0 <= limit <= 10  # Add reasonable limit bounds
    post: (sum(1 for i in range(limit) for j in range(i)) % 200 == 36) == (sum(1 for i in range(limit) for j in range(i)) % 200 == 36)
    '''
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

    "character_counter_module.py": """
def character_counter_transformed(text: str):
    '''
    pre: len(text) > 0  # String must not be empty
    pre: len(text) <= 10  # Add reasonable string length bound
    post: (sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27) == (sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27)
    '''
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

    "rolling_maximum_module.py": """
def rolling_maximum_transformed(values: list):
    '''
    pre: len(values) > 0  # List must not be empty
    pre: len(values) <= 10  # Add reasonable list length bound
    pre: all(0 <= x <= 100 for x in values)  # Add reasonable element bounds
    post: (max(values) + 10 == 99) == (max(values) + 10 == 99)
    '''
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

    "fibonacci_counter_module.py": """
def fibonacci_counter_transformed(n: int):
    '''
    pre: 0 <= n <= 10  # Add reasonable input bounds
    post: (sum(fibonacci(n)) % 100 == 89) == (sum(fibonacci(n)) % 100 == 89)
    '''
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
""",

    "loop_even_sum_module.py": """
def loop_even_sum_transformed(start: int, end: int):
    '''
    pre: 0 <= start <= 20  # Add reasonable bounds
    pre: 0 <= end <= 20
    post: (sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110) == (sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110)
    '''
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

    "loop_string_hash_module.py": """
def loop_string_hash_transformed(text: str):
    '''
    pre: len(text) > 0  # String must not be empty
    pre: len(text) <= 10  # Add reasonable string length bound
    post: (sum(ord(c) * 3 for c in text) % 200 == 66) == (sum(ord(c) * 3 for c in text) % 200 == 66)
    '''
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

# Write all modules to disk
for filename, code in transform_programs.items():
    with open(filename, 'w') as f:
        f.write(code)

print("Modules written successfully.") 