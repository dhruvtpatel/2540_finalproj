from hypothesis import given, strategies as st
from hypothesis import settings
from code.functions.transformed_functions import *

print("\nFuzz Testing Results for All Transformed Functions:")

@settings(max_examples=20)
@given(st.integers(min_value=0, max_value=100))
def test_process_data(x):
    try:
        process_data_transformed(x)
        print(f"PASS: process_data_transformed(x={x})")
    except AssertionError:
        print(f"FAIL: process_data_transformed(x={x})")

@settings(max_examples=20)
@given(st.floats(min_value=0, max_value=100))
def test_convert_temperature(c):
    try:
        convert_temperature_transformed(c)
        print(f"PASS: convert_temperature_transformed(c={c})")
    except AssertionError:
        print(f"FAIL: convert_temperature_transformed(c={c})")

@settings(max_examples=20)
@given(st.floats(min_value=0, max_value=200), st.floats(min_value=0, max_value=1))
def test_calculate_discount(p, d):
    try:
        calculate_discount_transformed(p, d)
        print(f"PASS: calculate_discount_transformed(price={p}, discount_rate={d})")
    except AssertionError:
        print(f"FAIL: calculate_discount_transformed(price={p}, discount_rate={d})")

@settings(max_examples=20)
@given(st.floats(min_value=-20, max_value=20), st.floats(min_value=-20, max_value=20))
def test_process_complex_number(r, i):
    try:
        process_complex_number_transformed(r, i)
        print(f"PASS: process_complex_number_transformed(real={r}, imag={i})")
    except AssertionError:
        print(f"FAIL: process_complex_number_transformed(real={r}, imag={i})")

@settings(max_examples=20)
@given(st.integers(min_value=0, max_value=100))
def test_transform_data(v):
    try:
        transform_data_transformed(v)
        print(f"PASS: transform_data_transformed(input_value={v})")
    except AssertionError:
        print(f"FAIL: transform_data_transformed(input_value={v})")

@settings(max_examples=20)
@given(st.floats(min_value=0, max_value=10))
def test_circle_area_diff(r):
    try:
        circle_area_diff_transformed(r)
        print(f"PASS: circle_area_diff_transformed(r={r})")
    except AssertionError:
        print(f"FAIL: circle_area_diff_transformed(r={r})")

@settings(max_examples=20)
@given(st.integers(min_value=1, max_value=100), 
       st.integers(min_value=1, max_value=100), 
       st.integers(min_value=1, max_value=100))
def test_triangle_checker(a, b, c):
    try:
        triangle_checker_transformed(a, b, c)
        print(f"PASS: triangle_checker_transformed(a={a}, b={b}, c={c})")
    except AssertionError:
        print(f"FAIL: triangle_checker_transformed(a={a}, b={b}, c={c})")

@settings(max_examples=20)
@given(st.floats(min_value=0, max_value=100))
def test_temperature_offset(c):
    try:
        temperature_offset_transformed(c)
        print(f"PASS: temperature_offset_transformed(c={c})")
    except AssertionError:
        print(f"FAIL: temperature_offset_transformed(c={c})")

@settings(max_examples=20)
@given(st.floats(min_value=-10, max_value=10), st.floats(min_value=-10, max_value=10))
def test_vector_norm(x, y):
    try:
        vector_norm_transformed(x, y)
        print(f"PASS: vector_norm_transformed(x={x}, y={y})")
    except AssertionError:
        print(f"FAIL: vector_norm_transformed(x={x}, y={y})")

@settings(max_examples=20)
@given(st.floats(min_value=1, max_value=10), st.floats(min_value=1, max_value=10))
def test_hypotenuse_diff(a, b):
    try:
        hypotenuse_diff_transformed(a, b)
        print(f"PASS: hypotenuse_diff_transformed(a={a}, b={b})")
    except AssertionError:
        print(f"FAIL: hypotenuse_diff_transformed(a={a}, b={b})")

@settings(max_examples=20)
@given(st.text(min_size=1, max_size=10))
def test_ascii_average(s):
    try:
        ascii_average_transformed(s)
        print(f"PASS: ascii_average_transformed(s={s})")
    except AssertionError:
        print(f"FAIL: ascii_average_transformed(s={s})")

@settings(max_examples=20)
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=2, max_size=10))
def test_list_balance(nums):
    try:
        list_balance_transformed(nums)
        print(f"PASS: list_balance_transformed(nums={nums})")
    except AssertionError:
        print(f"FAIL: list_balance_transformed(nums={nums})")

@settings(max_examples=20)
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=10))
def test_odd_sum_validator(lst):
    try:
        odd_sum_validator_transformed(lst)
        print(f"PASS: odd_sum_validator_transformed(lst={lst})")
    except AssertionError:
        print(f"FAIL: odd_sum_validator_transformed(lst={lst})")

@settings(max_examples=20)
@given(st.text(min_size=1, max_size=10))
def test_string_pattern_score(s):
    try:
        string_pattern_score_transformed(s)
        print(f"PASS: string_pattern_score_transformed(s={s})")
    except AssertionError:
        print(f"FAIL: string_pattern_score_transformed(s={s})")

@settings(max_examples=20)
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=10))
def test_sum_until_limit(nums):
    try:
        sum_until_limit_transformed(nums)
        print(f"PASS: sum_until_limit_transformed(nums={nums})")
    except AssertionError:
        print(f"FAIL: sum_until_limit_transformed(nums={nums})")

@settings(max_examples=20)
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=10))
def test_count_divisibles(nums):
    try:
        count_divisibles_transformed(nums)
        print(f"PASS: count_divisibles_transformed(nums={nums})")
    except AssertionError:
        print(f"FAIL: count_divisibles_transformed(nums={nums})")

@settings(max_examples=20)
@given(st.integers(min_value=0, max_value=100))
def test_square_accumulator(x):
    try:
        square_accumulator_transformed(x)
        print(f"PASS: square_accumulator_transformed(x={x})")
    except AssertionError:
        print(f"FAIL: square_accumulator_transformed(x={x})")

@settings(max_examples=20)
@given(st.text(min_size=1, max_size=10))
def test_character_counter(text):
    try:
        character_counter_transformed(text)
        print(f"PASS: character_counter_transformed(text={text})")
    except AssertionError:
        print(f"FAIL: character_counter_transformed(text={text})")

@settings(max_examples=20)
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=10))
def test_rolling_maximum(values):
    try:
        rolling_maximum_transformed(values)
        print(f"PASS: rolling_maximum_transformed(values={values})")
    except AssertionError:
        print(f"FAIL: rolling_maximum_transformed(values={values})")

@settings(max_examples=20)
@given(st.integers(min_value=1, max_value=20))
def test_fibonacci_counter(n):
    try:
        fibonacci_counter_transformed(n)
        print(f"PASS: fibonacci_counter_transformed(n={n})")
    except AssertionError:
        print(f"FAIL: fibonacci_counter_transformed(n={n})")

@settings(max_examples=20)
@given(st.integers(min_value=0, max_value=100), st.integers(min_value=0, max_value=100))
def test_loop_even_sum(start, end):
    try:
        loop_even_sum_transformed(start, end)
        print(f"PASS: loop_even_sum_transformed(start={start}, end={end})")
    except AssertionError:
        print(f"FAIL: loop_even_sum_transformed(start={start}, end={end})")

@settings(max_examples=20)
@given(st.text(min_size=1, max_size=10))
def test_loop_string_hash(text):
    try:
        loop_string_hash_transformed(text)
        print(f"PASS: loop_string_hash_transformed(text={text})")
    except AssertionError:
        print(f"FAIL: loop_string_hash_transformed(text={text})")

# Run all tests
if __name__ == "__main__":
    print("Starting comprehensive fuzz testing...")
    test_process_data()
    test_convert_temperature()
    test_calculate_discount()
    test_process_complex_number()
    test_transform_data()
    test_circle_area_diff()
    test_triangle_checker()
    test_temperature_offset()
    test_vector_norm()
    test_hypotenuse_diff()
    test_ascii_average()
    test_list_balance()
    test_odd_sum_validator()
    test_string_pattern_score()
    test_sum_until_limit()
    test_count_divisibles()
    test_square_accumulator()
    test_character_counter()
    test_rolling_maximum()
    test_fibonacci_counter()
    test_loop_even_sum()
    test_loop_string_hash()
    print("\nFuzz testing completed!") 