import os
from typing import Any, Dict, Optional, Union, List, TypeVar
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

import with_graphs_analysis.bytecode.analyze_computational_load as acl

# Ensure graphs directory exists
def ensure_graphs_dir() -> str:
    """Create graphs directory if it doesn't exist."""
    graphs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "graphs")
    os.makedirs(graphs_dir, exist_ok=True)
    return graphs_dir


def create_complete_scatter_plot() -> Optional[Any]:
    """Create a scatter plot showing bytecode instruction counts for all functions."""
    if plt is None or acl is None or pd is None:
        print("Cannot create scatter plot: required libraries not installed")
        return None
        
    # Analyze the file to get the data
    file_path = os.path.join(PROJECT_ROOT, "code_files", "a_original_programs", "functions.py")
    functions_data = acl.analyze_file(file_path)
    
    # Check if functions_data is empty
    if not functions_data:
        print("No functions data found. The analyze_file function returned empty data.")
        return None

    # Debug - print the keys from the first function to verify structure
    if functions_data:
        first_func = next(iter(functions_data))
        print(f"First function: {first_func}")
        print(f"Keys in function data: {list(functions_data[first_func].keys())}")

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(functions_data, orient="index")
    
    # Check if expected columns exist
    if "early_comment" not in df.columns or "final_assert" not in df.columns:
        print(f"Missing expected columns. Available columns: {list(df.columns)}")
        # Try to proceed with available data
        if df.empty:
            print("DataFrame is empty, cannot proceed.")
            return None
    else:
        # Filter out functions without both early comment and final assertion
        df = df[df["early_comment"].notna() & df["final_assert"].notna()]

    # Sort by instruction count
    df = df.sort_values("instruction_count", ascending=False)

    # Create a figure with a larger size to accommodate all function names
    plt.figure(figsize=(20, 10))

    
    # Generate gradient colors for the bars
    if df.empty or "instruction_count" not in df.columns or df["instruction_count"].empty:
        # Fallback color if df is empty or instruction_count is not available/empty
        print("DataFrame is empty or 'instruction_count' is unsuitable for color mapping. Using default color for bars.")
        bar_colors: Union[str, List[Any]] = "skyblue"
    else:
        counts = df["instruction_count"]
        # Normalize counts to 0-1 range for the colormap
        norm = plt.Normalize(vmin=counts.min(), vmax=counts.max())
        # Get the 'viridis' colormap
        cmap = plt.cm.get_cmap('viridis')
        # Create a list of colors for the bars
        bar_colors = [cmap(norm(value)) for value in counts]

    # Create bar chart with function names on x-axis
    bars = plt.bar(df.index, df["instruction_count"], color=bar_colors, alpha=0.7)
    
    # Configure axes
    plt.xticks(rotation=90, fontsize=8)  # Rotate function names for readability
    plt.ylabel("Bytecode Instructions", fontsize=12)
    plt.title(
        "Bytecode Instructions Between Early and Final Assertions for All Functions",
        fontsize=14,
    )
    plt.grid(True, linestyle="--", alpha=0.7, axis="y")

    # Add a horizontal line for the mean
    mean_instructions = df["instruction_count"].mean()
    plt.axhline(mean_instructions, color="red", linestyle="-", alpha=0.6)
    plt.text(
        df.index[0] if not df.empty else 0,
        mean_instructions + 0.8,
        f"Mean: {mean_instructions:.2f} instructions",
        fontsize=10,
        color="red",
    )

    # Ensure enough space at the bottom for function names
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.3)

    # Save the figure to graphs directory
    graphs_dir = ensure_graphs_dir()
    plt.savefig(os.path.join(graphs_dir, "all_functions_bytecode.png"), dpi=300, bbox_inches="tight")
    plt.close()

    # Also create a boxplot to summarize the distribution
    if sns is not None and not df.empty:
        plt.figure(figsize=(10, 6))

        # Create boxplot
        sns.boxplot(y=df["instruction_count"])

        # Add individual points
        sns.stripplot(y=df["instruction_count"], color="red", alpha=0.5)

        # Add labels
        plt.ylabel("Bytecode Instructions")
        plt.title("Distribution of Bytecode Instructions Across All Functions")

        # Save figure to graphs directory
        plt.savefig(os.path.join(graphs_dir, "bytecode_distribution.png"), dpi=300)
        plt.close()
    else:
        print("Skipping boxplot creation: seaborn not installed or DataFrame is empty")

    # Print summary
    if not df.empty:
        print(f"Total functions analyzed: {len(df)}")
        print(f"Mean bytecode instructions: {mean_instructions:.2f}")
        print(f"Min instructions: {df['instruction_count'].min()}")
        print(f"Max instructions: {df['instruction_count'].max()}")
    else:
        print("No data to analyze.")
    
    print(f"Images saved to: {graphs_dir}")

    return df


if __name__ == "__main__":
    df = create_complete_scatter_plot()
    if df is not None and not df.empty:
        print("Plots created successfully!")
    else:
        print("Failed to create plots due to missing dependencies or empty data.")
