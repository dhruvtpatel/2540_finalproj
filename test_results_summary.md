# Test Results Summary

## Overview
This document summarizes the results of testing various functions using multiple testing methods (CrossHair, fuzzing, and assertion tests). The scoring system evaluates failure messages based on:
- Specificity (0.3 points)
- Actionability (0.3 points)
- Context (0.2 points)
- Technical Detail (0.2 points)

Note: Only failing functions are scored (0-1). Passing functions are marked as PASS (score 1.0).

## Function Results

### 1. process_data
- Status: PASS (score 1.0)
- Early Assertion: `assert x == 50, 'Input must be 50 to satisfy final assertion'`
- Final Assertion: `assert z == 100, "Final check: z must equal 100"`
- Analysis: Function passed all tests

### 2. convert_temperature
- Status: PASS (score 1.0)
- Early Assertion: `assert celsius == 37.77777777777778, 'Input must be approximately 37.78°C to convert to 100°F'`
- Final Assertion: `assert rounded_temp == 100, "Final check: converted temperature must be exactly 100"`
- Analysis: Function passed all tests

### 3. calculate_discount
- Status: PASS (score 1.0)
- Early Assertion: `assert price * (1 - discount_rate) == 50, 'Discounted price must equal 50'`
- Final Assertion: `assert rounded_price == 50, "Final check: discounted price must be exactly 50"`
- Analysis: Function passed all tests

### 4. process_complex_number
- Status: PASS (score 1.0)
- Early Assertion: `assert real**2 + imag**2 == 100, 'Complex number magnitude squared must be 100'`
- Final Assertion: `assert rounded_magnitude == 10, "Final check: magnitude must be exactly 10"`
- Analysis: Function passed all tests

### 5. transform_data
- Status: PASS (score 1.0)
- Early Assertion: `assert (input_value * 3 + 1) // 2 == 50, 'Transformed value must be 50'`
- Final Assertion: `assert processed == 50, "Final check: processed value must be exactly 50"`
- Analysis: Function passed all tests

### 6. circle_area_diff
- Status: PASS (score 1.0)
- Early Assertion: `assert round(math.pi * r**2 - 2 * math.pi * r) == 50, 'Difference between area and circumference must be 50'`
- Final Assertion: `assert diff == 50, "Final check: area minus circumference must be 50"`
- Analysis: Function passed all tests

### 7. triangle_checker
- Status: PASS (score 1.0)
- Early Assertion: `assert a + b > c and a + c > b and b + c > a, 'Sides must form a valid triangle'`
- Final Assertion: `assert code == 100, "Final check: must be a triangle"`
- Analysis: Function passed all tests

### 8. temperature_offset
- Status: PASS (score 1.0)
- Early Assertion: `assert round((c * 9/5) + 32) - int(c) == 68, 'Temperature offset must be 68'`
- Final Assertion: `assert adjusted == 68, "Final check: adjusted temp must be 68"`
- Analysis: Function passed all tests

### 9. quadratic_discriminant
- Status: PASS (score 1.0)
- Early Assertion: `assert abs(b**2 - 4*a*c) % 100 == 25, 'Normalized discriminant must be 25'`
- Final Assertion: `assert normalized == 25, "Final check: normalized discriminant must be 25"`
- Analysis: Function passed all tests

### 10. vector_norm
- Status: PASS (score 1.0)
- Early Assertion: `assert round(math.sqrt(x**2 + y**2)) == 10, 'Vector norm must be 10'`
- Final Assertion: `assert rounded == 10, "Final check: norm must be 10"`
- Analysis: Function passed all tests

### 11. hypotenuse_diff
- Status: PASS (score 1.0)
- Early Assertion: `assert abs(round(math.hypot(a, b)) - int(a) - int(b)) == 3, 'Hypotenuse difference must be 3'`
- Final Assertion: `assert diff == 3, "Final check: diff must be 3"`
- Analysis: Function passed all tests

### 12. ascii_average
- Status: PASS (score 1.0)
- Early Assertion: `assert sum(ord(c) for c in s) // len(s) == 83, 'Average ASCII value must be 83'`
- Final Assertion: `assert avg == 83, "Final check: average ASCII must be 83"`
- Analysis: Function passed all tests

### 13. list_balance
- Status: PASS (score 1.0)
- Early Assertion: `assert abs(sum(nums[:len(nums)//2]) - sum(nums[len(nums)//2:])) == 5, 'List halves must balance to 5'`
- Final Assertion: `assert balance == 5, "Final check: list halves balance to 5"`
- Analysis: Function passed all tests

### 14. odd_sum_validator
- Status: PASS (score 1.0)
- Early Assertion: `assert sum(n for n in lst if n % 2 == 1) % 100 == 33, 'Odd sum mod 100 must be 33'`
- Final Assertion: `assert mod == 33, "Final check: odd sum mod 100 must be 33"`
- Analysis: Function passed all tests

### 15. string_pattern_score
- Status: PASS (score 1.0)
- Early Assertion: `assert sum(1 for c in s if c in 'aeiouAEIOU') * 5 == 25, 'Vowel score must be 25'`
- Final Assertion: `assert result == 25, "Final check: vowel score must be 25"`
- Analysis: Function passed all tests

### 16. sum_until_limit
- Status: FAIL
- Score: 0.40/1.00
- Early Assertion: `assert sum(n for n in nums if sum(nums[:nums.index(n) + 1]) < 50) + len(nums) == 60, 'Sum and size must be 60'`
- Final Assertion: `assert adjusted == 60, "Final check: sum and size must be 60"`
- Failure Cases:
  - `nums=[11, 18, 7, 19, 14]`
  - `nums=[1, 20, 11, 18, 8, 8, 12, 1, 9, 2]`
- Analysis: Failure message lacks specific information about why the sum condition failed. Could benefit from:
  - Showing actual sum values
  - Explaining the relationship between sum and size
  - Providing guidance on valid input ranges

### 17. count_divisibles
- Status: PASS (score 1.0)
- Early Assertion: `assert sum(1 for n in nums if n % 4 == 0) * 10 == 40, 'Divisible count score must be 40'`
- Final Assertion: `assert score == 40, "Final check: divisible count score must be 40"`
- Analysis: Function passed all tests

### 18. index_weighted_sum
- Status: PASS (score 1.0)
- Early Assertion: `assert sum(val * i for i, val in enumerate(lst)) % 100 == 35, 'Weighted sum mod 100 must be 35'`
- Final Assertion: `assert result == 35, "Final check: weighted mod result must be 35"`
- Analysis: Function passed all tests

### 19. square_accumulator
- Status: PASS (score 1.0)
- Early Assertion: `assert sum(i * i for i in range(x)) % 100 == 55, 'Square sum mod 100 must be 55'`
- Final Assertion: `assert final == 55, "Final check: square sum mod 100 must be 55"`
- Analysis: Function passed all tests

### 20. nested_loop_checker
- Status: PASS (score 1.0)
- Early Assertion: `assert sum(1 for i in range(limit) for j in range(i)) % 200 == 36, 'Nested loop result must be 36'`
- Final Assertion: `assert final == 36, "Final check: nested loop result must be 36"`
- Analysis: Function passed all tests

### 21. character_counter
- Status: PASS (score 1.0)
- Early Assertion: `assert sum(1 for ch in text if ch in 'aeiouAEIOU') * 3 == 27, 'Vowel count score must be 27'`
- Final Assertion: `assert result == 27, "Final check: vowel count score must be 27"`
- Analysis: Function passed all tests

### 22. rolling_maximum
- Status: PASS (score 1.0)
- Early Assertion: `assert max(values) + 10 == 99, 'Max plus 10 must be 99'`
- Final Assertion: `assert final == 99, "Final check: max plus 10 must be 99"`
- Analysis: Function passed all tests

### 23. fibonacci_counter
- Status: PASS (score 1.0)
- Early Assertion: `assert sum(fibonacci(n)) % 100 == 89, 'Fibonacci sum mod 100 must be 89'`
- Final Assertion: `assert mod_sum == 89, "Final check: Fibonacci sum mod 100 must be 89"`
- Analysis: Function passed all tests

### 24. loop_even_sum
- Status: PASS (score 1.0)
- Early Assertion: `assert sum(i for i in range(start, end + 1) if i % 2 == 0) // 2 == 110, 'Halved even sum must be 110'`
- Final Assertion: `assert final == 110, "Final check: halved even sum must be 110"`
- Analysis: Function passed all tests

### 25. loop_string_hash
- Status: FAIL
- Score: 0.20/1.00
- Early Assertion: `assert sum(ord(c) * 3 for c in text) % 200 == 66, 'Character hash must be 66'`
- Final Assertion: `assert final == 66, "Final check: character hash must be 66"`
- Failure Cases: Multiple string inputs that didn't satisfy the hash condition
- Analysis: Failure message provides minimal information. Could be improved by:
  - Showing the actual hash value
  - Explaining the character weighting (×3)
  - Providing examples of valid input strings
  - Explaining the modulo 200 operation

## Summary Statistics
- Total Functions Tested: 25
- Passed: 23 (score 1.0)
- Failed: 2
- Average Failure Explanation Score: 0.30
- Lowest Failure Explanation Score: 0.20 (loop_string_hash)

## Areas for Improvement in Failure Explanations
1. Specificity:
   - Show actual vs. expected values
   - Provide concrete examples of valid inputs
   - Explain the mathematical relationships

2. Actionability:
   - Include specific steps to fix the issue
   - Provide valid input ranges
   - Explain the constraints in simpler terms

3. Context:
   - Explain the purpose of the conditions
   - Show how the values are calculated
   - Provide background on the mathematical operations

4. Technical Detail:
   - Break down complex calculations
   - Explain the significance of constants
   - Show intermediate values 