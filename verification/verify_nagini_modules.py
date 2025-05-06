#!/usr/bin/env python3
import os
import subprocess
import sys


def verify_module(module_path):
    """Verify a single module with Nagini."""
    print(f"Verifying {module_path}...")
    try:
        result = subprocess.run(
            ["nagini", "--float-encoding", "real", module_path],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"✅ {module_path}: Verified")
            return True
        else:
            print(f"❌ {module_path}: Failed")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"Error verifying {module_path}: {e}")
        return False


def main():
    """Verify all modules in nagini_modules directory."""
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    modules_dir = os.path.join(script_dir, "nagini_modules")

    if not os.path.exists(modules_dir):
        print(f"Error: Directory {modules_dir} does not exist.")
        return 1

    # Get all Python files in the directory
    python_files = [
        os.path.join(modules_dir, f)
        for f in os.listdir(modules_dir)
        if f.endswith(".py")
    ]

    if not python_files:
        print(f"No Python files found in {modules_dir}.")
        return 1

    # Verify each file
    success_count = 0
    for module_path in sorted(python_files):
        if verify_module(module_path):
            success_count += 1

    total = len(python_files)
    print(f"\nSummary: {success_count}/{total} modules verified successfully.")

    return 0 if success_count == total else 1


if __name__ == "__main__":
    sys.exit(main())
