"""
System to evaluate the quality of failure explanations across different testing methods.
This script runs multiple testing approaches and scores the quality of their failure messages.
"""

import subprocess
import json
import re
from typing import Dict, List, Tuple
import os
import time
from dataclasses import dataclass
from enum import Enum
from tabulate import tabulate

class TestMethod(Enum):
    CROSSHAIR = "crosshair"
    FUZZING = "fuzzing"
    ASSERTION = "assertion"

@dataclass
class FailureMessage:
    method: TestMethod
    function_name: str
    message: str
    score: float = 0.0

def run_crosshair(function_name: str) -> List[FailureMessage]:
    """Run CrossHair on a specific function and collect failure messages."""
    messages = []
    try:
        result = subprocess.run(
            ['crosshair', 'check', f'functions_with_assertions.py:{function_name}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        
        if result.stdout.strip():
            messages.append(FailureMessage(
                method=TestMethod.CROSSHAIR,
                function_name=function_name,
                message=result.stdout.strip()
            ))
    except Exception as e:
        messages.append(FailureMessage(
            method=TestMethod.CROSSHAIR,
            function_name=function_name,
            message=str(e)
        ))
    
    return messages

def run_fuzzing(function_name: str) -> List[FailureMessage]:
    """Run fuzzing on a specific function and collect failure messages."""
    messages = []
    try:
        result = subprocess.run(
            ['python', 'fuzz_test_transformed.py', function_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        
        if result.stdout.strip():
            messages.append(FailureMessage(
                method=TestMethod.FUZZING,
                function_name=function_name,
                message=result.stdout.strip()
            ))
    except Exception as e:
        messages.append(FailureMessage(
            method=TestMethod.FUZZING,
            function_name=function_name,
            message=str(e)
        ))
    
    return messages

def run_assertion_test(function_name: str) -> List[FailureMessage]:
    """Run assertion tests on a specific function and collect failure messages."""
    messages = []
    try:
        result = subprocess.run(
            ['python', 'llm_inserted_assertions.py', function_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        
        if result.stdout.strip():
            messages.append(FailureMessage(
                method=TestMethod.ASSERTION,
                function_name=function_name,
                message=result.stdout.strip()
            ))
    except Exception as e:
        messages.append(FailureMessage(
            method=TestMethod.ASSERTION,
            function_name=function_name,
            message=str(e)
        ))
    
    return messages

def score_message_quality(message: str) -> float:
    """
    Score the quality of a failure message based on several factors:
    1. Specificity (0-0.3)
    2. Actionability (0-0.3)
    3. Context (0-0.2)
    4. Technical Detail (0-0.2)
    """
    score = 0.0
    
    # 1. Specificity (0-0.3)
    if "must be" in message or "should be" in message:
        score += 0.1
    if "expected" in message and "got" in message:
        score += 0.2
    
    # 2. Actionability (0-0.3)
    if "fix" in message or "correct" in message:
        score += 0.1
    if "check" in message or "verify" in message:
        score += 0.1
    if "ensure" in message or "make sure" in message:
        score += 0.1
    
    # 3. Context (0-0.2)
    if "when" in message or "during" in message:
        score += 0.1
    if "because" in message or "due to" in message:
        score += 0.1
    
    # 4. Technical Detail (0-0.2)
    if any(term in message for term in ["type", "value", "range", "bound"]):
        score += 0.1
    if any(term in message for term in ["assertion", "condition", "constraint"]):
        score += 0.1
    
    return min(score, 1.0)  # Cap at 1.0

def evaluate_function(function_name: str) -> List[FailureMessage]:
    """Run all testing methods on a function and evaluate failure messages."""
    messages = []
    
    # Run all testing methods
    messages.extend(run_crosshair(function_name))
    messages.extend(run_fuzzing(function_name))
    messages.extend(run_assertion_test(function_name))
    
    # Score each message
    for message in messages:
        message.score = score_message_quality(message.message)
    
    return messages

def run_nagini(function_name: str) -> bool:
    """Run Nagini verification on a specific function."""
    try:
        result = subprocess.run(
            ['python', 'nagini.py', function_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        return "Verification successful" in result.stdout
    except Exception:
        return False

def get_difficulty(function_name: str) -> int:
    """Get difficulty rating for a function (1-10)."""
    # This is a simplified difficulty rating based on function complexity
    try:
        with open('functions.py', 'r') as f:
            content = f.read()
            function_match = re.search(f'def {function_name}.*?(?=def|\Z)', content, re.DOTALL)
            if function_match:
                function_code = function_match.group(0)
                # Simple metric: count control structures and operations
                complexity = (
                    function_code.count('if') +
                    function_code.count('for') +
                    function_code.count('while') +
                    function_code.count('+') +
                    function_code.count('*') +
                    len(re.findall(r'[<>]=?', function_code))
                )
                return min(max(complexity, 1), 10)
    except Exception:
        pass
    return 1

def main():
    # Get list of functions to test
    with open('functions.py', 'r') as f:
        content = f.read()
        functions = re.findall(r'def (\w+)\s*\(', content)
    
    # Prepare table headers
    headers = ["Program", "Difficulty (1-10)", "Fuzz Testing", "CrossHair Result", "Nagini Result", "Counterexample Input"]
    table_data = []
    
    for function in functions:
        print(f"\nEvaluating {function}...")
        
        # Get difficulty rating
        difficulty = get_difficulty(function)
        
        # Run all tests
        fuzz_results = run_fuzzing(function)
        crosshair_results = run_crosshair(function)
        nagini_result = run_nagini(function)
        
        # Determine results
        fuzz_status = "Pass" if not fuzz_results else "Fail"
        crosshair_status = "Pass" if not crosshair_results else "Fail"
        nagini_status = "Pass" if nagini_result else "Fail"
        
        # Get counterexample if any test failed
        counterexample = "N/A"
        for result in (fuzz_results + crosshair_results):
            if result.message:
                match = re.search(r'Input: (.*?)(?=\n|$)', result.message)
                if match:
                    counterexample = match.group(1)
                    break
        
        # Add row to table
        table_data.append([
            function,
            difficulty,
            fuzz_status,
            crosshair_status,
            nagini_status,
            counterexample
        ])
    
    # Sort table by difficulty
    table_data.sort(key=lambda x: (-x[1], x[0]))
    
    # Print table
    print("\nTest Results Summary")
    print("=" * 80)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    # Save results as JSON
    results_dict = {
        row[0]: {
            "difficulty": row[1],
            "fuzz_testing": row[2],
            "crosshair_result": row[3],
            "nagini_result": row[4],
            "counterexample": row[5]
        }
        for row in table_data
    }
    
    with open('test_results_summary.json', 'w') as f:
        json.dump(results_dict, f, indent=2)

if __name__ == "__main__":
    main() 