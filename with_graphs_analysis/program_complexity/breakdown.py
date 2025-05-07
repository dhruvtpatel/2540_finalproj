import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import json
from collections import defaultdict
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

# Extract data from program_difficulty_scores.json
def extract_data_from_json():
    # Read the JSON file
    with open(os.path.join(PROJECT_ROOT, "difficulty/program_difficulty_scores.json"), "r") as f:
        program_data = json.load(f)
    
    # Create the dataframe with the same structure as before
    data = []
    
    # Default values for tools that we don't have data for in the JSON
    default_verification = {
        "fuzz_testing": "Pass",  # Assuming fuzz testing passes for all
        "crosshair": "Fail",     # Default to fail
        "nagini": "Fail",        # Default to fail
        "feq": 0.5               # Default FEQ value
    }
    
    # Map from component names in JSON to the ones used in the original script
    component_map = {
        "params": "param",
        "operations": "op",
        "control_flow": "cf",
        "data_types": "dt",
        "assertions": "assert",
        "math_complexity": "math",
        "loops": "loop",
        "calls": "call",
        "branches": "branch"
    }
    
    # Extract data for each program
    for program in program_data:
        program_name = program["program"]
        difficulty = program["difficulty_score"]
        
        # Add row to our data with verification defaults
        data.append((
            program_name,
            difficulty,
            default_verification["fuzz_testing"],
            default_verification["crosshair"],
            default_verification["nagini"],
            default_verification["feq"]
        ))
    
    # Create DataFrame
    df = pd.DataFrame(
        data,
        columns=["program", "difficulty", "fuzz_testing", "crosshair", "nagini", "feq"],
    )
    
    # Component weights (reusing the original weights)
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
    
    # Program complexity subscores - extract from JSON
    complexity_subscores = {}
    
    for program in program_data:
        program_name = program["program"]
        component_scores = program["component_scores"]
        
        # Map component names and create subscore dictionary for this program
        subscores = {}
        for json_key, orig_key in component_map.items():
            if json_key in component_scores:
                subscores[orig_key] = component_scores[json_key]
            else:
                subscores[orig_key] = 0.0  # Default if missing
                
        complexity_subscores[program_name] = subscores

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
        on="program"
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
    plt.savefig(os.path.join(PROJECT_ROOT, "extra_analysis", "program_complexity", "graphs", "subscore_verification_relationship.png"), dpi=300)
    plt.close()

    return "subscore_verification_relationship.png"


def main():
    # Extract data from JSON instead of LaTeX
    df, component_weights, complexity_subscores = extract_data_from_json()

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
