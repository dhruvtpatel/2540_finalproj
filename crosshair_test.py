"""
CrossHair test script to verify assertion equivalence between early and late assertions.
"""

import sys
import importlib
import inspect
from typing import Any, Dict, Optional, Tuple
import time
from crosshair import check, AnalysisMessage, MessageType

def extract_assertions(func: callable) -> tuple[str, str]:
    """Extract early and late assertions from a function's source code."""
    source = inspect.getsource(func)
    early_assert = None
    late_assert = None
    
    for line in source.split('\n'):
        if 'assert' in line:
            if 'Final check' in line:
                late_assert = line.strip()
            else:
                early_assert = line.strip()
    
    if not early_assert or not late_assert:
        raise ValueError("Could not find both assertions")
    
    # Extract the conditions
    early_cond = early_assert.split('assert')[1].split(',')[0].strip()
    late_cond = late_assert.split('assert')[1].split(',')[0].strip()
    
    return early_cond, late_cond

def create_verification_function(func: callable) -> callable:
    """Create a CrossHair verification function to check assertion equivalence."""
    early_cond, late_cond = extract_assertions(func)
    sig = inspect.signature(func)
    
    def verification_wrapper(*args, **kwargs):
        # Get the local variables
        locals_dict = kwargs.copy()
        
        # Evaluate early assertion
        early_result = eval(early_cond, globals(), locals_dict)
        
        # If early assertion passes, late assertion must pass
        if early_result:
            late_result = eval(late_cond, globals(), locals_dict)
            if not late_result:
                raise AssertionError("Late assertion failed when early assertion passed")
        
        # If late assertion passes, early assertion must pass
        late_result = eval(late_cond, globals(), locals_dict)
        if late_result:
            early_result = eval(early_cond, globals(), locals_dict)
            if not early_result:
                raise AssertionError("Early assertion failed when late assertion passed")
        
        return True
    
    verification_wrapper.__signature__ = sig
    verification_wrapper.__name__ = f"verify_{func.__name__}"
    
    return verification_wrapper

def verify_assertion_equivalence(func_name: str) -> Tuple[bool, Optional[Dict[str, Any]]]:
    """Verify that early and late assertions are equivalent using CrossHair."""
    try:
        # Import the function
        module = importlib.import_module('functions_with_assertions')
        func = getattr(module, func_name)
        
        # Create verification function
        verify_func = create_verification_function(func)
        
        # Run CrossHair verification
        messages = list(check(verify_func))
        
        # Check for any counterexamples
        for msg in messages:
            if msg.message_type == MessageType.CANNOT_CONFIRM:
                return False, msg.state
        
        return True, None
        
    except Exception as e:
        print(f"Error during verification: {e}")
        return False, None

def main():
    if len(sys.argv) != 2:
        print("Usage: python crosshair_test.py <function_name>")
        sys.exit(1)
    
    function_name = sys.argv[1]
    
    print(f"Verifying assertion equivalence for {function_name}...")
    start_time = time.time()
    
    is_equivalent, counterexample = verify_assertion_equivalence(function_name)
    
    runtime = time.time() - start_time
    
    if not is_equivalent:
        if counterexample:
            print(f"Assertions are not equivalent (found in {runtime:.2f} seconds)")
            print(f"Counterexample: {counterexample}")
        else:
            print(f"Could not verify equivalence (after {runtime:.2f} seconds)")
    else:
        print(f"Assertions are equivalent (verified in {runtime:.2f} seconds)")

if __name__ == "__main__":
    main() 