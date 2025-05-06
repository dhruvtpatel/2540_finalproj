# # Step 3: Define the function to run CrossHair on a module
# import subprocess
# from symbolic_execution_specs import transform_programs

# def run_crosshair(module_name):
#     try:
#         result = subprocess.run(['crosshair', 'check', module_name],
#                                 stdout=subprocess.PIPE,
#                                 stderr=subprocess.PIPE,
#                                 text=True,
#                                 check=True)
#         print(f"✓ PASSED: {module_name}")
#     except subprocess.CalledProcessError as e:
#         print(f"✗ FAILED: {module_name}")
#         print(f"  Error output: {e.stderr.decode() if e.stderr else 'No error output'}")
#         print(f"  Return code: {e.returncode}")

# print("CrossHair Test Results")
# print("=====================")
# for module in transform_programs.keys():
#     run_crosshair(module)

# Step 3: Define the function to run CrossHair on a module
import subprocess
from symbolic_execution_specs import transform_programs

def run_crosshair(module_name):
    print(f"Running CrossHair on {module_name}...")
    try:
        result = subprocess.run(['crosshair', 'check', module_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                check=True)
        if result.stdout.strip() == "":
            print("No counterexamples found")
        else:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("CrossHair detected counterexamples:")
        print(e.stdout)
        print(e.stderr)

for module in transform_programs.keys():
    run_crosshair(module)