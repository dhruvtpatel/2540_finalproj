"""
CrossHair Testing for All Transformed Functions
This script runs CrossHair verification on all transformed functions.
"""

import math
import subprocess
import os
from symbolic_execution_specs import transform_programs

# Create directory for modules if it doesn't exist
os.makedirs('crosshair_modules', exist_ok=True)

# Write each module to disk
for module_name, code in transform_programs.items():
    with open(f'crosshair_modules/{module_name}.py', 'w') as f:
        f.write(code)

print("Modules written successfully.\n")

# Run CrossHair on each module
for module_name in transform_programs.keys():
    print(f"Running CrossHair on {module_name}...")
    result = subprocess.run(
        ['crosshair', 'check', f'crosshair_modules/{module_name}.py'],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    print() 