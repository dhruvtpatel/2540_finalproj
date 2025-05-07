#!/usr/bin/env python3
"""
Script to update nagini_results.json and nagini_conversion_results.json based on translation failures.
Also removes files that fail translation from the nagini_modules directory.
"""
import json
import os
import re

def update_files():
    """
    Update nagini_results.json and nagini_conversion_results.json.
    Also removes files that fail translation from the nagini_modules directory.
    """
    # Load the nagini_results.json file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_file = os.path.join(script_dir, "nagini_results.json")
    conversion_file = os.path.join(script_dir, "nagini_conversion_results.json")
    modules_dir = os.path.join(script_dir, "nagini_modules")
    
    with open(results_file, 'r') as f:
        results_data = json.load(f)
    
    with open(conversion_file, 'r') as f:
        conversion_data = json.load(f)
    
    # Identify modules with translation failures
    translation_failures = []
    updated_results = []
    deleted_files = []
    
    for result in results_data["results"]:
        module_name = result["module"]
        module_path = result["path"]
        base_name = os.path.splitext(module_name)[0]
        transformed_name = f"{base_name}_transformed"
        
        if "Translation failed" in result["full_log"]:
            translation_failures.append((module_name, transformed_name, result["full_log"]))
            
            # Delete the file if it exists
            if os.path.exists(module_path):
                try:
                    os.remove(module_path)
                    deleted_files.append(module_name)
                    print(f"Deleted file: {module_path}")
                except Exception as e:
                    print(f"Error deleting file {module_path}: {e}")
        else:
            updated_results.append(result)
    
    # Update nagini_results.json to remove translation failures
    results_data["results"] = updated_results
    
    # Update the summary statistics
    success_count = sum(1 for r in updated_results if r["verification_result"] == "success")
    failure_count = sum(1 for r in updated_results if r["verification_result"] == "failure")
    error_count = sum(1 for r in updated_results if r["verification_result"] == "error")
    verified_total = success_count + failure_count + error_count
    total = len(updated_results)
    
    results_data["summary"]["total_modules"] = total
    results_data["summary"]["verified_modules"] = verified_total
    results_data["summary"]["success_count"] = success_count
    results_data["summary"]["failure_count"] = failure_count
    results_data["summary"]["error_count"] = error_count
    results_data["summary"]["success_rate"] = (success_count / verified_total * 100) if verified_total > 0 else 0
    
    # Update nagini_conversion_results.json based on translation failures
    updated_conversion_entries = 0
    for module_name, transformed_name, error_log in translation_failures:
        if transformed_name in conversion_data:
            # Extract the unsupported feature from the error message
            reason = extract_reason_from_error(error_log, module_name)
            
            # Update the conversion result
            conversion_data[transformed_name]["convertible"] = False
            conversion_data[transformed_name]["nagini_code"] = None
            conversion_data[transformed_name]["reason"] = reason
            updated_conversion_entries += 1
    
    # Save the updated files
    with open(results_file, 'w') as f:
        json.dump(results_data, f, indent=2)
    
    with open(conversion_file, 'w') as f:
        json.dump(conversion_data, f, indent=2)
    
    print(f"Removed {len(translation_failures)} translation failures from {results_file}")
    print(f"Deleted {len(deleted_files)} files from {modules_dir}")
    print(f"Updated {updated_conversion_entries} entries in {conversion_file}")
    
    if deleted_files:
        print("\nDeleted files:")
        for file in deleted_files:
            print(f"  - {file}")

def extract_reason_from_error(error_log, module_name):
    """Extract a meaningful reason from the error log"""
    
    if "while (i < len" in error_log:
        pattern = r"while \(i < len\(([^)]+)\)\):\s+([^\n]+)"
        match = re.search(pattern, error_log)
        if match:
            var_name = match.group(1)
            operation = match.group(2).strip()
            return f"Nagini does not support while loops with collection indexing. Specifically, it cannot translate the pattern 'while (i < len({var_name}))' with operations like '{operation}'. This is a limitation in Nagini's handling of loops over collections with explicit index bounds checking."
    
    if "Unsupported type: AnyType" in error_log:
        return "Nagini requires explicit type information for collections. Generic list types cannot be used; instead, specific types like List[int] must be specified. This is a limitation in Nagini's type system which requires concrete type information for verification."
    
    # Default reason
    return f"The code in {module_name} uses features that are not supported by Nagini's translation system. The specific unsupported pattern appears to be related to collection iteration or type handling. Nagini has limitations regarding while loops with indexing, type specifications, and certain operations on collections."

if __name__ == "__main__":
    update_files() 