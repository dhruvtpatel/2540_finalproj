#!/usr/bin/env python3
"""
Script to convert transformed programs to Nagini specification language.
This script uses GPT-4.1 to generate Nagini specifications for each transformed function.
"""

import os
import sys
import json
import inspect
import importlib.util
from importlib.machinery import ModuleSpec
from pathlib import Path
from typing import Dict, List, Optional, Any, Union, cast
from dataclasses import dataclass
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the project root directory and set up path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

# Import the transformed functions module using absolute path to ensure it works from any directory
transformed_module_path = os.path.join(PROJECT_ROOT, "code_files", "c_transformed_programs", "transformed_functions.py")
if not os.path.exists(transformed_module_path):
    print(f"Error: Transformed functions file not found at {transformed_module_path}")
    sys.exit(1)

spec = importlib.util.spec_from_file_location("transformed_functions", transformed_module_path)
if spec is None:
    print(f"Error: Could not create module spec from {transformed_module_path}")
    sys.exit(1)

# At this point we know spec is not None
module_spec = cast(ModuleSpec, spec)
transformed_module = importlib.util.module_from_spec(module_spec)
if module_spec.loader is None:
    print(f"Error: Module spec has no loader")
    sys.exit(1)

module_spec.loader.exec_module(transformed_module)

# Define models for OpenAI structured output
class NaginiConversionResult(BaseModel):
    """Model for the result of converting a function to Nagini specifications."""
    convertible: bool
    nagini_code: Optional[str] = None
    reason: Optional[str] = None

class NaginiConversion:
    """Handles conversion of transformed functions to Nagini specification language."""
    
    def __init__(self):
        # Check for API key
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Error: OPENAI_API_KEY environment variable not set")
        
        self.client = OpenAI(api_key=api_key)
        self.output_dir = os.path.join(SCRIPT_DIR, "nagini_modules")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load Nagini documentation
        self.nagini_docs = self._load_nagini_documentation()
    
    def _load_nagini_documentation(self) -> str:
        """Load Nagini documentation from markdown files."""
        nagini_wiki_dir = os.path.join(PROJECT_ROOT, "wikis", "nagini")
        
        docs = []
        for filename in ["Home.md", "Information-Flow-Specifications.md"]:
            file_path = os.path.join(nagini_wiki_dir, filename)
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    docs.append(f.read())
            else:
                print(f"Warning: Documentation file {file_path} not found")
        
        return "\n\n".join(docs)
    
    def get_function_source(self, func_name: str) -> str:
        """Get the source code of a function from the transformed module."""
        func = getattr(transformed_module, func_name, None)
        if not func:
            return f"Function {func_name} not found in transformed module."
        
        return inspect.getsource(func)
    
    def convert_function(self, func_name: str) -> NaginiConversionResult:
        """Convert a function to Nagini specification language using GPT-4.1."""
        function_source = self.get_function_source(func_name)
        
        # System prompt with Nagini documentation and instructions
        system_prompt = f"""You are an expert in formal verification and the Nagini specification language. 
Your task is to convert Python functions into the Nagini specification language.

Here is documentation on the Nagini specification language:

{self.nagini_docs}

The input you will receive is a Python function that has been transformed to check assertion equivalence.
Your task is to convert this function to use Nagini's formal verification approach.

These functions typically have:
1. An early assertion `b_early`
2. Some computation
3. A final assertion `b_final`
4. An assertion checking if `b_early == b_final`

For your conversion:
1. If the function can be converted to Nagini, set `convertible` to true and provide the Nagini code.
2. If the function cannot be converted to Nagini due to unsupported features, set `convertible` to false and explain why.

Focus on:
- Converting the assertion checks to appropriate pre/post conditions
- Using Nagini's Pure functions where appropriate
- Using Nagini's contracts system correctly
- Following Nagini's syntax for permissions and assertions

Unsupported features might include:
- Complex operations that can't be represented in Nagini's specification language
- Features like randomness that aren't compatible with formal verification
- Constructs that Nagini doesn't support

Your output should be a valid Python file that can be verified by Nagini.
Do not use type assertions under any circumstances.

Make sure to include the import for nagini_contracts at the top of the file:
from nagini_contracts.contracts import *
"""
        
        # User message with the function to convert
        user_message = f"""
Convert the following function to Nagini specification language:

```python
{function_source}
```

Analyze if this function can be properly converted to Nagini, or if there are features in it that cannot be represented in Nagini's specification language.
"""
        
        try:
            # Use the parse method with Pydantic model for structured output
            completion = self.client.beta.chat.completions.parse(
                model="gpt-4o",  # Using 4o since 4.1 specifically may not be available
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                response_format=NaginiConversionResult,
            )
            
            # Get the parsed data from the response
            parsed_result = completion.choices[0].message.parsed
            return parsed_result
        
        except Exception as e:
            print(f"Error calling OpenAI API for {func_name}: {e}")
            return NaginiConversionResult(
                convertible=False,
                reason=f"API error: {str(e)}"
            )
    
    def save_nagini_module(self, func_name: str, nagini_code: str) -> str:
        """Save a Nagini module to the output directory."""
        # Create filename from function name without the '_transformed' suffix
        base_name = func_name
        if base_name.endswith("_transformed"):
            base_name = base_name[:-12]
        
        filename = f"{base_name}.py"
        file_path = os.path.join(self.output_dir, filename)
        
        with open(file_path, 'w') as f:
            f.write(nagini_code)
        
        return file_path
    
    def convert_all_functions(self) -> Dict[str, NaginiConversionResult]:
        """Convert all transformed functions from the module."""
        results = {}
        
        # Get all transformed functions from the module
        transformed_funcs = [
            name for name in dir(transformed_module) 
            if name.endswith("_transformed") and callable(getattr(transformed_module, name))
        ]
        
        for i, func_name in enumerate(transformed_funcs):
            print(f"Converting {i+1}/{len(transformed_funcs)}: {func_name}")
            
            result = self.convert_function(func_name)
            results[func_name] = result
            
            # Save convertible functions to Nagini modules
            if result.convertible and result.nagini_code:
                file_path = self.save_nagini_module(func_name, result.nagini_code)
                print(f"  Saved to {file_path}")
            else:
                print(f"  Not convertible: {result.reason}")
        
        return results
    
    def save_results_json(self, results: Dict[str, NaginiConversionResult]) -> str:
        """Save the conversion results to a JSON file."""
        serialized_results = {}
        
        for func_name, result in results.items():
            serialized_results[func_name] = {
                "convertible": result.convertible,
                "nagini_code": result.nagini_code if result.convertible else None,
                "reason": result.reason if not result.convertible else None
            }
        
        output_file = os.path.join(SCRIPT_DIR, "nagini_conversion_results.json")
        with open(output_file, 'w') as f:
            json.dump(serialized_results, f, indent=2)
        
        return output_file

def main():
    """Main function to convert all transformed functions."""
    print(f"Script directory: {SCRIPT_DIR}")
    print(f"Project root: {PROJECT_ROOT}")
    
    converter = NaginiConversion()
    
    print("Converting transformed functions to Nagini specification language...")
    results = converter.convert_all_functions()
    
    # Save results to JSON
    output_file = converter.save_results_json(results)
    
    # Print summary
    convertible = sum(1 for r in results.values() if r.convertible)
    total = len(results)
    
    print("\nConversion Summary:")
    print(f"Total functions: {total}")
    print(f"Convertible to Nagini: {convertible} ({convertible/total*100:.2f}%)")
    print(f"Not convertible: {total - convertible} ({(total-convertible)/total*100:.2f}%)")
    print(f"\nDetailed results saved to {output_file}")
    
    print(f"\nYou can verify the generated Nagini modules using:\n{os.path.join(SCRIPT_DIR, 'verify_nagini_modules.py')}")

if __name__ == "__main__":
    main() 