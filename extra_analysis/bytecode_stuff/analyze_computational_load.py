import ast
import astor
import dis
import inspect
import textwrap
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import re
from typing import Dict, List, Tuple, Optional


def analyze_file(file_path):
    """Analyze a Python file for computational load between early comment and final assertion."""
    with open(file_path, "r") as file:
        lines = file.readlines()

    functions_data = {}
    current_function = None
    early_line_idx = None
    final_assert_idx = None
    function_body = []
    in_function = False
    starting_line = 0

    # Parse the file line by line
    for i, line in enumerate(lines):
        line = line.strip()

        # Check for function definition
        if line.startswith("def ") and "(" in line:
            # Process previous function if there was one
            if (
                current_function
                and early_line_idx is not None
                and final_assert_idx is not None
            ):
                # Extract code between early comment and final assertion
                between_code = function_body[early_line_idx + 1 : final_assert_idx]

                functions_data[current_function] = {
                    "early_comment": early_line_idx,
                    "final_assert": final_assert_idx,
                    "between_code": between_code,
                    "loc": len(between_code),
                    "instruction_count": 0,
                }

                # Count bytecode instructions
                count_bytecode_instructions(
                    functions_data[current_function], between_code
                )

            # Start new function
            func_name = line[4 : line.index("(")].strip()
            current_function = func_name
            function_body = []
            early_line_idx = None
            final_assert_idx = None
            in_function = True
            starting_line = i

        # If we're in a function, collect the lines
        elif in_function:
            rel_line = i - starting_line
            function_body.append(line)

            # Check for early assert comment
            if "#Early Assert HERE" in line:
                early_line_idx = rel_line

            # Check for final assertion
            if line.strip().startswith("assert "):
                final_assert_idx = rel_line

            # Check if function ended (empty line after indentation ends)
            if line == "" and len(function_body) > 0 and function_body[-1] == "":
                in_function = False

                # Process this function
                if (
                    current_function
                    and early_line_idx is not None
                    and final_assert_idx is not None
                ):
                    # Extract code between early comment and final assertion
                    between_code = function_body[early_line_idx + 1 : final_assert_idx]

                    functions_data[current_function] = {
                        "early_comment": early_line_idx,
                        "final_assert": final_assert_idx,
                        "between_code": between_code,
                        "loc": len(between_code),
                        "instruction_count": 0,
                    }

                    # Count bytecode instructions
                    count_bytecode_instructions(
                        functions_data[current_function], between_code
                    )

    # Process the last function if needed
    if (
        current_function
        and early_line_idx is not None
        and final_assert_idx is not None
        and in_function
    ):
        # Extract code between early comment and final assertion
        between_code = function_body[early_line_idx + 1 : final_assert_idx]

        functions_data[current_function] = {
            "early_comment": early_line_idx,
            "final_assert": final_assert_idx,
            "between_code": between_code,
            "loc": len(between_code),
            "instruction_count": 0,
        }

        # Count bytecode instructions
        count_bytecode_instructions(functions_data[current_function], between_code)

    return functions_data


def create_comparative_visualizations(data):
    """Create visualizations comparing computational overhead between assertions."""
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame.from_dict(data, orient="index")

    # Filter out functions without both early comment and final assertion
    df = df[df["early_comment"].notna() & df["final_assert"].notna()]

    # Sort by instruction count
    df = df.sort_values("instruction_count", ascending=False)

    # Create visualizations
    create_bar_chart(df)
    create_scatter_plot(df)
    create_bytecode_density_plot(df)

    return df


def create_bar_chart(df):
    """Create a bar chart of bytecode instruction counts."""
    plt.figure(figsize=(12, 8))

    # Limit to top 25 functions for readability
    if len(df) > 25:
        df_plot = df.head(25)
    else:
        df_plot = df

    plt.bar(df_plot.index, df_plot["instruction_count"], color="#1f77b4")
    plt.xticks(rotation=90)
    plt.xlabel("Function")
    plt.ylabel("Bytecode Instruction Count")
    plt.title(
        "Computational Overhead Between Early and Final Assertions (Bytecode Instructions)"
    )
    plt.tight_layout()
    plt.savefig("bytecode_instructions.png", dpi=300)
    plt.close()


def create_scatter_plot(df):
    """Create a scatter plot comparing instruction count to lines of code."""
    plt.figure(figsize=(12, 8))

    # Create scatter plot
    plt.scatter(df["loc"], df["instruction_count"], s=80, alpha=0.7)

    # Add labels for each point (limit to 25 for readability)
    df_labeled = df.head(25) if len(df) > 25 else df
    for i, func in enumerate(df_labeled.index):
        plt.annotate(
            func,
            (df_labeled["loc"].iloc[i], df_labeled["instruction_count"].iloc[i]),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=8,
        )

    # Add trend line
    z = np.polyfit(df["loc"], df["instruction_count"], 1)
    p = np.poly1d(z)
    plt.plot(df["loc"], p(df["loc"]), "r--", alpha=0.8)

    # Add correlation coefficient
    corr = df["loc"].corr(df["instruction_count"])
    plt.text(
        0.05,
        0.95,
        f"Correlation: {corr:.2f}",
        transform=plt.gca().transAxes,
        fontsize=10,
        bbox=dict(facecolor="white", alpha=0.8),
    )

    plt.xlabel("Lines of Code")
    plt.ylabel("Bytecode Instruction Count")
    plt.title("Relationship Between Code Size and Computational Overhead")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("loc_vs_instructions.png", dpi=300)
    plt.close()


def create_bytecode_density_plot(df):
    """Create a density plot showing bytecode instructions per line of code."""
    # Calculate density (instructions per line)
    df["instruction_density"] = df["instruction_count"] / df["loc"].apply(
        lambda x: max(x, 1)
    )

    plt.figure(figsize=(12, 8))

    # Sort by density
    df_sorted = df.sort_values("instruction_density", ascending=False)

    # Limit to top 25 functions for readability
    if len(df_sorted) > 25:
        df_plot = df_sorted.head(25)
    else:
        df_plot = df_sorted

    # Create bar chart
    bars = plt.bar(df_plot.index, df_plot["instruction_density"], color="#2ca02c")

    # Add value annotations
    for i, bar in enumerate(bars):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            f"{df_plot['instruction_density'].iloc[i]:.1f}",
            ha="center",
            va="bottom",
            fontsize=8,
        )

    plt.xticks(rotation=90)
    plt.xlabel("Function")
    plt.ylabel("Bytecode Instructions per Line of Code")
    plt.title("Computational Density Between Assertions")
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("bytecode_density.png", dpi=300)
    plt.close()


def function_categories(df):
    """Categorize functions based on their characteristics for further analysis."""
    categories = {
        "arithmetic": [],
        "string_processing": [],
        "list_processing": [],
        "loop_heavy": [],
        "control_flow": [],
    }

    # This is a simplified categorization based on function names
    # In a real implementation, you might analyze the AST more thoroughly
    for func in df.index:
        if any(
            term in func.lower()
            for term in [
                "sum",
                "calculator",
                "calculate",
                "discount",
                "quadratic",
                "acc",
            ]
        ):
            categories["arithmetic"].append(func)
        elif any(
            term in func.lower()
            for term in ["str", "string", "character", "ascii", "hash"]
        ):
            categories["string_processing"].append(func)
        elif any(
            term in func.lower() for term in ["list", "lst", "array", "nums", "values"]
        ):
            categories["list_processing"].append(func)
        elif any(
            term in func.lower()
            for term in ["loop", "nested", "iterator", "fibonacci", "counter"]
        ):
            categories["loop_heavy"].append(func)
        elif any(
            term in func.lower() for term in ["checker", "validator", "if", "triangle"]
        ):
            categories["control_flow"].append(func)

    # Create a category visualization
    plt.figure(figsize=(12, 8))

    # Collect data
    category_names = list(categories.keys())
    category_counts = [len(categories[cat]) for cat in category_names]
    category_instr_avg = []

    for cat in category_names:
        if categories[cat]:
            funcs = categories[cat]
            avg = df.loc[funcs, "instruction_count"].mean()
            category_instr_avg.append(avg)
        else:
            category_instr_avg.append(0)

    # Create the plot with dual axis
    fig, ax1 = plt.subplots(figsize=(12, 8))

    # Plot function counts
    color = "tab:blue"
    ax1.set_xlabel("Function Category")
    ax1.set_ylabel("Number of Functions", color=color)
    bars = ax1.bar(category_names, category_counts, color=color, alpha=0.6)
    ax1.tick_params(axis="y", labelcolor=color)

    # Add count labels
    for bar in bars:
        height = bar.get_height()
        ax1.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{int(height)}",
            ha="center",
            va="bottom",
            color=color,
            fontweight="bold",
        )

    # Create a second y-axis
    ax2 = ax1.twinx()
    color = "tab:red"
    ax2.set_ylabel("Average Instruction Count", color=color)
    ax2.plot(
        category_names, category_instr_avg, "o-", color=color, linewidth=2, markersize=8
    )
    ax2.tick_params(axis="y", labelcolor=color)

    # Add average labels
    for i, v in enumerate(category_instr_avg):
        ax2.text(i, v + 1, f"{v:.1f}", ha="center", color=color, fontweight="bold")

    fig.tight_layout()
    plt.title("Function Categories and Their Computational Overhead")
    plt.savefig("function_categories.png", dpi=300)
    plt.close()

    return categories


def generate_latex_table(df):
    """Generate a LaTeX table for the paper."""
    # Round numeric columns to 2 decimal places
    df_rounded = df.round(2)

    # Select relevant columns
    df_table = df_rounded[["instruction_count", "loc", "instruction_density"]]

    # Rename columns for better readability
    df_table = df_table.rename(
        columns={
            "instruction_count": "Bytecode Instructions",
            "loc": "Lines of Code",
            "instruction_density": "Instructions per Line",
        }
    )

    # Generate LaTeX table manually
    columns = list(df_table.columns)
    rows = df_table.index

    # Start building the LaTeX table
    latex_table = "\\begin{table}[h]\n\\centering\n\\begin{tabular}{|l|"

    # Add column specifications
    for _ in columns:
        latex_table += "r|"
    latex_table += "}\n\\hline\n"

    # Add header row
    latex_table += "Function & " + " & ".join(columns) + " \\\\\n\\hline\n"

    # Add data rows (limit to 25 for space)
    rows_to_show = list(rows)[:25] if len(rows) > 25 else rows
    for row in rows_to_show:
        latex_table += (
            row
            + " & "
            + " & ".join([str(df_table.loc[row, col]) for col in columns])
            + " \\\\\n"
        )

    # Close the table
    latex_table += "\\hline\n\\end{tabular}\n"
    latex_table += "\\caption{Computational Overhead Between Early and Final Assertions (Top 25 Functions)}\n"
    latex_table += "\\label{tab:computational_overhead}\n"
    latex_table += "\\end{table}"

    # Save to file
    with open("computational_overhead_table.tex", "w") as f:
        f.write(latex_table)

    return latex_table


def count_bytecode_instructions(function_data, code_lines):
    """Count bytecode instructions for code between assertions."""
    if not code_lines:
        function_data["instruction_count"] = 0
        return

    # Create a function containing just the code between assertions
    code_str = "\n".join(code_lines)

    # Indent the code properly
    code_str = textwrap.indent(code_str, "    ")

    # Create a function with this code
    func_str = f"def _temp_function():\n{code_str}\n    pass"

    try:
        # Compile and load the function
        namespace = {}
        exec(func_str, namespace)
        temp_func = namespace["_temp_function"]

        # Count bytecode instructions
        instruction_count = 0
        bytecode = dis.Bytecode(temp_func)
        for instr in bytecode:
            # Count each actual instruction (skip line numbers, etc.)
            if instr.opcode != dis.opmap.get("EXTENDED_ARG", -1):
                instruction_count += 1

        function_data["instruction_count"] = instruction_count
    except Exception as e:
        # Fallback: estimate based on how many lines we have, with a multiplier
        print(
            f"Warning: Couldn't analyze bytecode for function, falling back to line count * 3: {str(e)}"
        )
        function_data["instruction_count"] = len(code_lines) * 3  # Rough estimate


def main():
    # Analyze the file
    file_path = "../code/functions/functions.py"
    functions_data = analyze_file(file_path)

    # Create visualizations
    df = create_comparative_visualizations(functions_data)

    # Calculate instruction density
    df["instruction_density"] = df["instruction_count"] / df["loc"].apply(
        lambda x: max(x, 1)
    )

    # Analyze function categories
    categories = function_categories(df)

    # Generate LaTeX table
    latex_table = generate_latex_table(df)

    print(
        f"Analysis complete. Found {len(df)} functions with both early comment and final assertion."
    )
    print("Visualizations and LaTeX table have been generated.")

    # Display summary statistics
    print("\nSummary Statistics:")
    print(df[["instruction_count", "loc", "instruction_density"]].describe())

    # List functions by instruction count (top 25 if there are many)
    print("\nFunctions Ranked by Computational Overhead (Bytecode Instructions):")
    count = 0
    for func, instr_count in df["instruction_count"].items():
        print(f"{func}: {instr_count:.0f} instructions")
        count += 1
        if count >= 25:
            print(
                f"... and {len(df) - 25} more functions (showing top 25 of {len(df)})"
            )
            break


if __name__ == "__main__":
    main()
