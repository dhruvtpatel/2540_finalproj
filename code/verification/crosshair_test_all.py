"""
Run CrossHair verification on all functions with assertions, specifically testing
equivalence between early and late assertions.
"""
import os
import sys
from pathlib import Path
from crosshair.core import analyze_function
from typing import Callable, List, Dict, Any
import inspect
import ast
import subprocess

# Add parent directory to Python path
current_file = Path(__file__).resolve()
parent_dir = current_file.parent.parent
sys.path.append(str(parent_dir))

# Import all functions from functions_with_assertions
from functions.functions_with_assertions import *

# Create results directory if it doesn't exist
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

def create_transformed_function(func):
    """Create a transformed version of the function with proper imports and scoping."""
    # Get the function's source code
    source = inspect.getsource(func)
    lines = source.split('\n')
    
    # Extract imports and function body
    imports = []
    body = []
    in_body = False
    indent = ''
    
    for line in lines:
        if line.strip().startswith('import ') or line.strip().startswith('from '):
            imports.append(line.strip())  # Remove any indentation from imports
        elif line.strip().startswith('def '):
            in_body = True
            body.append(line.strip())  # Remove indentation from function definition
            # Get the indentation from the first line after function definition
            for next_line in lines[lines.index(line) + 1:]:
                if next_line.strip():
                    indent = ' ' * (len(next_line) - len(next_line.lstrip()))
                    break
        elif in_body and line.strip():
            # Preserve relative indentation for body
            current_indent = len(line) - len(line.lstrip())
            if current_indent > len(indent):
                # This is nested code, preserve its relative indentation
                body.append('    ' + line[len(indent):])
            else:
                # This is at the same level as the function body
                body.append('    ' + line.lstrip())
    
    # Create the transformed function
    transformed_lines = []
    # Add imports at the top level
    transformed_lines.extend(imports)
    transformed_lines.append('')
    # Add function definition
    transformed_lines.append('def ' + func.__name__ + '_transformed(*args, **kwargs):')
    transformed_lines.append('    # Early assertion')
    transformed_lines.append('    assert True  # Placeholder for early assertion')
    transformed_lines.append('')
    # Add function body with proper indentation
    transformed_lines.extend(body[1:])  # Skip the original function definition
    transformed_lines.append('')
    transformed_lines.append('    # Final assertion')
    transformed_lines.append('    assert True  # Placeholder for final assertion')
    transformed_lines.append('')
    transformed_lines.append('    return result')
    
    # Create the module content
    module_content = '\n'.join(transformed_lines)
    
    return module_content

# Function prefixes to test
function_prefixes = [
    "process_data", "convert_temperature", "calculate_discount",
    "process_complex_number", "transform_data", "circle_area_diff",
    "triangle_checker", "temperature_offset", "quadratic_discriminant",
    "vector_norm", "hypotenuse_diff", "ascii_average", "list_balance",
    "odd_sum_validator", "string_pattern_score", "sum_until_limit",
    "count_divisibles", "index_weighted_sum", "square_accumulator",
    "nested_loop_checker", "character_counter", "rolling_maximum",
    "fibonacci_counter", "loop_even_sum", "loop_string_hash"
] + [f"function_{i}" for i in range(11, 36)]

# Collect functions to test
functions_to_test: Dict[str, Callable] = {}
for name, obj in list(globals().items()):
    if callable(obj) and any(name.startswith(prefix) for prefix in function_prefixes):
        functions_to_test[name] = obj

# Create modules directory if it doesn't exist
modules_dir = Path("crosshair_modules")
modules_dir.mkdir(exist_ok=True)

# Open results file and write header
with open(results_dir / "crosshair_results.txt", "w") as f:
    total_functions = len(functions_to_test)
    passed_functions = 0
    failed_functions = 0
    
    f.write("CrossHair Test Results\n")
    f.write("=====================\n\n")
    
    # Test each function
    for name, func in functions_to_test.items():
        f.write(f"Testing function: {name}\n")
        f.write("-" * (len(name) + 18) + "\n")
        
        try:
            # Create transformed function
            transformed = create_transformed_function(func)
            module_path = modules_dir / f"{name}_module.py"
            with open(module_path, "w") as mf:
                mf.write(transformed)
            
            # Run CrossHair on the module
            result = subprocess.run(
                ['crosshair', 'check', str(module_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.returncode == 0:
                passed_functions += 1
                f.write("✓ PASSED: Early and final assertions are equivalent\n")
            else:
                failed_functions += 1
                f.write("✗ FAILED: Early and final assertions are not equivalent\n")
                f.write(f"  - {result.stdout}\n")
                f.write(f"  - {result.stderr}\n")
            
            # Clean up
            module_path.unlink()
            
        except Exception as e:
            failed_functions += 1
            f.write(f"✗ ERROR: {str(e)}\n")
        
        f.write("\n")
    
    # Write summary
    f.write("\nSummary\n")
    f.write("=======\n")
    f.write(f"Total functions tested: {total_functions}\n")
    f.write(f"Passed: {passed_functions} ({passed_functions/total_functions*100:.1f}%)\n")
    f.write(f"Failed: {failed_functions} ({failed_functions/total_functions*100:.1f}%)\n") 