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

def main():
    # Get list of functions to test
    with open('functions.py', 'r') as f:
        content = f.read()
        functions = re.findall(r'def (\w+)\s*\(', content)
    
    all_results = {}
    
    for function in functions:
        print(f"\nEvaluating {function}...")
        results = evaluate_function(function)
        all_results[function] = [
            {
                "method": msg.method.value,
                "message": msg.message,
                "score": msg.score
            }
            for msg in results
        ]
    
    # Save results
    with open('failure_explanation_quality.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    
    # Print summary
    print("\nFailure Explanation Quality Summary:")
    print("=" * 50)
    for function, results in all_results.items():
        print(f"\n{function}:")
        if not results:
            print("  ✓ No failures found")
            continue
            
        for result in results:
            score_str = f"{result['score']:.2f}/1.00"
            print(f"  {result['method']}: {score_str}")
            print(f"    Message: {result['message']}")

if __name__ == "__main__":
    main() 