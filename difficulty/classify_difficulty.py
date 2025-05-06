import ast
import math
import inspect
from typing import Dict, List, Tuple
from dataclasses import dataclass
from code_files.a_original_programs.functions import *

@dataclass
class ComplexityMetrics:
    num_params: int
    num_operations: int
    control_flow_depth: int
    data_types: List[str]
    num_assertions: int
    math_complexity: int


class ProgramDifficultyRater(ast.NodeVisitor):
    def __init__(self):
        self.metrics = ComplexityMetrics(
            num_params=0,
            num_operations=0,
            control_flow_depth=0,
            data_types=[],
            num_assertions=0,
            math_complexity=0,
        )
        self.current_depth = 0
        self.loop_count = 0
        self.function_calls = 0
        self.branch_count = 0

    def visit_FunctionDef(self, node):
        self.metrics.num_params = len(node.args.args)
        for arg in node.args.args:
            if hasattr(arg, "annotation") and hasattr(arg.annotation, "id"):
                self.metrics.data_types.append(arg.annotation.id)
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.metrics.num_assertions += 1
        self.generic_visit(node)

    def visit_If(self, node):
        self.branch_count += 1
        self.current_depth += 1
        self.metrics.control_flow_depth = max(
            self.metrics.control_flow_depth, self.current_depth
        )
        self.generic_visit(node)
        self.current_depth -= 1

    def visit_For(self, node):
        self.loop_count += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.loop_count += 1
        self.generic_visit(node)

    def visit_BinOp(self, node):
        self.metrics.num_operations += 1
        if isinstance(node.op, (ast.Mult, ast.Div, ast.FloorDiv, ast.Mod)):
            self.metrics.math_complexity += 0.3
        elif isinstance(node.op, ast.Pow):
            self.metrics.math_complexity += 0.6
        self.generic_visit(node)

    def visit_Call(self, node):
        self.function_calls += 1
        if isinstance(node.func, ast.Name):
            if node.func.id in ["round", "abs"]:
                self.metrics.math_complexity += 0.2
            elif node.func.id in ["complex", "factorial", "sqrt", "hypot"]:
                self.metrics.math_complexity += 0.7
        elif isinstance(node.func, ast.Attribute):
            attr = node.func.attr
            if attr in ["sqrt", "factorial", "hypot", "ceil"]:
                self.metrics.math_complexity += 0.7
        self.generic_visit(node)


def calculate_difficulty_score(
    metrics: ComplexityMetrics, loop_count=0, function_calls=0, branch_count=0
) -> Tuple[int, Dict[str, float]]:
    weights = {
        "params": 0.4,
        "operations": 0.45,
        "control_flow": 0.6,
        "data_types": 0.25,
        "assertions": 0.2,
        "math_complexity": 0.55,
        "loops": 0.5,
        "calls": 0.4,
        "branches": 0.45,
    }

    scores = {
        "params": (metrics.num_params**2.0) * weights["params"],
        "operations": (math.log2(metrics.num_operations + 1) * 4)
        * weights["operations"],
        "control_flow": (metrics.control_flow_depth**2.2) * weights["control_flow"],
        "data_types": (len(set(metrics.data_types)) ** 1.8) * weights["data_types"],
        "assertions": (metrics.num_assertions**1.5) * weights["assertions"],
        "math_complexity": (metrics.math_complexity**1.8) * weights["math_complexity"],
        "loops": (loop_count**2.0) * weights["loops"],
        "calls": (function_calls**1.7) * weights["calls"],
        "branches": (branch_count**1.9) * weights["branches"],
    }

    raw_score = sum(scores.values())

    # Final scaling function with maximum spread
    base = (
        math.atan(raw_score / 1.0) * 7 / math.pi
    )  # Increased multiplier, decreased denominator
    power = math.pow(raw_score / 2.5, 0.6)  # More aggressive power scaling
    exp = math.exp(raw_score / 10) / 2  # More aggressive exponential
    log = math.log2(raw_score + 2)  # Added logarithmic component

    scaled_score = base + power + exp + log - 2  # Combined scaling with offset
    total_score = min(10, max(1, round(scaled_score)))

    return total_score, scores


def rate_program_difficulty(
    source_code: str,
) -> Tuple[int, Dict[str, float], ComplexityMetrics]:
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
    "random_value_adjuster": random_value_adjuster,
    "ceiling_multiplier": ceiling_multiplier,
    "factorial_root_calculator": factorial_root_calculator,
    "digit_length_scorer": digit_length_scorer,
    "random_double_modulo": random_double_modulo,
    "modulo_scaler": modulo_scaler,
    "random_adjustment_calculator": random_adjustment_calculator,
    "factorial_mod_processor": factorial_mod_processor,
    "modular_doubler": modular_doubler,
    "ceiling_adjustment_calculator": ceiling_adjustment_calculator,
    "random_sequence_generator": random_sequence_generator,
    "digit_sum_multiplier": digit_sum_multiplier,
    "factorial_square_root_mod": factorial_square_root_mod,
    "decimal_ceiling_adjuster": decimal_ceiling_adjuster,
    "modular_scaling_calculator": modular_scaling_calculator,
    "digit_count_processor": digit_count_processor,
    "random_mod_adjuster": random_mod_adjuster,
    "factorial_root_modulo": factorial_root_modulo,
    "random_pair_modulo": random_pair_modulo,
    "digit_pair_calculator": digit_pair_calculator,
    "modular_multiplication_scaler": modular_multiplication_scaler,
    "float_ceiling_adjuster": float_ceiling_adjuster,
    "factorial_modulo_processor": factorial_modulo_processor,
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


print("Program Difficulty Ratings:")
print("=" * 50)

for name, func in programs.items():
    source = inspect.getsource(func) # type: ignore
    difficulty, scores, metrics = rate_program_difficulty(source)

    print(f"\n{name}:")
    print(f"Overall Difficulty: {difficulty}/10")
    print("\nComponent Scores:")
    for component, score in scores.items():
        print(f"  {component:15} {score:.2f}")
    print("\nMetrics:")
    print(f"  Parameters:       {metrics.num_params}")
    print(f"  Operations:       {metrics.num_operations}")
    print(f"  Control Flow:     {metrics.control_flow_depth}")
    print(f"  Data Types:       {', '.join(metrics.data_types)}")
    print(f"  Assertions:       {metrics.num_assertions}")
    print(f"  Math Complexity:  {metrics.math_complexity:.1f}")
    print("-" * 50)
