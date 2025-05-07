#!/usr/bin/env python3
"""
Script to compile all verification results across methods.

This script combines results from:
- Program difficulty scores
- CrossHair verification
- Fuzzing verification
- Nagini verification
- Failure Explanation Quality (FEQ) scores

Output is a JSON file that aggregates results for each program.
"""

import json
import os
import re
import sys
from collections import defaultdict

# Directory structure
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
RESULTS_DIR = PROJECT_ROOT
DIFFICULTY_FILE = os.path.join(PROJECT_ROOT, "..", "difficulty", "program_difficulty_scores.json")
CROSSHAIR_FILE = os.path.join(PROJECT_ROOT, "crosshair", "crosshair_results.json")
FUZZ_FILE = os.path.join(PROJECT_ROOT, "fuzz", "fuzz_results.json")
NAGINI_FILE = os.path.join(PROJECT_ROOT, "nagini", "nagini_results.json")
FEQ_FILE = os.path.join(PROJECT_ROOT, "failure_explanation_quality", "feq_evaluation_results.json")

# Output file
OUTPUT_FILE = os.path.join(RESULTS_DIR, "all_results.json")

def normalize_program_name(name):
    """Normalize program names to handle variations in different result files."""
    # Remove any suffixes like "_transformed" or ".py" or "_module"
    name = re.sub(r'(_transformed|\.py|_module\.py|_module)$', '', name)
    return name

def load_json_file(file_path):
    """Load a JSON file and return its contents."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading {file_path}: {e}")
        return []

def get_program_difficulty(difficulty_data, program_name):
    """Extract difficulty score for a program."""
    for entry in difficulty_data:
        if normalize_program_name(entry.get("program", "")) == program_name:
            return entry.get("difficulty_score", None)
    return None

def get_fuzz_result(fuzz_data, program_name):
    """Extract fuzz testing result for a program."""
    norm_name = f"{program_name}_transformed"
    for entry in fuzz_data:
        if normalize_program_name(entry.get("program", "")) == normalize_program_name(norm_name):
            return "pass" if entry.get("pass", False) else "fail"
    return "unsupported"

def get_crosshair_result(crosshair_data, program_name):
    """Extract CrossHair verification result for a program."""
    for entry in crosshair_data:
        entry_program = entry.get("program", "")
        if normalize_program_name(entry_program) == program_name:
            # CrossHair passes if assertion_equivalence_result is "true"
            return "pass" if entry.get("assertion_equivalence_result") == "true" else "fail"
    return "unsupported"

def get_nagini_result(nagini_data, program_name):
    """Extract Nagini verification result for a program."""
    for entry in nagini_data.get("results", []):
        module_name = os.path.splitext(os.path.basename(entry.get("module", "")))[0]
        if normalize_program_name(module_name) == program_name:
            return "pass" if entry.get("verification_result") == "success" else "fail"
    return "unsupported"

def get_feq_scores(feq_data, program_name):
    """Extract FEQ scores for a program across verification methods."""
    scores = {
        "fuzz": "NA",
        "crosshair": "NA",
        "nagini": "NA"
    }
    
    for entry in feq_data:
        function_name = normalize_program_name(entry.get("function", ""))
        if function_name == f"{program_name}_module" or function_name == program_name:
            method = entry.get("method", "").lower()
            if method in scores:
                scores[method] = entry.get("feq_score", "NA")
    
    return scores

def main():
    """Main function to gather and compile all results."""
    # Load data files
    difficulty_data = load_json_file(DIFFICULTY_FILE)
    crosshair_data = load_json_file(CROSSHAIR_FILE)
    fuzz_data = load_json_file(FUZZ_FILE)
    nagini_data = load_json_file(NAGINI_FILE)
    feq_data = load_json_file(FEQ_FILE)
    
    # Set of all program names
    program_names = set()
    
    # Extract all program names from difficulty data
    for entry in difficulty_data:
        program_names.add(normalize_program_name(entry.get("program", "")))
    
    # Add program names from fuzz data
    for entry in fuzz_data:
        program_names.add(normalize_program_name(entry.get("program", "")))
    
    # Compile results for each program
    all_results = []
    for program in sorted(program_names):
        difficulty = get_program_difficulty(difficulty_data, program)
        fuzz_result = get_fuzz_result(fuzz_data, program)
        crosshair_result = get_crosshair_result(crosshair_data, program)
        nagini_result = get_nagini_result(nagini_data, program)
        feq_scores = get_feq_scores(feq_data, program)
        
        result = {
            "program": program,
            "difficulty": difficulty,
            "fuzz": fuzz_result,
            "crosshair": crosshair_result,
            "nagini": nagini_result,
            "feq": feq_scores
        }
        
        all_results.append(result)
    
    # Write results to JSON file
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"Results compiled and written to {OUTPUT_FILE}")
    print(f"Total programs: {len(all_results)}")

if __name__ == "__main__":
    main()
