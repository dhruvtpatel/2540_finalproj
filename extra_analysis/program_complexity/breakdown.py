import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from collections import defaultdict


# Extract data from final_writeup.tex
def extract_data_from_latex():
    # This data is from the appendix table in final_writeup.tex
    # Format: program_name, difficulty, fuzz_testing, crosshair, nagini, feq
    data = [
        ("process_data", 5.00, "Pass", "Fail", "Fail", 0.5),
        ("convert_temperature", 6.00, "Pass", "Fail", "Fail", 0.7),
        ("calculate_discount", 6.00, "Pass", "Fail", "Fail", 0.7),
        ("process_complex_number", 6.00, "Pass", "Pass", "Fail", 0.9),
        ("transform_data", 6.00, "Pass", "Pass", "Pass", 0.0),
        ("circle_area_diff", 7.00, "Pass", "Pass", "Fail", 0.4),
        ("triangle_checker", 7.00, "Pass", "Pass", "Fail", 0.4),
        ("temperature_offset", 7.00, "Pass", "Pass", "Fail", 0.4),
        ("quadratic_discriminant", 9.00, "Pass", "Fail", "Fail", 0.7),
        ("vector_norm", 8.00, "Pass", "Pass", "Fail", 0.4),
        ("hypotenuse_diff", 9.00, "Pass", "Pass", "Pass", 0.4),
        ("ascii_average", 6.00, "Pass", "Pass", "Pass", 0.0),
        ("list_balance", 8.00, "Pass", "Pass", "Fail", 0.4),
        ("odd_sum_validator", 6.00, "Pass", "Pass", "Pass", 0.0),
        ("string_pattern_score", 5.00, "Pass", "Pass", "Pass", 0.0),
        ("random_mod_calculator", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("digit_sum_processor", 9.00, "Pass", "Fail", "Fail", 0.5),
        ("random_value_adjuster", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("ceiling_multiplier", 6.00, "Pass", "Fail", "Fail", 0.5),
        ("factorial_root_calculator", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("digit_length_scorer", 9.00, "Pass", "Fail", "Fail", 0.5),
        ("random_double_modulo", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("modulo_scaler", 6.00, "Pass", "Fail", "Fail", 0.5),
        ("random_adjustment_calculator", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("factorial_mod_processor", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("modular_doubler", 6.00, "Pass", "Fail", "Fail", 0.5),
        ("ceiling_adjustment_calculator", 6.00, "Pass", "Fail", "Fail", 0.5),
        ("random_sequence_generator", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("digit_sum_multiplier", 9.00, "Pass", "Fail", "Fail", 0.5),
        ("factorial_square_root_mod", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("decimal_ceiling_adjuster", 6.00, "Pass", "Fail", "Fail", 0.5),
        ("modular_scaling_calculator", 6.00, "Pass", "Fail", "Fail", 0.5),
        ("digit_count_processor", 9.00, "Pass", "Fail", "Fail", 0.5),
        ("random_mod_adjuster", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("factorial_root_modulo", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("random_pair_modulo", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("digit_pair_calculator", 9.00, "Pass", "Fail", "Fail", 0.5),
        ("modular_multiplication_scaler", 6.00, "Pass", "Fail", "Fail", 0.5),
        ("float_ceiling_adjuster", 6.00, "Pass", "Fail", "Fail", 0.5),
        ("factorial_modulo_processor", 7.00, "Pass", "Fail", "Fail", 0.5),
        ("sum_until_limit", 5.60, "Pass", "Fail", "Fail", 0.8),
        ("count_divisibles", 5.47, "Pass", "Pass", "Pass", 0.0),
        ("index_weighted_sum", 4.82, "Pass", "Fail", "Fail", 0.5),
        ("square_accumulator", 4.82, "Pass", "Pass", "Pass", 0.0),
        ("nested_loop_checker", 6.01, "Pass", "Fail", "Fail", 0.5),
        ("character_counter", 4.26, "Pass", "Pass", "Pass", 0.0),
        ("rolling_maximum", 4.60, "Pass", "Pass", "Pass", 0.0),
        ("fibonacci_counter", 4.66, "Pass", "Fail", "Fail", 0.5),
        ("loop_even_sum", 7.82, "Pass", "Pass", "Fail", 0.4),
        ("loop_string_hash", 4.82, "Pass", "Pass", "Pass", 0.6),
    ]

    # Create DataFrame
    df = pd.DataFrame(
        data,
        columns=["program", "difficulty", "fuzz_testing", "crosshair", "nagini", "feq"],
    )

    # Component weights from the LaTeX file
    component_weights = {
        "param": 0.40,  # Parameter Complexity
        "op": 0.45,  # Operation Density
        "cf": 0.60,  # Control Flow Depth
        "dt": 0.25,  # Data Type Diversity
        "assert": 0.20,  # Assertion Complexity
        "math": 0.55,  # Mathematical Sophistication
        "loop": 0.50,  # Loop Complexity
        "call": 0.40,  # Function Call Density
        "branch": 0.45,  # Branching Complexity
    }

    # Program complexity subscores from the LaTeX file - actual data
    complexity_subscores = {
        "process_data": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.60,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.06,
            "loop": 0.00,
            "call": 0.00,
            "branch": 0.45,
        },
        "convert_temperature": {
            "param": 0.40,
            "op": 3.60,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.37,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "calculate_discount": {
            "param": 1.60,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.16,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "process_complex_number": {
            "param": 1.60,
            "op": 0.00,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.65,
            "loop": 0.00,
            "call": 2.59,
            "branch": 0.00,
        },
        "transform_data": {
            "param": 0.40,
            "op": 3.60,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.22,
            "loop": 0.00,
            "call": 0.00,
            "branch": 0.00,
        },
        "circle_area_diff": {
            "param": 0.40,
            "op": 4.65,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 1.43,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "triangle_checker": {
            "param": 3.60,
            "op": 1.80,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.00,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "temperature_offset": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.37,
            "loop": 0.00,
            "call": 1.30,
            "branch": 0.00,
        },
        "quadratic_discriminant": {
            "param": 3.60,
            "op": 4.65,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 1.43,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "vector_norm": {
            "param": 1.60,
            "op": 3.60,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 2.09,
            "loop": 0.00,
            "call": 1.30,
            "branch": 0.00,
        },
        "hypotenuse_diff": {
            "param": 1.60,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.65,
            "loop": 0.00,
            "call": 6.17,
            "branch": 0.00,
        },
        "ascii_average": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.06,
            "loop": 0.00,
            "call": 2.59,
            "branch": 0.00,
        },
        "list_balance": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.16,
            "loop": 0.00,
            "call": 4.22,
            "branch": 0.00,
        },
        "odd_sum_validator": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.22,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "string_pattern_score": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.06,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "random_mod_calculator": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "digit_sum_processor": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.16,
            "loop": 0.00,
            "call": 6.17,
            "branch": 0.00,
        },
        "random_value_adjuster": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "ceiling_multiplier": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.55,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "factorial_root_calculator": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 1.43,
            "loop": 0.00,
            "call": 2.59,
            "branch": 0.00,
        },
        "digit_length_scorer": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.16,
            "loop": 0.00,
            "call": 6.17,
            "branch": 0.00,
        },
        "random_double_modulo": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "modulo_scaler": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.00,
            "branch": 0.00,
        },
        "random_adjustment_calculator": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "factorial_mod_processor": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 1.43,
            "loop": 0.00,
            "call": 2.59,
            "branch": 0.00,
        },
        "modular_doubler": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.00,
            "branch": 0.00,
        },
        "ceiling_adjustment_calculator": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.55,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "random_sequence_generator": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "digit_sum_multiplier": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.16,
            "loop": 0.00,
            "call": 6.17,
            "branch": 0.00,
        },
        "factorial_square_root_mod": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 1.43,
            "loop": 0.00,
            "call": 2.59,
            "branch": 0.00,
        },
        "decimal_ceiling_adjuster": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.55,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "modular_scaling_calculator": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.00,
            "branch": 0.00,
        },
        "digit_count_processor": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.16,
            "loop": 0.00,
            "call": 6.17,
            "branch": 0.00,
        },
        "random_mod_adjuster": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "factorial_root_modulo": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 1.43,
            "loop": 0.00,
            "call": 2.59,
            "branch": 0.00,
        },
        "random_pair_modulo": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "digit_pair_calculator": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.16,
            "loop": 0.00,
            "call": 6.17,
            "branch": 0.00,
        },
        "modular_multiplication_scaler": {
            "param": 0.40,
            "op": 4.18,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.45,
            "loop": 0.00,
            "call": 0.00,
            "branch": 0.00,
        },
        "float_ceiling_adjuster": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.55,
            "loop": 0.00,
            "call": 0.40,
            "branch": 0.00,
        },
        "factorial_modulo_processor": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 1.43,
            "loop": 0.00,
            "call": 2.59,
            "branch": 0.00,
        },
        "sum_until_limit": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.60,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.00,
            "loop": 0.50,
            "call": 0.40,
            "branch": 0.45,
        },
        "count_divisibles": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.60,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.22,
            "loop": 0.50,
            "call": 0.00,
            "branch": 0.45,
        },
        "index_weighted_sum": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.22,
            "loop": 0.50,
            "call": 0.40,
            "branch": 0.00,
        },
        "square_accumulator": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.22,
            "loop": 0.50,
            "call": 0.40,
            "branch": 0.00,
        },
        "nested_loop_checker": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.06,
            "loop": 2.00,
            "call": 1.30,
            "branch": 0.00,
        },
        "character_counter": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.60,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.06,
            "loop": 0.50,
            "call": 0.00,
            "branch": 0.45,
        },
        "rolling_maximum": {
            "param": 0.40,
            "op": 1.80,
            "cf": 0.60,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.00,
            "loop": 0.50,
            "call": 0.40,
            "branch": 0.45,
        },
        "fibonacci_counter": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.06,
            "loop": 0.50,
            "call": 0.40,
            "branch": 0.00,
        },
        "loop_even_sum": {
            "param": 1.60,
            "op": 3.60,
            "cf": 0.60,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.22,
            "loop": 0.50,
            "call": 0.40,
            "branch": 0.45,
        },
        "loop_string_hash": {
            "param": 0.40,
            "op": 2.85,
            "cf": 0.00,
            "dt": 0.25,
            "assert": 0.20,
            "math": 0.22,
            "loop": 0.50,
            "call": 0.40,
            "branch": 0.00,
        },
    }

    return df, component_weights, complexity_subscores


def plot_subscore_verification_relationship(
    df, complexity_subscores, component_weights
):
    """
    Create a 3x3 grid of subplots, one for each component.
    Each subplot shows the relationship between the component score and verification success.
    """
    # Create a dataframe with all component scores
    component_df = pd.DataFrame()

    # Extract component scores for each program
    for program, scores in complexity_subscores.items():
        program_row = {"program": program}
        program_row.update(scores)
        component_df = pd.concat(
            [component_df, pd.DataFrame([program_row])], ignore_index=True
        )

    # Merge with verification results
    merged_df = pd.merge(
        component_df,
        df[["program", "fuzz_testing", "crosshair", "nagini"]],
        on="program",
    )

    # Set up the figure
    fig, axes = plt.subplots(3, 3, figsize=(15, 15))
    axes = axes.flatten()

    # Components to plot
    components = list(component_weights.keys())
    component_names = {
        "param": "Parameter Complexity",
        "op": "Operation Density",
        "cf": "Control Flow Depth",
        "dt": "Data Type Diversity",
        "assert": "Assertion Complexity",
        "math": "Mathematical Sophistication",
        "loop": "Loop Complexity",
        "call": "Function Call Density",
        "branch": "Branching Complexity",
    }

    # For each component, create a subplot
    for i, component in enumerate(components):
        ax = axes[i]

        # Get unique values for the component and sort them
        score_values = sorted(merged_df[component].unique())

        # For each verification method, calculate the number of passes for each score value
        verification_methods = [
            ("fuzz_testing", "Fuzz Testing", "blue"),
            ("crosshair", "CrossHair", "green"),
            ("nagini", "Nagini", "red"),
        ]

        for method, label, color in verification_methods:
            # Calculate number of passes for each score value
            passes = []
            for score in score_values:
                programs_with_score = merged_df[merged_df[component] == score]
                pass_count = (programs_with_score[method] == "Pass").sum()
                passes.append(pass_count)

            # Plot the line
            ax.plot(
                score_values, passes, marker="o", linewidth=2, label=label, color=color
            )

        # Set title and labels
        ax.set_title(component_names[component])
        ax.set_xlabel("Component Score")
        ax.set_ylabel("Number of Passing Programs")
        ax.grid(True, alpha=0.3)

        # Only show legend on the first subplot
        if i == 0:
            ax.legend()

    # Adjust layout and save
    plt.tight_layout()
    plt.savefig("subscore_verification_relationship.png", dpi=300)
    plt.close()

    return "subscore_verification_relationship.png"


def main():
    # Extract data
    df, component_weights, complexity_subscores = extract_data_from_latex()

    # Create the visualization
    output_file = plot_subscore_verification_relationship(
        df, complexity_subscores, component_weights
    )

    # Print results
    print("Program Complexity Analysis")
    print("==========================")
    print(f"Total programs analyzed: {len(df)}")
    print(
        f"Complexity distribution: Min={df['difficulty'].min()}, Max={df['difficulty'].max()}, Mean={df['difficulty'].mean():.2f}"
    )

    # Count passing and failing for each method
    fuzz_pass = (df["fuzz_testing"] == "Pass").sum()
    crosshair_pass = (df["crosshair"] == "Pass").sum()
    nagini_pass = (df["nagini"] == "Pass").sum()

    print("\nVerification Pass Counts:")
    print(f"  Fuzz Testing: {fuzz_pass}/{len(df)} ({fuzz_pass / len(df) * 100:.1f}%)")
    print(
        f"  CrossHair: {crosshair_pass}/{len(df)} ({crosshair_pass / len(df) * 100:.1f}%)"
    )
    print(f"  Nagini: {nagini_pass}/{len(df)} ({nagini_pass / len(df) * 100:.1f}%)")

    print("\nComplexity Component Weights:")
    sorted_components = sorted(
        component_weights.items(), key=lambda x: x[1], reverse=True
    )
    for component, weight in sorted_components:
        print(f"  {component}: {weight}")

    print(f"\nAnalysis complete. Visualization saved to: {output_file}")


if __name__ == "__main__":
    main()
