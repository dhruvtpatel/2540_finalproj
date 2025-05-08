import ast
import math
import inspect
import json
import os
from typing import Dict, List, Tuple, Any, Callable, Union, cast
from dataclasses import dataclass, asdict
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from code_files.a_original_programs.functions import *

@dataclass
class ComplexityMetrics:
    num_params: int
    num_operations: int
    control_flow_depth: int
    data_types: List[str]
    num_assertions: int
    math_complexity: float
    loop_complexity: float
    assertion_complexity: float
    call_complexity: float
    branch_complexity: float

class ProgramDifficultyRater(ast.NodeVisitor):
    def __init__(self):
        self.metrics = ComplexityMetrics(
            num_params=0,
            num_operations=0,
            control_flow_depth=0,
            data_types=[],
            num_assertions=0,
            math_complexity=0.0,
            loop_complexity=0.0,
            assertion_complexity=0.0,
            call_complexity=0.0,
            branch_complexity=0.0
        )
        self.current_depth = 0
        self.max_depth = 0
        self.loop_count = 0
        self.function_calls = 0
        self.branch_count = 0
        self.nested_loop_depth = 0
        self.max_nested_loop_depth = 0

    def _calculate_condition_complexity(self, node):
        if isinstance(node, ast.BoolOp):
            if isinstance(node.op, ast.And):
                return sum(self._calculate_condition_complexity(operand) for operand in node.values) * 1.5
            else:  # ast.Or
                return sum(self._calculate_condition_complexity(operand) for operand in node.values) * 1.2
        elif isinstance(node, ast.Compare):
            base_complexity = len(node.ops) * 0.5
            for op in node.ops:
                if isinstance(op, (ast.In, ast.NotIn)):
                    base_complexity += 0.8
                elif isinstance(op, (ast.Is, ast.IsNot)):
                    base_complexity += 0.6
                elif isinstance(op, (ast.Lt, ast.LtE, ast.Gt, ast.GtE)):
                    base_complexity += 0.4
            return base_complexity
        elif isinstance(node, ast.Call):
            return 0.5 + len(node.args) * 0.3
        elif isinstance(node, ast.UnaryOp):
            return 0.4 + self._calculate_condition_complexity(node.operand)
        elif isinstance(node, ast.BinOp):
            return 0.3 + self._calculate_condition_complexity(node.left) + self._calculate_condition_complexity(node.right)
        elif isinstance(node, ast.Constant):
            return 0.1
        elif isinstance(node, ast.Name):
            return 0.2
        return 0.3

    def _calculate_loop_complexity(self, node):
        complexity = 0.0
        complexity += self.nested_loop_depth * 0.5
        if isinstance(node, ast.While):
            complexity += self._calculate_condition_complexity(node.test)
        for child in ast.walk(node):
            if isinstance(child, ast.BinOp):
                complexity += 0.2
            elif isinstance(child, ast.Call):
                complexity += 0.3
        return complexity

    def visit_FunctionDef(self, node):
        self.metrics.num_params = len(node.args.args)
        for arg in node.args.args:
            if hasattr(arg, "annotation") and hasattr(arg.annotation, "id"):
                self.metrics.data_types.append(arg.annotation.id)
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.metrics.num_assertions += 1
        
        # Calculate base complexity from condition
        condition_complexity = self._calculate_condition_complexity(node.test)
        
        # Add complexity based on assertion length
        assertion_length = len(ast.unparse(node))
        length_complexity = min(assertion_length / 50, 2.0)  # Cap at 2.0
        
        # Add complexity for nested expressions
        nested_complexity = 0
        for child in ast.walk(node):
            if isinstance(child, (ast.BinOp, ast.Compare, ast.BoolOp)):
                nested_complexity += 0.3
            elif isinstance(child, ast.Call):
                nested_complexity += 0.4
        
        # Combine all complexity factors
        total_complexity = condition_complexity + length_complexity + nested_complexity
        self.metrics.assertion_complexity += total_complexity
        
        self.generic_visit(node)

    def visit_If(self, node):
        self.branch_count += 1
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        self.metrics.control_flow_depth = self.max_depth
        condition_complexity = self._calculate_condition_complexity(node.test)
        self.metrics.branch_complexity += condition_complexity
        if node.orelse:
            self.metrics.branch_complexity += 0.5
        self.generic_visit(node)
        self.current_depth -= 1

    def visit_For(self, node):
        self.loop_count += 1
        self.nested_loop_depth += 1
        self.max_nested_loop_depth = max(self.max_nested_loop_depth, self.nested_loop_depth)
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        self.metrics.control_flow_depth = self.max_depth
        loop_complexity = self._calculate_loop_complexity(node)
        self.metrics.loop_complexity += loop_complexity
        self.generic_visit(node)
        self.current_depth -= 1
        self.nested_loop_depth -= 1

    def visit_While(self, node):
        self.loop_count += 1
        self.nested_loop_depth += 1
        self.max_nested_loop_depth = max(self.max_nested_loop_depth, self.nested_loop_depth)
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        self.metrics.control_flow_depth = self.max_depth
        loop_complexity = self._calculate_loop_complexity(node)
        self.metrics.loop_complexity += loop_complexity
        self.generic_visit(node)
        self.current_depth -= 1
        self.nested_loop_depth -= 1

    def visit_BinOp(self, node):
        self.metrics.num_operations += 1
        if isinstance(node.op, (ast.Mult, ast.Div, ast.FloorDiv, ast.Mod)):
            self.metrics.math_complexity += 0.4
        elif isinstance(node.op, ast.Pow):
            self.metrics.math_complexity += 0.8
        self.generic_visit(node)

    def visit_Call(self, node):
        self.function_calls += 1
        call_complexity = 0.0
        if isinstance(node.func, ast.Name):
            if node.func.id in ["round", "abs"]:
                self.metrics.math_complexity += 0.3
                call_complexity = 0.3
            elif node.func.id in ["complex", "factorial", "sqrt", "hypot"]:
                self.metrics.math_complexity += 0.9
                call_complexity = 0.9
            elif node.func.id == node.func.id:  # Recursive call
                call_complexity = 1.0
        elif isinstance(node.func, ast.Attribute):
            attr = node.func.attr
            if attr in ["sqrt", "factorial", "hypot", "ceil"]:
                self.metrics.math_complexity += 0.9
                call_complexity = 0.9
        call_complexity += len(node.args) * 0.2
        self.metrics.call_complexity += call_complexity
        self.generic_visit(node)

def calculate_difficulty_score(
    metrics: ComplexityMetrics, loop_count=0, function_calls=0, branch_count=0
) -> Tuple[float, Dict[str, float]]:
    weights = {
        "params": 0.3,
        "operations": 0.4,
        "control_flow": 0.7,
        "data_types": 0.25,
        "assertions": 0.2,
        "math_complexity": 0.5,
        "loop_complexity": 0.6,
        "assertion_complexity": 0.8,
        "call_complexity": 0.35,
        "branch_complexity": 0.5,
        "bytecode_complexity": 0.45
    }

    bytecode_complexity = (
        metrics.num_operations * 1.1 +
        metrics.control_flow_depth * 1.3 +
        metrics.loop_complexity * 1.2 +
        metrics.branch_complexity * 1.0 +
        metrics.assertion_complexity * 1.4
    )

    scores = {
        "params": (metrics.num_params ** 2.0) * weights["params"],
        "operations": (math.log2(metrics.num_operations + 1) * 4.5) * weights["operations"],
        "control_flow": (metrics.control_flow_depth ** 2.2) * weights["control_flow"],
        "data_types": (len(set(metrics.data_types)) ** 1.9) * weights["data_types"],
        "assertions": (metrics.assertion_complexity ** 1.5) * weights["assertions"],
        "math_complexity": (metrics.math_complexity ** 1.9) * weights["math_complexity"],
        "loop_complexity": (metrics.loop_complexity ** 1.8) * weights["loop_complexity"],
        "assertion_complexity": (metrics.assertion_complexity ** 1.8) * weights["assertion_complexity"],
        "call_complexity": (metrics.call_complexity ** 1.7) * weights["call_complexity"],
        "branch_complexity": (metrics.branch_complexity ** 1.8) * weights["branch_complexity"],
        "bytecode_complexity": (bytecode_complexity ** 1.5) * weights["bytecode_complexity"]
    }

    raw_score = sum(scores.values())
    base = math.atan(raw_score / 10.0) * 0.5 / math.pi  # Same as before
    power = math.pow(raw_score / 20.0, 0.6)  # Same as before
    exp = math.exp(raw_score / 60) / 8.0  # Same as before
    log = math.log2(raw_score + 3.0) * 0.15  # Same as before
    scaled_score = base + power + exp + log + 0.3  # Reduced offset to push simpler programs lower
    total_score = min(5.0, max(1.0, scaled_score))  # Clamped between 1-5
    return total_score, scores

def rate_program_difficulty(
    source_code: str,
) -> Tuple[float, Dict[str, float], ComplexityMetrics]:
    tree = ast.parse(source_code)
    visitor = ProgramDifficultyRater()
    visitor.visit(tree)
    score, breakdown = calculate_difficulty_score(
        visitor.metrics,
        visitor.loop_count,
        visitor.function_calls,
        visitor.branch_count,
    )
    return score, breakdown, visitor.metrics

def metrics_to_dict(metrics: ComplexityMetrics) -> Dict[str, Any]:
    result = asdict(metrics)
    result["data_types"] = ", ".join(metrics.data_types) if metrics.data_types else ""
    return result

# Test the difficulty rater on our programs
programs = {
    "process_data": process_data,
    "convert_temperature": convert_temperature,
    "calculate_discount": calculate_discount,
    "process_complex_number": process_complex_number,
    "transform_data": transform_data,
    "circle_area_diff": circle_area_diff,
    "triangle_checker": triangle_checker,
    "temperature_offset": temperature_offset,
    "quadratic_discriminant": quadratic_discriminant,
    "vector_norm": vector_norm,
    "hypotenuse_diff": hypotenuse_diff,
    "ascii_average": ascii_average,
    "list_balance": list_balance,
    "odd_sum_validator": odd_sum_validator,
    "string_pattern_score": string_pattern_score,
    "random_mod_calculator": random_mod_calculator,
    "digit_sum_processor": digit_sum_processor,
    "string_reversal_checker": string_reversal_checker,
    "ceiling_multiplier": ceiling_multiplier,
    "factorial_root_calculator": factorial_root_calculator,
    "prime_number_counter": prime_number_counter,
    "date_difference_calculator": date_difference_calculator,
    "modulo_scaler": modulo_scaler,
    "text_frequency_analyzer": text_frequency_analyzer,
    "gcd_calculator": gcd_calculator,
    "hexadecimal_converter": hexadecimal_converter,
    "mean_absolute_deviation": mean_absolute_deviation,
    "password_strength_checker": password_strength_checker,
    "rectangle_overlap_area": rectangle_overlap_area,
    "collatz_sequence_length": collatz_sequence_length,
    "word_frequency_counter": word_frequency_counter,
    "binary_hamming_distance": binary_hamming_distance,
    "geometric_sequence_sum": geometric_sequence_sum,
    "caesar_cipher_encoder": caesar_cipher_encoder,
    "matrix_determinant": matrix_determinant,
    "isbn_validator": isbn_validator,
    "day_of_week_calculator": day_of_week_calculator,
    "armstrong_number_checker": armstrong_number_checker,
    "binary_search_iterations": binary_search_iterations,
    "polygon_area_calculator": polygon_area_calculator,
    "sum_until_limit": sum_until_limit,
    "count_divisibles": count_divisibles,
    "index_weighted_sum": index_weighted_sum,
    "square_accumulator": square_accumulator,
    "nested_loop_checker": nested_loop_checker,
    "character_counter": character_counter,
    "rolling_maximum": rolling_maximum,
    "fibonacci_counter": fibonacci_counter,
    "loop_even_sum": loop_even_sum,
    "loop_string_hash": loop_string_hash,
}

# Create a list to store all results
all_results = []

print("Processing Program Difficulty Ratings...")
print("=" * 50)

for name, func in programs.items():
    source = inspect.getsource(cast(Any, func))
    difficulty, scores, metrics = rate_program_difficulty(source)
    
    # Create a dictionary for this program's results
    program_result = {
        "program": name,
        "difficulty_score": difficulty,
        "component_scores": {k: round(v, 2) for k, v in scores.items()},
        "metrics": metrics_to_dict(metrics),
        "code_stats": {}
    }
    
    # Get the tree and visitor again to access loop_count, function_calls, etc.
    tree = ast.parse(source)
    visitor = ProgramDifficultyRater()
    visitor.visit(tree)
    
    program_result["code_stats"] = {
        "loop_count": visitor.loop_count,
        "function_calls": visitor.function_calls,
        "branch_count": visitor.branch_count
    }
    
    all_results.append(program_result)
    
    # Print basic info to console
    print(f"Processed: {name} (Score: {difficulty:.2f})")

# Sort the results by difficulty score (descending)
all_results.sort(key=lambda x: cast(float, x["difficulty_score"]), reverse=True)

# Ensure the difficulty directory exists
os.makedirs("difficulty", exist_ok=True)

# Write results to JSON file
output_file = os.path.join("difficulty", "program_difficulty_scores.json")
with open(output_file, "w") as f:
    json.dump(all_results, f, indent=2)

print("\nCompleted processing all programs.")
print(f"Results written to: {output_file}")
print(f"Total programs analyzed: {len(all_results)}")

def generate_latex_table(results: List[Dict[str, Any]]) -> str:
    """Generate a LaTeX table for the difficulty scores."""
    # Start building the LaTeX table
    latex_table = "\\begin{table}[h]\n\\centering\n\\scriptsize\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{lrrrrrrrrrr}\n\\toprule\n"
    
    # Add headers
    headers = [
        "\\textbf{Function}", "\\textbf{Score}", "\\textbf{Params}", "\\textbf{Ops}", 
        "\\textbf{CF}", "\\textbf{Types}", "\\textbf{Assert}", "\\textbf{Math}", 
        "\\textbf{Loops}", "\\textbf{Calls}", "\\textbf{Branches}"
    ]
    latex_table += " & ".join(headers) + " \\\\\n\\midrule\n"
    
    # Add data rows
    for result in results:
        row = [
            result["program"].replace("_", "\\_"),  # Escape underscores
            f"{result['difficulty_score']:.2f}",
            f"{result['component_scores']['params']:.2f}",
            f"{result['component_scores']['operations']:.2f}",
            f"{result['component_scores']['control_flow']:.2f}",
            f"{result['component_scores']['data_types']:.2f}",
            f"{result['component_scores']['assertions']:.2f}",
            f"{result['component_scores']['math_complexity']:.2f}",
            f"{result['component_scores']['loop_complexity']:.2f}",
            f"{result['component_scores']['call_complexity']:.2f}",
            f"{result['component_scores']['branch_complexity']:.2f}"
        ]
        latex_table += " & ".join(row) + " \\\\\n"
    
    # Close the table
    latex_table += "\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n"
    latex_table += "\\caption{Program Difficulty Scores and Component Scores}\n"
    latex_table += "\\label{tab:program_difficulty}\n"
    latex_table += "\\end{table}"
    
    return latex_table

# Generate and write LaTeX table
latex_table = generate_latex_table(all_results)
latex_file = os.path.join("difficulty", "program_difficulty_scores.tex")
with open(latex_file, "w") as f:
    f.write(latex_table)
print(f"\nLaTeX table written to: {latex_file}")