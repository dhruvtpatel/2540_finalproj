"""
System to evaluate the quality of failure explanations across different testing methods.
This script analyzes failure messages from CrossHair, fuzzing, and Nagini test results.
It uses OpenAI to evaluate false positives and score explanation quality.
"""

import json
import os
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Any
from tabulate import tabulate
import re
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

class TestMethod(Enum):
    CROSSHAIR = "crosshair"
    FUZZING = "fuzzing"
    NAGINI = "nagini"

@dataclass
class FEQScore:
    """Failure Explanation Quality score with subscores and reasoning."""
    specificity: float 
    specificity_reason: str
    actionability: float
    actionability_reason: str
    context: float
    context_reason: str
    technical_detail: float
    technical_detail_reason: str
    false_positive: bool
    false_positive_reason: str
    
    @property
    def total_score(self) -> float:
        """Calculate the total FEQ score using the weighted formula."""
        return (0.3 * self.specificity + 
                0.3 * self.actionability + 
                0.2 * self.context + 
                0.2 * self.technical_detail)

@dataclass
class FailureEvaluation:
    method: TestMethod
    function_name: str
    message: str
    input_args: str
    feq_score: Optional[FEQScore] = None

def load_crosshair_results(file_path: str) -> List[Dict[str, Any]]:
    """Load CrossHair results from JSON file."""
    with open(file_path, 'r') as f:
        results = json.load(f)
    return results

def load_fuzzing_results(file_path: str) -> List[Dict[str, Any]]:
    """Load fuzzing results from JSON file."""
    with open(file_path, 'r') as f:
        results = json.load(f)
    return results

def load_nagini_results(file_path: str) -> Dict[str, Any]:
    """Load Nagini results from JSON file."""
    with open(file_path, 'r') as f:
        results = json.load(f)
    return results

def extract_failure_messages(crosshair_results: List[Dict], 
                            fuzzing_results: List[Dict],
                            nagini_results: Dict[str, Any]) -> List[FailureEvaluation]:
    """Extract failure messages from all testing methods.
    For CrossHair: One evaluation per failing program with full log
    For Fuzzing: One evaluation per program with all failing examples combined
    For Nagini: One evaluation per failing program with full log"""
    evaluations = []
    
    # # Process CrossHair results
    # for result in crosshair_results:
    #     program = result.get("program", "")
    #     if result.get("assertion_equivalence_result") == "false":
    #         # Include both the failure_reason and the full_log
    #         failure_reason = result.get("failure_reason", "")
    #         full_log = result.get("full_log", "")
    #         message = f"Failure Reason: {failure_reason}\n\nFull Log: {full_log}"
            
    #         input_match = re.search(r'when calling (.*)', failure_reason) if failure_reason else None
    #         input_args = input_match.group(1) if input_match else "unknown input"
            
    #         evaluations.append(FailureEvaluation(
    #             method=TestMethod.CROSSHAIR,
    #             function_name=program,
    #             message=message,
    #             input_args=input_args
    #         ))
    
    # # Process fuzzing results - consolidate failures per program
    # for result in fuzzing_results:
    #     program = result.get("program", "")
    #     failing_examples = result.get("failing_examples", [])
        
    #     # Only process programs with failing examples
    #     if failing_examples:
    #         # Combine all failing examples into a single message
    #         consolidated_message = f"Program {program} has {len(failing_examples)} failing examples:\n\n"
            
    #         for i, example in enumerate(failing_examples, 1):
    #             args = example.get("args", "unknown input")
    #             error = example.get("error", "")
    #             consolidated_message += f"Example {i}:\nInput: {args}\nError: {error}\n\n"
            
    #         # Use the first example's args as representative input
    #         representative_input = failing_examples[0].get("args", "multiple inputs") if failing_examples else "unknown input"
            
    #         evaluations.append(FailureEvaluation(
    #             method=TestMethod.FUZZING,
    #             function_name=program,
    #             message=consolidated_message,
    #             input_args=representative_input
    #         ))
    
    # Process Nagini results
    for result in nagini_results.get("results", []):
        if result.get("verification_result") == "failure":
            module = result.get("module", "").replace(".py", "")
            error_message = result.get("error_message", "")
            full_log = result.get("full_log", "")
            message = f"Error Message: {error_message}\n\nFull Log: {full_log}"
            
            # Extract line numbers or specific failure from the log if possible
            input_args = "N/A - static verification"
            
            evaluations.append(FailureEvaluation(
                method=TestMethod.NAGINI,
                function_name=module,
                message=message,
                input_args=input_args
            ))
    
    return evaluations

# Define Pydantic model for OpenAI structured output
class FEQScoreModel(BaseModel):
    false_positive: bool
    false_positive_reason: str
    specificity: float
    specificity_reason: str
    actionability: float
    actionability_reason: str
    context: float
    context_reason: str
    technical_detail: float
    technical_detail_reason: str

def evaluate_with_openai(evaluation: FailureEvaluation, client: OpenAI) -> FEQScore:
    """Use OpenAI to evaluate failure explanation quality."""
    # System prompt that explains the task
    system_prompt = """You are an expert at evaluating program failure explanations.
    Analyze the provided failure message to determine:
    1. If this is a false positive (the failure isn't related to assertion equivalence)
    2. Score the quality of the failure explanation on these dimensions:
       - Specificity (0-1): How precise and clear the error message is
       - Actionability (0-1): How well it guides the user to fix the issue
       - Context (0-1): How well it explains when/why the failure occurs
       - Technical Detail (0-1): How much implementation/technical information it provides
    
    Note that failures can come from different testing methods:
    - 'crosshair': Symbolic execution tool that explores multiple execution paths
    - 'fuzzing': Random testing with generated inputs
    - 'nagini': Static verification tool that proves program properties
    
    For static verification (nagini), focus on how well the error describes the 
    logical/formal verification failure rather than specific inputs.
    
    Provide a reason for each score."""
    
    # User message with the details of the failure
    user_message = f"""
    Testing Method: {evaluation.method.value}
    Function: {evaluation.function_name}
    Input: {evaluation.input_args}
    Failure Message: {evaluation.message}
    
    Analyze this failure message for its quality and determine if it's a false positive.
    """
    
    try:
        # Use the parse method with Pydantic model for structured output
        completion = client.beta.chat.completions.parse(
            model="gpt-4o",  # Update with available model
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            response_format=FEQScoreModel,
        )
        
        # Get the parsed data from the response
        parsed_result = completion.choices[0].message.parsed
        assert parsed_result is not None
        parsed_data: FEQScoreModel = parsed_result
        
        # Since we know the model returned a valid FEQScoreModel, we can safely use its attributes
        return FEQScore(
            specificity=parsed_data.specificity,
            specificity_reason=parsed_data.specificity_reason,
            actionability=parsed_data.actionability,
            actionability_reason=parsed_data.actionability_reason,
            context=parsed_data.context,
            context_reason=parsed_data.context_reason,
            technical_detail=parsed_data.technical_detail,
            technical_detail_reason=parsed_data.technical_detail_reason,
            false_positive=parsed_data.false_positive,
            false_positive_reason=parsed_data.false_positive_reason
        )
    
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        # Return default scores in case of API failure
        return FEQScore(
            specificity=0.0,
            specificity_reason="API error",
            actionability=0.0,
            actionability_reason="API error",
            context=0.0,
            context_reason="API error",
            technical_detail=0.0,
            technical_detail_reason="API error",
            false_positive=False,
            false_positive_reason="Could not determine due to API error"
        )

def main():
    # Path to result files
    crosshair_results_path = os.path.join(PROJECT_ROOT, "verification", "crosshair", "crosshair_results.json")
    fuzzing_results_path = os.path.join(PROJECT_ROOT, "verification", "fuzz", "fuzz_results.json")
    nagini_results_path = os.path.join(PROJECT_ROOT, "verification", "nagini", "nagini_results.json")
    
    # Load OpenAI API key from environment
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)
        
    client = OpenAI(api_key=api_key)
    
    # Load results
    print("Loading test results...")
    crosshair_results = load_crosshair_results(crosshair_results_path)
    fuzzing_results = load_fuzzing_results(fuzzing_results_path)
    nagini_results = load_nagini_results(nagini_results_path)
    
    # Extract failure messages
    evaluations = extract_failure_messages(crosshair_results, fuzzing_results, nagini_results)
    print(f"Found {len(evaluations)} failure evaluations to process")
    
    # Evaluate each failure message
    for i, evaluation in enumerate(evaluations):
        print(f"Evaluating failure {i+1}/{len(evaluations)}: {evaluation.function_name} ({evaluation.method.value})")
        feq_score = evaluate_with_openai(evaluation, client)
        evaluation.feq_score = feq_score
    
    # Prepare results for output
    table_data = []
    headers = [
        "Function", "Test Method", "Input", "FEQ Score", "False Positive", 
        "Specificity", "Actionability", "Context", "Technical Detail"
    ]
    
    for eval in evaluations:
        score = eval.feq_score
        if score:
            table_data.append([
                eval.function_name,
                eval.method.value,
                eval.input_args,
                f"{score.total_score:.2f}",
                f"{score.false_positive} ({score.false_positive_reason[:30]}...)" if len(score.false_positive_reason) > 30 else f"{score.false_positive} ({score.false_positive_reason})",
                f"{score.specificity:.2f} ({score.specificity_reason[:30]}...)" if len(score.specificity_reason) > 30 else f"{score.specificity:.2f} ({score.specificity_reason})",
                f"{score.actionability:.2f} ({score.actionability_reason[:30]}...)" if len(score.actionability_reason) > 30 else f"{score.actionability:.2f} ({score.actionability_reason})",
                f"{score.context:.2f} ({score.context_reason[:30]}...)" if len(score.context_reason) > 30 else f"{score.context:.2f} ({score.context_reason})",
                f"{score.technical_detail:.2f} ({score.technical_detail_reason[:30]}...)" if len(score.technical_detail_reason) > 30 else f"{score.technical_detail:.2f} ({score.technical_detail_reason})"
            ])
    
    # Sort by FEQ score descending
    table_data.sort(key=lambda x: float(x[3]), reverse=True)
    
    # Print table
    print("\nFailure Explanation Quality Evaluation Results")
    print("=" * 100)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    # Save detailed results as JSON
    detailed_results = []
    for eval in evaluations:
        if eval.feq_score:
            detailed_results.append({
                "function": eval.function_name,
                "method": eval.method.value,
                "input_args": eval.input_args,
                "message": eval.message,
                "feq_score": eval.feq_score.total_score,
                "false_positive": eval.feq_score.false_positive,
                "false_positive_reason": eval.feq_score.false_positive_reason,
                "specificity": {
                    "score": eval.feq_score.specificity,
                    "reason": eval.feq_score.specificity_reason
                },
                "actionability": {
                    "score": eval.feq_score.actionability,
                    "reason": eval.feq_score.actionability_reason
                },
                "context": {
                    "score": eval.feq_score.context,
                    "reason": eval.feq_score.context_reason
                },
                "technical_detail": {
                    "score": eval.feq_score.technical_detail,
                    "reason": eval.feq_score.technical_detail_reason
                }
            })
    
    with open(os.path.join(PROJECT_ROOT, "verification", "failure_explanation_quality", "feq_evaluation_results.json"), "w") as f:
        json.dump(detailed_results, f, indent=2)
    
    print(f"\nDetailed results saved to {os.path.join(PROJECT_ROOT, 'verification', 'failure_explanation_quality', 'feq_evaluation_results.json')}")
    
    # Calculate and print statistics
    true_positives = sum(1 for eval in evaluations if eval.feq_score and not eval.feq_score.false_positive)
    false_positives = sum(1 for eval in evaluations if eval.feq_score and eval.feq_score.false_positive)
    avg_feq = sum(eval.feq_score.total_score for eval in evaluations if eval.feq_score) / len(evaluations) if evaluations else 0
    
    # Add statistics per test method
    methods = [TestMethod.CROSSHAIR, TestMethod.FUZZING, TestMethod.NAGINI]
    print("\nStatistics by Test Method:")
    for method in methods:
        method_evals = [e for e in evaluations if e.method == method and e.feq_score]
        if method_evals:
            method_true_pos = sum(1 for e in method_evals if not e.feq_score.false_positive)
            method_false_pos = sum(1 for e in method_evals if e.feq_score.false_positive)
            method_avg_feq = sum(e.feq_score.total_score for e in method_evals) / len(method_evals)
            print(f"  {method.value}:")
            print(f"    Total failures: {len(method_evals)}")
            print(f"    True positives: {method_true_pos} ({method_true_pos/len(method_evals)*100:.2f}%)")
            print(f"    False positives: {method_false_pos} ({method_false_pos/len(method_evals)*100:.2f}%)")
            print(f"    Average FEQ score: {method_avg_feq:.2f}")
    
    print("\nOverall Summary:")
    print(f"Total failures evaluated: {len(evaluations)}")
    print(f"True positives: {true_positives} ({true_positives/len(evaluations)*100:.2f}%)")
    print(f"False positives: {false_positives} ({false_positives/len(evaluations)*100:.2f}%)")
    print(f"Average FEQ score: {avg_feq:.2f}")

if __name__ == "__main__":
    main() 