import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the data from the existing files or regenerate
import analyze_computational_load as acl


def create_complete_scatter_plot():
    """Create a scatter plot showing bytecode instruction counts for all functions."""
    # Analyze the file to get the data
    file_path = "../code/functions/functions.py"
    functions_data = acl.analyze_file(file_path)

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(functions_data, orient="index")

    # Filter out functions without both early comment and final assertion
    df = df[df["early_comment"].notna() & df["final_assert"].notna()]

    # Sort by instruction count
    df = df.sort_values("instruction_count", ascending=False)

    # Create a figure with a larger size to accommodate all function names
    plt.figure(figsize=(20, 10))

    # Create bar chart with function names on x-axis
    bars = plt.bar(df.index, df["instruction_count"], color="skyblue", alpha=0.7)

    # Color bars based on instruction count
    for i, bar in enumerate(bars):
        bar.set_color(
            plt.cm.viridis(
                df["instruction_count"].iloc[i] / df["instruction_count"].max()
            )
        )

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
        df.index[0],
        mean_instructions + 0.8,
        f"Mean: {mean_instructions:.2f} instructions",
        fontsize=10,
        color="red",
    )

    # Ensure enough space at the bottom for function names
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.3)

    # Save the figure
    plt.savefig("all_functions_bytecode.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Also create a boxplot to summarize the distribution
    plt.figure(figsize=(10, 6))

    # Create boxplot
    sns.boxplot(y=df["instruction_count"])

    # Add individual points
    sns.stripplot(y=df["instruction_count"], color="red", alpha=0.5)

    # Add labels
    plt.ylabel("Bytecode Instructions")
    plt.title("Distribution of Bytecode Instructions Across All Functions")

    # Save figure
    plt.savefig("bytecode_distribution.png", dpi=300)
    plt.close()

    # Print summary
    print(f"Total functions analyzed: {len(df)}")
    print(f"Mean bytecode instructions: {mean_instructions:.2f}")
    print(f"Min instructions: {df['instruction_count'].min()}")
    print(f"Max instructions: {df['instruction_count'].max()}")

    return df


if __name__ == "__main__":
    df = create_complete_scatter_plot()
    print("Plots created successfully!")
