import openai
import json
from typing import Dict
import os
import inspect
from functions import *

# Mock response for testing
def mock_generate_early_assertion(function_code: str) -> dict:
    # Extract the final assertion from the code
    final_assert = [line for line in function_code.split('\n') if 'assert' in line][0]
    
    # Simple mock response based on the function name
    if 'process_data' in function_code:
        return {
            "assertion_code": "assert x == 50, 'Input must be 50 to satisfy final assertion'",
            "explanation": "The early assertion checks if x is 50, which is the only value that will make z equal to 100 in the final assertion."
        }
    elif 'convert_temperature' in function_code:
        return {
            "assertion_code": "assert celsius == 37.77777777777778, 'Input must be approximately 37.78°C to convert to 100°F'",
            "explanation": "The early assertion checks if the input temperature is approximately 37.78°C, which converts to exactly 100°F."
        }
    elif 'calculate_discount' in function_code:
        return {
            "assertion_code": "assert price * (1 - discount_rate) == 50, 'Discounted price must equal 50'",
            "explanation": "The early assertion checks if the discounted price will be exactly 50, matching the final assertion."
        }
    elif 'process_complex_number' in function_code:
        return {
            "assertion_code": "assert real**2 + imag**2 == 100, 'Complex number magnitude squared must be 100'",
            "explanation": "The early assertion checks if the magnitude squared of the complex number is 100, which will make the rounded magnitude 10."
        }
    elif 'transform_data' in function_code:
        return {
            "assertion_code": "assert (input_value * 3 + 1) // 2 == 50, 'Transformed value must be 50'",
            "explanation": "The early assertion checks if the transformed value will be exactly 50, matching the final assertion."
        }
    elif 'circle_area_diff' in function_code:
        return {
            "assertion_code": "assert round(math.pi * r**2 - 2 * math.pi * r) == 50, 'Difference between area and circumference must be 50'",
            "explanation": "The early assertion checks if the difference between the circle's area and circumference is 50."
        }
    elif 'triangle_checker' in function_code:
        return {
            "assertion_code": "assert a + b > c and a + c > b and b + c > a, 'Sides must form a valid triangle'",
            "explanation": "The early assertion checks if the sides can form a valid triangle, which is required for the final assertion to be true."
        }
    elif 'temperature_offset' in function_code:
        return {
            "assertion_code": "assert round((c * 9/5) + 32) - int(c) == 68, 'Temperature offset must be 68'",
            "explanation": "The early assertion checks if the temperature offset will be exactly 68, matching the final assertion."
        }
    elif 'quadratic_discriminant' in function_code:
        return {
            "assertion_code": "assert abs(b**2 - 4*a*c) % 100 == 25, 'Normalized discriminant must be 25'",
            "explanation": "The early assertion checks if the normalized discriminant will be 25, matching the final assertion."
        }
    elif 'vector_norm' in function_code:
        return {
            "assertion_code": "assert round(math.sqrt(x**2 + y**2)) == 10, 'Vector norm must be 10'",
            "explanation": "The early assertion checks if the vector norm will be exactly 10, matching the final assertion."
        }
    elif 'hypotenuse_diff' in function_code:
        return {
            "assertion_code": "assert abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3, 'Hypotenuse difference must be 3'",
            "explanation": "The early assertion checks if the difference between the hypotenuse and the sum of the sides will be 3."
        }
    elif 'ascii_average' in function_code:
        return {
            "assertion_code": "assert sum(ord(c) for c in s) // len(s) == 83, 'Average ASCII value must be 83'",
            "explanation": "The early assertion checks if the average ASCII value of the string will be 83."
        }
    elif 'list_balance' in function_code:
        return {
            "assertion_code": "assert abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5, 'List halves must balance to 5'",
            "explanation": "The early assertion checks if the difference between the sums of the two halves of the list is 5."
        }
    elif 'odd_sum_validator' in function_code:
        return {
            "assertion_code": "assert sum(n for n in lst if n % 2 == 1) % 100 == 33, 'Odd sum mod 100 must be 33'",
            "explanation": "The early assertion checks if the sum of odd numbers modulo 100 will be 33."
        }
    elif 'string_pattern_score' in function_code:
        return {
            "assertion_code": "assert sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25, 'Vowel score must be 25'",
            "explanation": "The early assertion checks if the vowel score will be exactly 25."
        }
    elif 'sum_until_limit' in function_code:
        return {
            "assertion_code": "assert sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60, 'Sum and size must be 60'",
            "explanation": "The early assertion checks if the sum of numbers until reaching 50 plus the list length will be 60."
        }
    elif 'count_divisibles' in function_code:
        return {
            "assertion_code": "assert sum(1 for n in nums if n % 4 == 0) * 10 == 40, 'Divisible count score must be 40'",
            "explanation": "The early assertion checks if the count of numbers divisible by 4 times 10 will be 40."
        }
    elif 'index_weighted_sum' in function_code:
        return {
            "assertion_code": "assert sum(val * i for i, val in enumerate(lst)) % 100 == 35, 'Weighted sum mod 100 must be 35'",
            "explanation": "The early assertion checks if the weighted sum modulo 100 will be 35."
        }
    elif 'square_accumulator' in function_code:
        return {
            "assertion_code": "assert sum(i * i for i in range(x)) % 100 == 55, 'Square sum mod 100 must be 55'",
            "explanation": "The early assertion checks if the sum of squares modulo 100 will be 55."
        }
    elif 'nested_loop_checker' in function_code:
        return {
            "assertion_code": "assert sum(1 for i in range(limit) for j in range(i)) % 200 == 36, 'Nested loop result must be 36'",
            "explanation": "The early assertion checks if the count of nested loop iterations modulo 200 will be 36."
        }
    elif 'character_counter' in function_code:
        return {
            "assertion_code": "assert sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27, 'Vowel count score must be 27'",
            "explanation": "The early assertion checks if the vowel count times 3 will be 27."
        }
    elif 'rolling_maximum' in function_code:
        return {
            "assertion_code": "assert max(values) + 10 == 99, 'Max plus 10 must be 99'",
            "explanation": "The early assertion checks if the maximum value plus 10 will be 99."
        }
    elif 'fibonacci_counter' in function_code:
        return {
            "assertion_code": "assert sum(fibonacci(n)) % 100 == 89, 'Fibonacci sum mod 100 must be 89'",
            "explanation": "The early assertion checks if the sum of Fibonacci numbers modulo 100 will be 89."
        }
    elif 'loop_even_sum' in function_code:
        return {
            "assertion_code": "assert sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110, 'Halved even sum must be 110'",
            "explanation": "The early assertion checks if the sum of even numbers divided by 2 will be 110."
        }
    elif 'loop_string_hash' in function_code:
        return {
            "assertion_code": "assert sum(ord(c) * 3 for c in text) % 200 == 66, 'Character hash must be 66'",
            "explanation": "The early assertion checks if the weighted character sum modulo 200 will be 66."
        }
    else:
        return {
            "assertion_code": "assert False, 'No early assertion available for this function'",
            "explanation": "No early assertion was generated for this function"
        }

# Dictionary of our test programs
programs = {
    "process_data": process_data,
    "convert_temperature": convert_temperature,
    "calculate_discount": calculate_discount,
    "process_complex_number": process_complex_number,
    "transform_data": transform_data,
    "circle_area_diff": circle_area_diff,
    "triangle_checker": triangle_checker,
    "temperature_offset": temperature_offset,
    "quadratic_discriminant": quadratic_discriminant,
    "vector_norm": vector_norm,
    "hypotenuse_diff": hypotenuse_diff,
    "ascii_average": ascii_average,
    "list_balance": list_balance,
    "odd_sum_validator": odd_sum_validator,
    "string_pattern_score": string_pattern_score,
    "sum_until_limit": sum_until_limit,
    "count_divisibles": count_divisibles,
    "index_weighted_sum": index_weighted_sum,
    "square_accumulator": square_accumulator,
    "nested_loop_checker": nested_loop_checker,
    "character_counter": character_counter,
    "rolling_maximum": rolling_maximum,
    "fibonacci_counter": fibonacci_counter,
    "loop_even_sum": loop_even_sum,
    "loop_string_hash": loop_string_hash
}

print("Generating Early Assertions:")
print("=" * 50)

# Store all generated functions
generated_functions = []

for name, func in programs.items():
    print(f"\nGenerating assertion for {name}:")
    print("=" * 50)

    try:
        # Get the source code
        source = inspect.getsource(func)

        # Generate the assertion
        result = mock_generate_early_assertion(source)

        if "error" in result:
            print(f"Error generating assertion for {name}: {result['error']}")
            continue

        print(f"Generated Assertion: {result['assertion_code']}")
        print(f"Explanation: {result['explanation']}")
        print("-" * 50)

        # Create the complete function with early assertion
        lines = source.split('\n')
        for i, line in enumerate(lines):
            if '#Early Assert HERE' in line:
                lines[i] = f"    {result['assertion_code']}"
        
        generated_functions.append('\n'.join(lines))
        print("Complete function with early assertion:")
        print('\n'.join(lines))
        print("-" * 50)

    except Exception as e:
        print(f"Error processing {name}: {str(e)}")
        print("-" * 50)

# Write all generated functions to a new file
with open('functions_with_assertions.py', 'w') as f:
    f.write("""\"\"\"
This file contains all the functions from functions.py with their early assertions inserted.
Each function has an early assertion that is logically equivalent to its final assertion.
\"\"\"

import math

""")
    f.write('\n\n'.join(generated_functions))