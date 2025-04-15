"""
System to run CrossHair symbolic execution on transformed functions.
This script provides functionality to run CrossHair on individual modules or all modules at once.
"""

import subprocess
import os
import time
from typing import List, Dict, Optional
import json

def run_crosshair(module_name: str, timeout: int = 30) -> Dict:
    """
    Run CrossHair on a single module and return the results.
    
    Args:
        module_name: Name of the module to test
        timeout: Maximum time to run CrossHair in seconds
        
    Returns:
        Dictionary containing test results
    """
    print(f"\nRunning CrossHair on {module_name}...")
    start_time = time.time()
    
    try:
        result = subprocess.run(
            ['crosshair', 'check', module_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            check=True
        )
        
        runtime = time.time() - start_time
        
        if result.stdout.strip() == "":
            return {
                "module": module_name,
                "status": "success",
                "counterexamples": [],
                "runtime": runtime,
                "error": None
            }
        else:
            return {
                "module": module_name,
                "status": "counterexamples_found",
                "counterexamples": result.stdout.strip().split('\n'),
                "runtime": runtime,
                "error": None
            }
            
    except subprocess.CalledProcessError as e:
        runtime = time.time() - start_time
        return {
            "module": module_name,
            "status": "counterexamples_found",
            "counterexamples": e.stdout.strip().split('\n'),
            "runtime": runtime,
            "error": e.stderr
        }
    except subprocess.TimeoutExpired:
        runtime = time.time() - start_time
        return {
            "module": module_name,
            "status": "timeout",
            "counterexamples": [],
            "runtime": runtime,
            "error": f"CrossHair timed out after {timeout} seconds"
        }
    except Exception as e:
        runtime = time.time() - start_time
        return {
            "module": module_name,
            "status": "error",
            "counterexamples": [],
            "runtime": runtime,
            "error": str(e)
        }

def run_all_crosshair(modules: List[str], timeout: int = 30) -> List[Dict]:
    """
    Run CrossHair on all specified modules and return combined results.
    
    Args:
        modules: List of module names to test
        timeout: Maximum time to run CrossHair on each module in seconds
        
    Returns:
        List of dictionaries containing test results for each module
    """
    results = []
    total_modules = len(modules)
    
    for i, module in enumerate(modules, 1):
        print(f"\nProcessing module {i}/{total_modules}: {module}")
        result = run_crosshair(module, timeout)
        results.append(result)
        
        # Print summary for this module
        if result["status"] == "success":
            print(f"✓ {module}: No counterexamples found (runtime: {result['runtime']:.2f}s)")
        elif result["status"] == "counterexamples_found":
            print(f"✗ {module}: Counterexamples found (runtime: {result['runtime']:.2f}s)")
            for counterexample in result["counterexamples"]:
                print(f"  - {counterexample}")
        elif result["status"] == "timeout":
            print(f"⚠ {module}: Timed out after {timeout}s")
        else:
            print(f"⚠ {module}: Error - {result['error']}")
    
    return results

def save_results(results: List[Dict], filename: str = "crosshair_results.json"):
    """Save CrossHair results to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {filename}")

def main():
    # Test functions_with_assertions.py
    module = "functions_with_assertions.py"
    
    if not os.path.exists(module):
        print(f"Error: {module} not found!")
        return
    
    print(f"Running CrossHair on {module}")
    result = run_crosshair(module, timeout=60)  # Increased timeout for larger file
    
    # Save results
    save_results([result])
    
    # Print summary
    if result["status"] == "success":
        print("\n✓ All functions passed verification!")
    elif result["status"] == "counterexamples_found":
        print("\n✗ Counterexamples found:")
        for counterexample in result["counterexamples"]:
            print(f"  - {counterexample}")
    else:
        print(f"\n⚠ Error: {result['error']}")

if __name__ == "__main__":
    main() 