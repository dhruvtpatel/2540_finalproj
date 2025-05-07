from hypothesis import given, settings, strategies as st, HealthCheck, Verbosity
import inspect
import importlib
import json
import datetime
import os
from typing import List, Dict, Any
import sys
import traceback

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

from code_files.c_transformed_programs.transformed_functions import *

def get_strategy_for_type(param_type):
    """Return appropriate hypothesis strategy based on parameter type."""
    if param_type == int:
        # For date-related functions, avoid values that might cause date errors
        # Safe ranges for year: 1-9999, month: 1-12, day: 1-28 (to be safe)
        return st.integers(min_value=1, max_value=100)
    elif param_type == float:
        return st.floats(min_value=0, max_value=100, allow_nan=False, allow_infinity=False)
    elif param_type == str:
        return st.text(min_size=1, max_size=10)
    elif param_type == list:
        return st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=10)
    else:
        # Default strategy for unknown types
        return st.integers(min_value=1, max_value=100)

def get_strategy_for_function(func):
    """Generate appropriate strategy and argnames for a function."""
    sig = inspect.signature(func)
    strategies = []
    argnames = []
    
    for param_name, param in sig.parameters.items():
        argnames.append(param_name)
        param_type = param.annotation if param.annotation != inspect.Parameter.empty else int
        strategies.append(get_strategy_for_type(param_type))
    
    if len(strategies) == 1:
        return strategies[0], argnames
    return st.tuples(*strategies), argnames

def run_test(func, args, argnames):
    argstr = ", ".join(f"{name}={val!r}" for name, val in zip(argnames, args))
    try:
        func(*args)
        print(f"PASS: {func.__name__}({argstr})")
        return {"status": "passed", "args": argstr}
    except AssertionError as e:
        print(f"FAIL: {func.__name__}({argstr}) - {str(e)}")
        return {"status": "failed", "reason": "assertion_error", "args": argstr, "error": str(e)}
    except Exception as e:
        print(f"ERROR: {func.__name__}({argstr}) - {type(e).__name__}: {str(e)}")
        return {"status": "failed", "reason": "exception", "args": argstr, "error_type": type(e).__name__, "error": str(e)}

def make_hypothesis_test(func, strategy, argnames, results_list):
    function_results = {
        "function_name": func.__name__,
        "test_cases": [],
        "failing_examples": [],
        "execution_error": None
    }
    
    # Create a more robust settings profile
    robust_settings = settings(
        max_examples=20,
        # Disable some health checks that might stop execution
        suppress_health_check=[HealthCheck.too_slow, HealthCheck.filter_too_much],
        # Set deadline to None to avoid timing out
        deadline=None,
        # Verbose mode gives more details
        verbosity=Verbosity.normal
    )
    
    @given(strategy)
    @robust_settings
    def test(args):
        if not isinstance(args, tuple):
            args = (args,)
        try:
            result = run_test(func, args, argnames)
            function_results["test_cases"].append(result)
            if result["status"] == "failed":
                # Also store the failing example separately for easier access
                function_results["failing_examples"].append({
                    "args": result["args"],
                    "reason": result.get("reason", "unknown"),
                    "error": result.get("error", "")
                })
        except Exception as e:
            error_details = {
                "status": "failed",
                "reason": "test_execution_error",
                "args": str(args),
                "error_type": type(e).__name__, 
                "error": str(e),
                "traceback": traceback.format_exc()
            }
            function_results["test_cases"].append(error_details)
            function_results["failing_examples"].append({
                "args": str(args),
                "reason": "test_execution_error",
                "error": f"{type(e).__name__}: {str(e)}"
            })
            print(f"ERROR in test execution: {func.__name__}({str(args)}) - {type(e).__name__}: {str(e)}")
    
    try:
        test()
    except Exception as e:
        error_msg = f"Error running hypothesis test for {func.__name__}: {type(e).__name__}: {str(e)}"
        error_traceback = traceback.format_exc()
        print(error_msg)
        print(error_traceback)
        function_results["execution_error"] = {
            "error": error_msg,
            "traceback": error_traceback
        }
    
    results_list.append(function_results)

if __name__ == "__main__":
    print("Starting comprehensive fuzz testing...")
    
    # Create results list
    results: List[Dict[str, Any]] = []
    passed_count = 0
    failed_count = 0
    errored_functions = 0
    
    # Get all functions from the module
    module = importlib.import_module("code_files.c_transformed_programs.transformed_functions")
    transformed_functions = [
        (name, func) for name, func in inspect.getmembers(module, inspect.isfunction)
        if name.endswith("_transformed")
    ]
    
    print(f"Found {len(transformed_functions)} functions to test")
    
    for name, func in transformed_functions:
        print(f"\nTesting {name}...")
        try:
            strategy, argnames = get_strategy_for_function(func)
            make_hypothesis_test(func, strategy, argnames, results)
        except Exception as e:
            error_msg = f"Error setting up test for {name}: {type(e).__name__}: {str(e)}"
            error_traceback = traceback.format_exc()
            print(error_msg)
            print(error_traceback)
            
            function_results = {
                "function_name": name,
                "test_cases": [],
                "failing_examples": [],
                "execution_error": {
                    "error": error_msg,
                    "traceback": error_traceback
                }
            }
            results.append(function_results)
            errored_functions += 1
    
    # Calculate pass/fail statistics and create simplified results
    functions_with_failures = 0
    simplified_results = []
    
    for function_result in results:
        has_failures = False
        has_execution_error = function_result.get("execution_error") is not None
        
        if has_execution_error:
            has_failures = True
            
        for test_case in function_result["test_cases"]:
            if test_case["status"] == "passed":
                passed_count += 1
            else:
                failed_count += 1
                has_failures = True
        
        # Create entry in simplified_results
        program_name = function_result["function_name"]
        failing_examples = []
        
        # Extract failing examples if any
        if has_failures:
            functions_with_failures += 1
            for ex in function_result.get("failing_examples", []):
                failing_examples.append({
                    "args": ex["args"],
                    "error": ex.get("error", "")
                })
            
            # Add execution error if any
            if has_execution_error:
                failing_examples.append({
                    "args": "test_setup",
                    "error": function_result["execution_error"]["error"]
                })
        
        simplified_results.append({
            "program": program_name,
            "pass": not has_failures,
            "failing_examples": failing_examples
        })
    
    total_count = passed_count + failed_count
    
    # Write simplified results to JSON file
    results_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fuzz_results.json")
    with open(results_file, 'w') as f:
        json.dump(simplified_results, f, indent=2)
    
    # Print summary
    print("\n===== Summary Statistics =====")
    print(f"Total test cases: {total_count}")
    
    if total_count > 0:
        pass_percentage = round(passed_count/total_count*100, 2)
        print(f"Passed: {passed_count} ({pass_percentage}%)")
        print(f"Failed: {failed_count} ({round(failed_count/total_count*100, 2)}%)")
    else:
        print("No test cases were executed successfully.")
        print("Check the execution errors for details.")
    
    print(f"Functions with failures: {functions_with_failures} out of {len(transformed_functions)}")
    print(f"Functions with execution errors: {errored_functions}")
    
    if functions_with_failures > 0:
        print("\n===== Failing Examples Summary =====")
        for result in simplified_results:
            if not result["pass"]:
                print(f"\nFunction: {result['program']}")
                for i, example in enumerate(result['failing_examples'][:3], 1):  # Show max 3 failures
                    print(f"  Example {i}: {example['args']}")
                    print(f"  Error: {example['error']}")
                
                if len(result['failing_examples']) > 3:
                    print(f"  ... and {len(result['failing_examples']) - 3} more failing examples")
    
    print(f"\nResults written to: {results_file}")
    print("\nFuzz testing completed!") 