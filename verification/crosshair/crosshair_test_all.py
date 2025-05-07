"""
CrossHair Testing for All Transformed Functions
This script runs CrossHair verification on all transformed functions.
"""

import math
import subprocess
import os
import sys
import json
import datetime
import re

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

from code_files.b_llm_assertion_programs.symbolic_execution_specs import transform_programs

MODULES_DIR = os.path.join(PROJECT_ROOT, 'verification', 'crosshair', 'crosshair_modules')
RESULTS_DIR = os.path.join(PROJECT_ROOT, 'verification', 'crosshair')

# Ensure directories exist
os.makedirs(MODULES_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

print(f"Current working directory: {os.getcwd()}")
print(f"Modules directory: {MODULES_DIR}")
print(f"Results directory: {RESULTS_DIR}")

# Write each module to disk
for module_name, code in transform_programs.items():
    module_path = os.path.join(MODULES_DIR, module_name)
    # Prepend standard imports
    full_code = f"import math\nimport datetime\n\n{code}"
    with open(module_path, 'w') as f:
        f.write(full_code)

print(f"Modules written successfully to {MODULES_DIR}\n")

# Install crosshair if not already installed
try:
    subprocess.run(['crosshair', '--version'], capture_output=True, check=True)
except (subprocess.SubprocessError, FileNotFoundError):
    print("Installing crosshair...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'crosshair-tool'], check=True)

# Results will be stored in this list
results = []
passed_count = 0
failed_count = 0

# Run CrossHair on each module
for module_name in transform_programs.keys():
    module_path = os.path.join(MODULES_DIR, f'{module_name}')
    print(f"Running CrossHair on {module_name}...")
    result = subprocess.run(
        [sys.executable, '-m', 'crosshair', 'check', '--verbose', module_path],
        capture_output=True,
        text=True
    )
    
    # Complete output log
    full_log = result.stdout + result.stderr
    
    # Print concise output to console for monitoring
    print(f"Output from CrossHair (summary):")
    for line in full_log.splitlines():
        if "error:" in line or "warning:" in line:
            print(line)
    
    # Process the result
    has_assertion_error = "AssertionError" in full_log
    
    # Extract specific error message if there's an assertion error
    failure_reason = ""
    if has_assertion_error:
        error_match = re.search(r'AssertionError: (.*?when calling.*?\))', full_log, re.DOTALL)
        if error_match:
            failure_reason = error_match.group(1).strip()
        else:
            failure_reason = "AssertionError detected but could not extract specific message"
    else: 
        failure_reason = "No assertion error detected"
        
    # Determine pass/fail status
    if has_assertion_error:
        status = "failed"
        failed_count += 1
    else:
        status = "passed"
        passed_count += 1
    
    # Store result data
    result_data = {
        "program": module_name,
        "failure_reason": failure_reason,
        "assertion_equivalence_result": "false" if has_assertion_error else "true",
        "full_log": full_log
    }
    
    results.append(result_data)
    print(f"Status: {status}")
    if failure_reason and failure_reason != "No assertion error detected":
        print(f"Failure reason: {failure_reason}")
    print()

# Create timestamp for the results file
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
results_file = os.path.join(RESULTS_DIR, f"crosshair_results.json")

# Write results to JSON file
with open(results_file, 'w') as f:
    json.dump(results, f, indent=2)

# Print summary statistics
total_count = passed_count + failed_count
print("\n===== Summary Statistics =====")
print(f"Total programs tested: {total_count}")
print(f"Passed: {passed_count} ({passed_count/total_count*100:.2f}%)")
print(f"Failed: {failed_count} ({failed_count/total_count*100:.2f}%)")
print(f"Results written to: {results_file}")